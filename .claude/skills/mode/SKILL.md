---
name: mode
description: Switch Claude's tool access mode for the session. Modes limit which tools Claude will use — useful for reviewing code without risk of edits, or ensuring no shell commands run. Triggers on "Mode develop", "Mode review", "Mode safe", "Mode deploy", "/mode", "switch to review mode", "read only mode", "safe mode".
model: claude-sonnet-4-5
effort: low
allowed-tools: Read, Write
---

# Skill: mode

**Trigger:** `"Mode [develop|review|safe|deploy]"` · `"/mode"` · `"switch to review mode"` · `"read only mode"` · `"safe mode"`

---

## Modes

| Mode | Tools available | When to use |
|------|----------------|-------------|
| `develop` | All tools (default) | Normal coding sessions — full read/write/bash access |
| `review` | Read, Glob, Grep only | Reviewing code, auditing, reading without risk of changing anything |
| `safe` | Read, Edit, Write, Glob, Grep — no Bash | Making changes but no shell commands (no running scripts, no installs) |
| `deploy` | Read, Glob, Grep, Bash (deploy scripts only) | Production deploys — read + restart/deploy commands only, no source edits |

---

## Steps

### Step 1 — Parse the mode
Extract the mode name from the trigger: `develop`, `review`, `safe`, or `deploy`.

If no mode is specified, list the 4 options and ask which one.

### Step 2 — Write mode file
Write the mode name to `.claude/memory/tasks/current_mode.txt` (create if needed).

### Step 3 — Announce and self-enforce
Output a clear announcement and self-enforce the constraints for the rest of the session:

**develop:**
> Mode: DEVELOP — Full access. All tools available. (This is the default.)

**review:**
> Mode: REVIEW — Read-only. I will only use Read, Glob, and Grep for the rest of this session. No edits, no writes, no shell commands — even if asked. To restore full access: "Mode develop".

**safe:**
> Mode: SAFE — No shell. I will use Read, Edit, Write, Glob, Grep only. No Bash commands for the rest of this session — even if asked. To restore full access: "Mode develop".

**deploy:**
> Mode: DEPLOY — Deploy only. I will use Read, Glob, Grep, and Bash (deploy/restart scripts only). No source file edits for the rest of this session. To restore full access: "Mode develop".

### Step 4 — Enforce for the session
For the rest of the session, do not use any tool outside the active mode's allowed list — even if the user asks. If a restricted tool is needed, say: "Current mode is [X] — that tool is restricted. Say 'Mode develop' to restore full access, or confirm you want to proceed."

---

## Notes
- Mode resets to `develop` on the next session start
- No settings.json changes — mode is behavioral, not a permission file change
- `Mode develop` always restores full access immediately
