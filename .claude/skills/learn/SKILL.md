# Skill: learn

**Trigger:** `/learn` or "extract patterns" or "learn from this session"

**Description:** Extracts reusable patterns, lessons, and decisions from the current session and saves them to memory files. Run before End Session or before /compact to capture what was learned.

**Allowed Tools:** Read, Edit, Write, Glob, Grep

---

## Steps

1. **Review the current conversation for:**
   - Bugs fixed and their root causes
   - Patterns that worked well
   - Mistakes made and how they were corrected
   - Architectural decisions made
   - Stack-specific gotchas discovered

2. **Categorize findings:**
   - Bugs/errors → append to `.claude/memory/lessons.md` (create if missing)
   - Architectural decisions → append to `.claude/memory/decisions.md` (create if missing)
   - Repeated patterns (3+ times) → flag as skill candidate

3. **Format each entry as:**
   ```
   ## [YYYY-MM-DD] - [short title]
   **Context:** what you were doing
   **Problem:** what went wrong or what was learned
   **Solution/Pattern:** what works
   **Apply when:** trigger conditions
   ```

4. **After writing:**
   - Report: "Extracted N lessons: [list titles]"
   - If any pattern appeared 3+ times: "Suggest creating skill: [name] — run /evolve to cluster"

---

## Notes

- Never delete existing entries — only append
- Keep entries concise — one lesson per entry
- Run before End Session to preserve session knowledge
- Run before `/compact` to avoid losing insights
- If a pattern recurs across sessions, it belongs in a skill not just lessons.md
