# Skill: java-reviewer

**Trigger:** "java review" or "review java" or "review this java" or "check the java"

**Description:** Java-specific code review. Goes deeper than a general code review on Java files — checks for common Java antipatterns, correctness issues, and project-specific conventions.

**Allowed Tools:** Read, Glob, Grep, Bash

---

## Steps

1. **Read the file(s)** being reviewed in full
2. **Run each checklist section** — report issues with file + line number

---

## Checklist

### SQL / Database Patterns
- [ ] No string concatenation for SQL values — use parameterized queries or safe quoting utilities
- [ ] No `SELECT *` — always explicit column list
- [ ] Single row queries check for results before accessing (`if (rowsFound > 0)`)
- [ ] Multi-row queries iterate safely with bounds check
- [ ] INSERT statements include all required audit fields (created date, created by, org)

### Java Patterns
- [ ] No raw types — use generics properly
- [ ] No unchecked casts without comment explaining why it's safe
- [ ] Resources properly closed (try-with-resources or finally block)
- [ ] No swallowed exceptions (`catch (Exception e) {}`)
- [ ] Null checks before dereferencing

### API / Endpoint Patterns
- [ ] Public endpoints registered in auth-bypass list (if applicable)
- [ ] Auth checks on protected endpoints
- [ ] Request parameters validated before use
- [ ] Error responses follow consistent format
- [ ] Both success and error paths return valid responses

### Response Structure
- [ ] Success and error paths both handled
- [ ] Error messages don't expose stack traces or internal details
- [ ] Response format matches what frontend expects

### Code Quality
- [ ] No duplicate logic that already exists elsewhere — reuse helpers
- [ ] Methods are focused — one responsibility per method
- [ ] No hardcoded values that should be config/constants

---

## Report Format

For each issue found:
```
❌ [File] line [N]: [issue description]
   Fix: [specific fix]
```

For clean files:
```
✅ [File] — No issues found
```

---

## Notes

- Customize this checklist for your specific framework (Spring Boot, Resin, etc.)
- Add project-specific patterns to the checklist as you discover them via `/learn`
- Focus on correctness and security — style issues are secondary
