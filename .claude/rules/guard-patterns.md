# Guard Patterns — Named Checks That Prevent Known Mistakes

Each entry: ID, what to check, how to grep for it, which files, and why it matters.
Run `Guard Check` to scan all guards automatically.
Add a guard when you catch the same mistake twice.

---

## NULL_BEFORE_ACCESS
- **Check**: Never access a property on a value that could be null/undefined without a null guard
- **How to scan**: Grep for `\.map\(` or `\.forEach\(` on variables that come from API calls — verify there is a null check before the call
- **Files**: All JS/TS component and utility files
- **Why**: API calls can return null; unguarded property access throws and crashes the entire render tree

## HARDCODED_URL
- **Check**: No hardcoded localhost URLs or environment-specific strings in source files
- **How to scan**: Grep for `localhost:` in non-test source files
- **Files**: All JS, config files — exclude test files and .env files
- **Why**: Hardcoded dev URLs ship to production silently; symptoms are 404s that only appear in prod

## RAW_ERROR_EXPOSURE
- **Check**: Never return raw exception messages directly to the frontend response
- **How to scan**: Grep for `catch` blocks that pass `e.message` or `error.message` directly into a response object
- **Files**: All backend route, controller, and handler files
- **Why**: Stack traces and internal paths are exposed via raw exception messages — security surface and information leak

## CONSOLE_LOG_LEFT_IN
- **Check**: No `console.log` statements in production code paths
- **How to scan**: Grep for `console\.log\(` in source files, excluding test files
- **Files**: All JS/TS source files — exclude *.test.*, *.spec.*
- **Why**: console.log left in production floods browser consoles, leaks internal state, and is unprofessional

---

*Name guards clearly — the ID is what gets referenced when a violation is found.*
*Grep patterns use backtick-wrapped regex: the Guard Check command extracts and runs them automatically.*
