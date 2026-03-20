# Skill: evolve

**Trigger:** `/evolve` or "evolve lessons into skills" or "cluster patterns into skills"

**Description:** Reviews accumulated lessons.md entries, identifies repeated patterns, and proposes or creates new reusable skills. Turns hard-won session knowledge into formalized, reusable workflow.

**Allowed Tools:** Read, Edit, Write, Glob, Bash

---

## Steps

1. **Read memory files:**
   - `.claude/memory/lessons.md`
   - `.claude/memory/decisions.md` (if exists)

2. **Identify repeated patterns:**
   - Look for entries with the same root cause or "Apply when" condition
   - Flag patterns that appear 2+ times across sessions

3. **Check for existing skill coverage:**
   - List all skills in `.claude/skills/`
   - For each repeated pattern, check if an existing skill already covers it

4. **For uncovered repeated patterns, propose:**
   ```
   Pattern: [description]
   Appeared: N times
   Suggested skill name: [name]
   Create it? (yes/no)
   ```

5. **On confirmation, create the skill:**
   - Create `.claude/skills/[name]/SKILL.md`
   - Include: trigger phrase, description, allowed tools, step-by-step instructions, notes
   - Make steps specific to your actual stack and patterns

6. **Report:** "Created N new skills: [list]"

---

## Skill File Format
```markdown
# Skill: [name]

**Trigger:** [exact phrase(s) that invoke this skill]

**Description:** [one sentence — what it does and when to use it]

**Allowed Tools:** Read, Edit, Write, Glob, Grep, Bash

---

## Steps
1. ...
2. ...

## Notes
- ...
```

---

## Notes

- Only create skills for patterns with clear, repeatable trigger conditions
- Generic advice ("always test") doesn't make a good skill — specific workflows do
- Run `/learn` before `/evolve` to ensure latest session patterns are captured
- After creating skills, update MEMORY.md index if your project uses one
