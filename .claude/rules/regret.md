---
description: Rejected approaches — read before proposing solutions to avoid re-proposing already-discarded ideas
alwaysApply: true
---

# Rejected Approaches — Don't Propose These Again

Read before suggesting a solution. These were tried, evaluated, and discarded.

---

| Approach | Why Rejected |
|---|---|
| Nested async/API calls inside callbacks | Invisible coupling, hard to trace — use module-level globals to carry state across the boundary; each step gets its own top-level named callback |
| Writing a full file replacement (>1500 lines) in a single Write call | Exceeds single-response output limit; agent stalls before finishing — use targeted Edit calls instead |
| Sending raw base64 via API without URL-safe encoding | `+` in standard base64 → URL-decoded as space → corrupted binary files on disk. Always convert before sending: `base64.replace(/\+/g, '-').replace(/\//g, '_')`; server reverses before decoding |
| Em-dashes (`—`) or smart quotes in PowerShell string literals | PS parser breaks silently — use plain hyphens and straight quotes only |
| `$variables` in PowerShell passed via Bash tool | Bash interpolates `$var` before PS sees it — use single quotes around the command, or write the script to a file and run the file |
| Filtered SQL indexes (`CREATE INDEX ... WHERE col IS NOT NULL`) on tables the app writes to | SQL Server requires `SET QUOTED_IDENTIFIER ON` for all DML on a table with a filtered index — JDBC drivers don't guarantee this setting; every INSERT/UPDATE/DELETE silently fails. Use plain unfiltered indexes. |
| Multiple PostToolUse hook scripts (one per event type) | N processes spawn per file save — use a single dispatcher script that reads the event type and routes internally |
