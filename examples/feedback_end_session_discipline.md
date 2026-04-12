---
name: feedback_end_session_discipline
description: Never skip end-session steps — guards, code-map updates, and memory push compound across sessions
type: feedback
---

At every End Session, ALL maintenance steps must run — no exceptions, no "we didn't change much" excuses.

**Why:** The compounding effect. Each step feeds the next session. Skipping guard means bugs ship silently. Skipping code-map/index updates means the next session navigates blind. Skipping evolve-check means weak skills stay weak. One skipped session doesn't look bad — but three skipped sessions means the memory system is lying about the codebase state.

**How to apply:**
1. Run `/learn` — extract lessons and decisions
2. Run `/evolve-check` — check skill health
3. Run guards/scans — even if no code was edited this session (pre-existing bugs exist)
4. Update any code indexes or maps that reflect the current codebase
5. Update STATUS.md with session number + summary
6. Push to GitHub — never close without pushing
7. If context is low, at minimum: guards + index updates + push
