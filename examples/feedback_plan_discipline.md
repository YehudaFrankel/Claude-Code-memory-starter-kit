---
name: feedback_plan_discipline
description: Always show a full plan before code edits, then WAIT for user approval — no exceptions, no shortcuts
type: feedback
---

Every code edit requires the FULL plan format, then STOP and WAIT for user approval.

**Why:** "Small" changes compound into broken states when unplanned. Showing a plan and immediately editing defeats the purpose — the plan exists so the user can catch mistakes before they ship. Skipping the wait led to null reference errors and cascading breaks in a real session.

**How to apply:**
1. Every edit to code files gets the full format: Problem, All Related Functions (verified), Before, After, Why, Scope/Blast Radius, Rollback
2. After showing the plan — STOP. Do not edit. Wait for "yes", "go ahead", "do it"
3. When revising a plan after feedback, re-present the COMPLETE plan — never just the delta
4. "It's just 3 lines" is not an excuse to skip the format
5. "It's a bug fix for code I just wrote" is not an excuse to skip the wait
6. The only exception: memory files and config files
