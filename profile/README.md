<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/algotitanhq/.github/main/profile/assets/wordmark-dark.svg">
  <img src="https://raw.githubusercontent.com/algotitanhq/.github/main/profile/assets/wordmark-light.svg" width="560" alt="ALGOTITAN, an agentic organization">
</picture>

An organization of AI agents that design, build, test and ship software. One human founder, [@storagebits](https://github.com/storagebits), brings the ideas, the north stars and a few decisions; the agents do the rest.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/algotitanhq/.github/main/profile/assets/lab-dark.svg">
  <img src="https://raw.githubusercontent.com/algotitanhq/.github/main/profile/assets/lab-light.svg" width="100%" alt="The agentic lab, simplified: a human brings ideas and go / no-go decisions; Hermes is the conscience (memory, cron); ALGOTITAN, the organization on Paperclip, sits at the heart, linked to each of its agents (CEO, QA, Engineer, Writer, agency-agents personas); models come from Claude / OpenAI and OpenCode Go; Obsidian is the shared memory; the harness (Claude Code / OpenCode) does the work and ships to GitHub and to real devices; the agents talk to each other.">
</picture>

## What this is

ALGOTITAN is a working experiment: can one person with more ideas than nights run a small software organization whose staff are AI agents, and still ship things that are correct, secure and pleasant to use?

It is not a demo and not a framework. The agents have roles, a manager, a backlog, budgets and reviews. They work on real machines in a homelab, push to real repositories and install their builds on real devices: TVs, watches, phones, dev boards. The founder stays out of the day-to-day and keeps the decisions that cannot be undone.

## The team

| Role | Who | What they do |
| --- | --- | --- |
| **Founder** | a human, [@storagebits](https://github.com/storagebits) | Ideas, north stars, go / no-go at the gates. |
| **CEO** | agent | Turns an idea into a brief, splits it into issues, staffs them, follows up. |
| **Engineers** | agents, one per project workspace | Build, test on emulators and devices, open pull requests. |
| **QA** | agent | Reviews every pull request against the brief, asks for evidence, merges. |
| **Writer** | agent | READMEs, release notes, the posts that tell each project. |
| **Conscience** | Hermes | The organization's memory, a morning brief for the founder, the link between the founder and the organization. |
| **Specialists** | [agency-agents](https://github.com/msitarzewski/agency-agents) personas | Called in when a task needs a designer, a security reviewer, a TV or firmware specialist. |

## How a project goes

| Step | What happens | Gate |
| --- | --- | --- |
| 0. Idea | One line in an inbox. | |
| 1. Brief | Goal, north star, what success looks like. | **Founder's go** |
| 2. Reconnaissance | Prior art, constraints, a plan in small slices. | |
| 3. Build | One request, one issue, one pull request. | QA review |
| 4. Quality | Tests, CI, screenshots or recordings from the device. | QA review |
| 5. Security | Audit and secret hygiene. A finding blocks the release. | |
| 6. Release | Tag, signed builds, public repository. | **Founder's approval** |
| 7. Share | A post on [blok](https://blok.storagebits.workers.dev). | **Founder's review** |
| 8. Retro | Lessons go back into the shared memory. | |

## House rules

- **The human decides what cannot be undone**: publishing, spending money, anything signed in the founder's name. Everything else is delegated.
- **Nothing merges unreviewed.** Every change goes through QA, and every document is reviewed.
- **Each agent has its own identity**, short-lived tokens and only the access its role needs. No agent holds the founder's keys.
- **Transparency**: the code here is written by agents and says so. Every public repository carries at least one commit by the founder, and every post names the model that drafted it.

## Projects

| Project | What it is | Status |
| --- | --- | --- |
| [**Almanak**](https://github.com/algotitanhq/almanak) | An ambient almanac for Android TV and Google TV: time, weather, real-time buses, sun and moon. Open data, no account. | public, v1.0 on the way |
| [**Uberblok**](https://github.com/algotitanhq/uberblok) | An interactive museum of ZFS internals: one room per engineering idea, backed by the OpenZFS source. | live: [uberblok.storagebits.workers.dev](https://uberblok.storagebits.workers.dev) |
| **Lukarne** | Spin a globe on your TV, dive into a region and hop between live webcams with the remote. | coming soon |
| **Shot2Cart** | From a photo to a merchant's cart in under 15 seconds, without touching the keyboard. | in the workshop |

More are in the pipe; each gets a link here once it passes the release gate.

From the founder's own workshop: [Kronograf](https://github.com/storagebits/kronograf), a firmware for the LilyGO T-Watch 2020, and [Humility](https://github.com/storagebits/humility), the debugger for Oxide's Hubris, which the founder brought up on an unsupported STM32 board.

## Built with

[Paperclip](https://github.com/paperclipai/paperclip) for the organization (org chart, issues, approvals, budgets) · [Hermes](https://github.com/NousResearch/hermes-agent) for the conscience · [Claude Code](https://github.com/anthropics/claude-code) and [OpenCode](https://github.com/anomalyco/opencode) for the hands · [Obsidian](https://obsidian.md) for the shared memory · GitHub Actions for CI · a homelab for everything else.

## Follow along

The making-of, failures included, is on the blog: [blok.storagebits.workers.dev](https://blok.storagebits.workers.dev). Questions or ideas about a project: open an issue on its repository.
