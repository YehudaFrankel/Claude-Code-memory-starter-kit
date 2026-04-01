# Extending Clankbrain

Everything in `.claude/` is yours to modify. Three extension points: skills, agents, and rules.

---

## Add a skill

Drop a `SKILL.md` in `.claude/skills/<name>/`:

```markdown
---
name: my-skill
description: What triggers this skill (exact phrase Claude watches for)
allowed-tools: Read, Grep, Edit
---

## Steps

1. First step — what Claude does
2. Second step
3. ...
```

The `description` field is what Claude pattern-matches against your prompts. Make it the exact phrase you'd naturally say: `"review this PR"`, `"add a new endpoint"`, `"before I ship"`.

Or ask Claude directly: `Create a skill called [name] that [does what]` — it writes the file for you.

**→ See [skills.md](skills.md) for the full skill reference and learning loop.**

---

## Add an agent

Drop a `.md` in `.claude/agents/`:

```markdown
---
name: my-workflow
description: When to invoke this orchestrator
---

## Step 1 — First thing

Describe what Claude does here. Reference skills with `Run /skill-name`.

**BREAKPOINT — Show [what]. Wait for "continue" before Step 2.**

## Step 2 — Second thing

Next step.
```

**→ See [agents.md](agents.md) for the full agent reference and breakpoint patterns.**

---

## Add a path-scoped rule

Drop a `.md` in `.claude/rules/` with frontmatter:

```markdown
---
description: One-line summary for Claude Code's rule picker
globs:
  - "**/*.ts"
  - "**/*.tsx"
alwaysApply: false
---

## Your rule content
```

Remove it from the `@rules/` imports in CLAUDE.md so it only loads when the globs match — not on every turn.

**→ See [rules.md](rules.md) for always-load vs. path-scoped breakdown and recommended splits.**

---

## Keeping CLAUDE.md lean

CLAUDE.md should stay under 200 lines. Signs it's getting too long:

- Detailed coding conventions → move to a path-scoped rule
- Verbose command docs → condense to a Skill Map table
- Architecture deep-dives → move to a memory file or docs/

The Skill Map pattern:

```markdown
## Skill Map

| Workflow | Skills in Order |
|----------|----------------|
| New Feature | `/search-first` → `/plan` → *(code)* → `/code-reviewer` → `/learn` |
| Bug Fix | `/debug-session` → *(fix)* → `/verification-loop` → `/learn` |
| End of Session | `/learn` → `/evolve` *(every 3–5 sessions)* |
```

One table replaces pages of "when to use what" prose.
