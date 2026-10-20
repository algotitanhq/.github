#!/usr/bin/env python3
"""Builds profile/assets/lab-{dark,light}.svg, the simplified agentic lab of the storagebits site, as standalone SVGs.

Source of truth: the site's partial (blok/templates/partials/labo.html) and its English strings (blok/i18n/en.toml).
GitHub serves README images through its proxy with no external loads, so fonts are subset and embedded;
the packets (SMIL) and the pulse around ALGOTITAN (CSS) still play.
Run: python gen/lab.py  (needs fonttools and brotli). Then commit profile/assets.
"""
import base64, html, io, re, tomllib
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

HOME = Path.home() / "projects"
PARTIAL = HOME / "blok/templates/partials/labo.html"
STRINGS = HOME / "blok/i18n/en.toml"
FONTS = HOME / "storagebits-profile/gen/fonts"
OUT = Path(__file__).resolve().parent.parent / "profile/assets"

THEMES = {  # Almanak Nocturne and Paper, the site's tokens
    "dark": dict(fond="#0E0D0B", carte="#16140F", texte="#F2EDE4", doux="rgba(242,237,228,.70)", pale="rgba(242,237,228,.46)",
                 trait="rgba(242,237,228,.12)", accent="#E89E5C", ambre="#F2B35B", bleu="#6E8BC2", vert="#6FB487"),
    "light": dict(fond="#EFE8DA", carte="#F6F1E7", texte="#1F1B16", doux="rgba(31,27,22,.72)", pale="rgba(31,27,22,.52)",
                  trait="rgba(31,27,22,.14)", accent="#B4532A", ambre="#B4532A", bleu="#3F5E96", vert="#3C7A52"),
}

CSS = """
.labo-lien{fill:none;stroke:{texte};stroke-opacity:.16;stroke-width:1.4}
.labo-zone{fill:{carte};stroke:{trait};stroke-dasharray:4 5}
.labo-zone-txt{font:400 11px M;fill:{pale}}
.paquet{fill:{ambre}}
.paquet.agent{fill:{texte};opacity:.75}
.labo-lien.agents{stroke:{ambre};stroke-opacity:.3}
.noeud circle{fill:{carte};stroke-width:2}
.noeud .halo{stroke:none;opacity:.14}
.noeud .nom{font:400 15px F;fill:{texte}}
.noeud .nom.petit{font:400 12px M;fill:{doux}}
.noeud .sous{font:400 11px M;fill:{pale}}
.noeud.humain circle{stroke:{ambre}}.noeud.humain .halo{fill:{ambre};opacity:.3}
.noeud.conscience circle{stroke:{bleu}}.noeud.conscience .halo{fill:{bleu}}
.noeud.memoire circle{stroke:{vert}}.noeud.memoire .halo{fill:{vert}}
.noeud.modele circle{stroke:{texte}}.noeud.modele .halo{fill:{texte}}
.noeud.societe circle{stroke:{accent};stroke-width:2.5}.noeud.societe .halo{fill:{accent};opacity:.22}
.noeud.coeur>circle:not(.halo){fill:{fond}}
.noeud.coeur .halo{animation:coeur 3.2s ease-in-out infinite;transform-origin:505px 220px}
@keyframes coeur{50%{opacity:.38;transform:scale(1.06)}}
.logo-algotitan .logo-a,.logo-algotitan .logo-pt{fill:{texte}}
.logo-algotitan .logo-agent{fill:{ambre}}
.logo-algotitan .logo-humain{fill:{accent}}
.noeud .logo-algotitan circle{stroke:none}
.noeud .nom.titre-org{font:400 19px F;letter-spacing:.12em;fill:{texte}}
.noeud.agent circle{stroke:{ambre}}.noeud.agent .halo{fill:{ambre}}
.noeud.mains circle{stroke:{accent}}.noeud.mains .halo{fill:{accent}}
.noeud.dehors circle{stroke:{pale}}.noeud.dehors .halo{fill:{pale}}
@media (prefers-reduced-motion:reduce){.paquet{display:none}.noeud.coeur .halo{animation:none}}
"""


def face(name, file, text):
    o = subset.Options(); o.flavor = "woff2"; o.layout_features = ["kern", "tnum", "lnum"]
    f = TTFont(FONTS / file); s = subset.Subsetter(o); s.populate(text=text + " "); s.subset(f)
    b = io.BytesIO(); f.flavor = "woff2"; f.save(b)
    return f"@font-face{{font-family:{name};src:url(data:font/woff2;base64,{base64.b64encode(b.getvalue()).decode()}) format('woff2')}}"


def main():
    s = tomllib.loads(STRINGS.read_text())["labo"]
    src = PARTIAL.read_text()
    body = src[src.index("<svg"):src.index("</svg>") + 6]
    body = re.sub(r"\{\{\s*s\.labo\.(\w+)\s*\}\}", lambda m: html.escape(s[m[1]]), body)
    body = body.replace('<svg viewBox="0 0 1000 430"',
                        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 430" width="1000" height="430"', 1)
    serif = "".join(re.findall(r'class="nom(?: titre-org)?"[^>]*>([^<]*)<', body))
    mono = "".join(re.findall(r'class="(?:sous|nom petit|labo-zone-txt)"[^>]*>([^<]*)<', body))
    fonts = face("F", "fraunces-400.ttf", serif) + face("M", "mono-400.ttf", mono)
    OUT.mkdir(parents=True, exist_ok=True)
    for theme, t in THEMES.items():
        css = CSS
        for k, v in t.items(): css = css.replace("{" + k + "}", v)
        svg = body.replace("<title", f"<style>{fonts}{css}</style><title", 1)
        svg = svg.replace("</title>", f'</title><rect width="1000" height="430" rx="16" fill="{t["fond"]}"/>', 1)
        (OUT / f"lab-{theme}.svg").write_text(svg)
        print(theme, len(svg))


if __name__ == "__main__":
    main()
