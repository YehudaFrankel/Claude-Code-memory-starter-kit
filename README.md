# Claude Recall — The Living System for Claude Code

[![v2.0.0](https://img.shields.io/badge/version-2.0.0-blue?style=flat-square)](https://github.com/YehudaFrankel/claude-recall/releases) [![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue?style=flat-square)](https://python.org/downloads) [![MIT License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE) [![Claude Code](https://img.shields.io/badge/Claude-Code-orange?style=flat-square)](https://claude.ai/claude-code)

![Session demo](demo.gif)

**Memory that syncs. Skills that evolve. Sessions that compound — not reset.**

Claude Code is stateless. Every session starts from zero — no memory of yesterday's decisions, no record of bugs already fixed, no knowledge of the approach you rejected last week. You re-explain. Claude re-suggests the same things. The same mistake happens twice.

Claude Recall is a living system on top of Claude Code. It doesn't just store context — it grows with your project, improves its own skills from failure data, and runs multi-step workflows without human checkpoints between each step.

---

## Before and After

**Without Claude Recall:**
```
Monday:    explain your project → work → close
Tuesday:   explain your project again → work → close
Wednesday: explain again → re-fix a bug you already fixed → close
```

**With Claude Recall:**
```
Monday:    Start Session → work → End Session
Tuesday:   Start Session → Claude remembers everything → work → End Session
Wednesday: Start Session → lessons from Monday applied automatically → better work
```

---

## Quick Start

**Requires:** Python 3.7+ · [Claude Code](https://claude.ai/claude-code)

```bash
# 1. Clone once
git clone https://github.com/YehudaFrankel/claude-recall.git

# 2. Run setup in your project (takes ~2 minutes)
cd your-project
python /path/to/claude-recall/setup.py

# 3. Inside Claude Code — every session from here on:
Start Session    ←  reads memory, applies lessons, picks up where you left off
End Session      ←  extracts lessons, syncs memory, done
```

Setup asks about your stack, configures itself, and builds everything automatically. No databases, no API keys, no cloud services — plain text files and git.

---

## Skills Fix Their Own Mistakes

When a built-in skill (like `fix-bug`) gets something wrong and you correct it, that correction gets logged. Run `/evolve` every few sessions and it rewrites the exact failing step using your failure data.

This is the **compound learning loop** — skills score themselves on every use, `/evolve` patches the ones that failed, and next session they're better. Automatically, without you touching them.

```
session work
     ↓
/learn  →  lessons.md + decisions.md + skill_scores.md (Y/N per skill)
                    ↓
             /evolve  →  reads Y scores → patches the failing step
                      →  clusters repeated lessons into new skills
                    ↓
             better skills next session
```

Run `/learn` before `End Session`. Run `/evolve` every 3–5 sessions. The same mistake is architecturally impossible after `/evolve` runs.

---

## It Stays Accurate Without Effort

Most memory tools go stale — you document once, code moves on. Claude Recall runs a **drift detector** (`check_memory.py`) after every file edit. It compares live code against Claude's memory and flags undocumented changes immediately:

```
DRIFT DETECTED
  JS functions not in memory (2):
    - submitForm
    - resetPanel
  CSS classes not in memory (1):
    - .card--highlighted
→ memory updated automatically
```

Silent when clean. No manual updates needed.

---

## Workflows Run Themselves

Claude acts, not just answers. Three autonomous behaviors ship out of the box:

**Skill chaining** — add `## Auto-Chain` to any skill and it triggers the next step on pass or fail. No human prompts between steps:
```
fix-bug → verification-loop → smoke-test
               ↓ if fail
           debug-topic → smoke-test
```

**Self-healing** — when a verify step fails, Claude attempts the minimal fix and retries once before escalating to you. Define the recovery in a `## Recovery` section in any skill.

**Auto end session** — the stop hook monitors every response. After 9pm with unsaved memory changes, it auto-commits and pushes to git. Memory is never lost even if you forget `End Session`.

---

## It Works on Any Machine

Memory is stored as plain markdown files in your project, synced to git. Pull your project on a new machine, type `Install Memory`, and Claude is fully up to speed — every lesson, every decision, every skill improvement carried over.

```bash
# New machine setup
git pull
Install Memory    ←  inside Claude Code
Start Session     ←  Claude knows everything
```

---

## Commands

### Every day
| Command | What it does |
|---------|-------------|
| `Start Session` | Reads memory, applies all lessons, picks up where you left off |
| `End Session` | Runs `/learn`, updates STATUS.md, syncs memory |
| `/learn` | Extracts lessons, scores skills (Y/N), logs velocity — run before End Session |
| `/evolve` | Patches failing skills, clusters repeated patterns into new reusable skills |
| `Should I compact?` | Guides safe context compaction without losing memory |

### Auto-triggered — just describe the situation
| What you say | What Claude does |
|-------------|-----------------|
| `"fix the bug where..."` | Root cause first, fix second, logged so it never happens again |
| `"review this file"` | Dead code, missing error handling, convention violations |
| `"check for security issues"` | SQL injection, missing auth, exposed data |
| `"is this ready for prod"` | Catches hardcoded dev values, runs deploy checklist |
| `"refactor this"` | Plan first, change second — no surprise rewrites |

### Setup and recovery
| Command | What it does |
|---------|-------------|
| `Setup Memory` | First-time setup |
| `Install Memory` | New machine — copies memory to Claude's system path |
| `Generate Skills` | Auto-creates skills tailored to your stack |
| `Update Kit` | Pull latest updates safely — memory and skills never touched |
| `Estimate: [task]` | Complexity, files, risks, written plan — before any code |
| `Handoff` | Generates `HANDOFF.md` — state, next tasks, key decisions |

---

## Architecture

Three tiers — most memory tools ship only the first.

**Tier 1 — Memory**
Persistent context across sessions. Codebase knowledge, decisions made, known bugs, rejected approaches. Syncs to git. Travels with the code. Applied at every `Start Session` before any code is touched.

**Tier 2 — Skills**
Auto-triggered workflows from natural language. Each skill scores itself on every use (`skill_scores.md`). `/evolve` reads the scores and patches failing steps — the compound learning loop closes without manual intervention.

**Tier 3 — Autonomous**
Skill chaining, self-healing, drift detection, and auto end session run without prompting. Claude works through multi-step tasks without human checkpoints between each step. Agentic score on a real production codebase: **8.5/10** — the remaining 1.5 is intentional (you still initiate sessions and approve plans).

---

## What Gets Created

```
your-project/
├── CLAUDE.md                        ← Claude's instructions for this project
├── STATUS.md                        ← Full session log — date + what changed
├── tools/
│   ├── check_memory.py              ← Drift detector — runs after every edit
│   ├── session_journal.py           ← Auto-captures session summary on every Stop
│   └── stop_check.py               ← Auto-pushes memory after 9pm if unsaved
└── .claude/
    ├── settings.json                ← Hooks: drift · session start · compact · stop
    ├── memory/
    │   ├── MEMORY.md                ← Index — auto-loaded every session
    │   ├── lessons.md               ← Every lesson extracted by /learn
    │   ├── decisions.md             ← Settled decisions — never re-debated
    │   ├── js_functions.md          ← Every JS function with description
    │   ├── backend_reference.md     ← Every API endpoint and DB pattern
    │   └── tasks/
    │       ├── skill_scores.md      ← Skill report card — /evolve reads this
    │       ├── skill_improvements.md← What /evolve patched and why
    │       ├── regret.md            ← Rejected approaches — never re-proposed
    │       └── velocity.md          ← Estimated vs actual — self-calibrating
    └── skills/
        ├── learn/                   ← /learn — extract lessons + score skills
        ├── evolve/                  ← /evolve — patch failing skills
        ├── fix-bug/
        ├── code-review/
        ├── verification-loop/
        └── strategic-compact/
```

Commit `.claude/memory/` and `.claude/skills/` to your repo. Memory and skills travel with the code.

---

## Real Results

Tested across **112 real development sessions** on a production codebase — legacy Java backend, 5 JS files, 100+ functions, multi-page frontend with scheduler, email system, and encrypted URL handling. Not a demo project.

- Sessions crashed mid-task — `Start Session` recovered every time, zero re-explanation needed
- Skills patched themselves via `/evolve` — the same skill failure never happened twice
- A Resin compiler bug discovered, fixed, and logged permanently — never cost another debugging session
- 21 undocumented functions caught on the first drift detection run

---

## Common Questions

**Do I need to understand how it all works to use it?**
No. `Start Session` and `End Session` are the whole interface. Everything else runs automatically or responds to plain English.

**Does it work with any language or framework?**
Yes. Setup asks about your stack and configures drift detection, skills, and memory for what you're actually using.

**What makes it different from other Claude memory tools?**
Most memory tools are static — you document once and things go stale. Claude Recall is a living system: memory stays accurate via drift detection, skills improve via the compound learning loop, and sessions compound instead of reset. The architecture is described in detail on the [website](https://yehudafrankel.github.io/claude-recall).

**What if I'm on a new computer?**
Pull your project, open Claude Code, type `Install Memory`. Claude is fully up to speed in seconds.

**Can I customize the skills?**
Yes — every skill is a plain markdown file. Edit them directly, or type `Generate Skills` and Claude creates new ones tailored to your specific stack and patterns.

---

**Requires:** Python 3.7+ · [Claude Code](https://claude.ai/claude-code) · No other dependencies

If Claude Recall saved you from re-explaining your project one more time, **[⭐ star it on GitHub](https://github.com/YehudaFrankel/claude-recall)** — it helps others find it.
