---
name: User preferences and working style
description: How the user wants Claude to communicate and behave
type: user
---

<!-- Fill in as you learn what works. Examples below. -->

- Keep responses short and direct — no preamble, no summaries after edits
- When user types "Start Session": check Python, run drift check, read STATUS.md, report — do NOT do this automatically on every file read
- When user types "End Session": update STATUS.md + all relevant memory files, sync to bundle, confirm clean
- Never update memory files mid-session unless explicitly asked — only on "End Session"
- Always update CLAUDE.md and STATUS.md after every code change
- Don't add comments or docstrings to code that wasn't changed
- Don't over-engineer — simplest solution that works
