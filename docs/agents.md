# Agents — Multi-Skill Orchestrators

Skills handle one step. Agents chain several skills into a complete workflow, with explicit human-in-the-loop breakpoints at every decision point.

---

## Built-in agents

| Agent | Steps |
|-------|-------|
| `feature-build` | search-first → plan → implement → code-reviewer → verification-loop → /learn |
| `bug-fix` | reproduce → isolate → fix → verify → log+learn |
| `end-session` | /learn → update memory → drift check → STATUS.md → evolve → sync |

---

## How they work

Each agent is a markdown file in `.claude/agents/`. Claude reads the steps in order. Every step ends with a `BREAKPOINT` — Claude stops, shows its findings or output, and waits for your explicit confirmation before proceeding.

```markdown
## Step 1 — Search

Run `/search-first` with the feature description.
Find every related function. Note call chains and DB tables involved.

**BREAKPOINT — Show findings. Wait for "continue" before Step 2.**

## Step 2 — Plan

Run `/plan` ...
```

You can abort, adjust, or redirect at any BREAKPOINT. Claude does not proceed automatically.

---

## Agents vs. skills

| | Skills | Agents |
|-|--------|--------|
| **Scope** | One step | Full workflow |
| **Trigger** | Phrase match or `/name` | Invoked by name |
| **Breakpoints** | None — runs to completion | Explicit BREAKPOINT at each step |
| **Chaining** | Via `## Auto-Chain` section | Explicit ordered steps |
| **When to use** | Single, well-defined task | Multi-step feature or bug fix |

---

## Writing your own agent

Drop a `.md` in `.claude/agents/`:

```markdown
---
name: my-workflow
description: When to invoke this orchestrator
---

## Step 1 — First thing

Do this. Check that. Report findings.

**BREAKPOINT — Show [what]. Wait for "continue" before Step 2.**

## Step 2 — Second thing

Do this next.
```

**Rules:**
- Every step should have exactly one `BREAKPOINT` at the end
- State what Claude should show at the breakpoint (findings, plan, review results)
- State what confirmation phrase to wait for
- Steps should map to skills where possible — `Run /skill-name` keeps agents thin and skills reusable
