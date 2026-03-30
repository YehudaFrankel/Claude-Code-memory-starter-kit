# Error Lookup — Known Errors → Cause → Fix

When Claude or a runtime throws a recognizable error, check here before investigating.
Add entries as you debug. Never debug the same error twice.

---

## Runtime / JS Errors

| Error message | Cause | Fix |
|---|---|---|
| `Cannot read properties of undefined (reading 'X')` | Component renders before data loads | Add null guard: `if (!data) return` before accessing data |
| `Module not found: Can't resolve 'X'` | Missing import or wrong path | Check file exists at exact path; verify casing (Linux is case-sensitive) |
| Event handler fires twice | Listener added inside a re-render | Move listener outside render; add cleanup in useEffect return |

---

## Auth / Session Errors

| Symptom | Cause | Fix |
|---|---|---|
| API returns 401 unexpectedly | Token expired or not sent | Check Authorization header is present and token is fresh |
| Login succeeds but user is immediately logged out | Session not persisted to storage | Check sessionStorage vs localStorage — pick one and use it consistently |

---

## DB / Query Errors

| Error message | Cause | Fix |
|---|---|---|
| `Duplicate entry for key 'PRIMARY'` | INSERT on existing PK | Use UPSERT / INSERT OR REPLACE pattern |
| `Column X cannot be null` | Required field missing from INSERT | Check all NOT NULL columns are included in the INSERT |

---

## Build / Compile Errors

| Error message | Cause | Fix |
|---|---|---|
| `SyntaxError: Unexpected token` | Usually a missing bracket or comma | Check the line ABOVE the reported line — error reporting is one line off |

---

*Each entry here is a bug that already cost time. It should never cost time again.*
