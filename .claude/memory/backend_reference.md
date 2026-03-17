---
name: [Project Name] backend reference
description: All API endpoints, DB patterns, and utility methods for the backend
type: reference
---

## API Endpoints

| Endpoint | Auth? | Purpose |
|----------|-------|---------|
| `getExample` | No | |

---

## DB Patterns

<!-- How to safely query, insert, update in this project -->

### Safe value quoting
```java
// Example: UFmt.fAddQuotes(value) — never raw string concat
```

### Single-row SELECT
```java
// Pattern for fetching one row
```

### Multi-row SELECT
```java
// Pattern for fetching multiple rows
```

### INSERT (append-only tables)
```java
// Direct SQL pattern
```

---

## Key Utility Methods

| Method | Purpose |
|--------|---------|
| `UtilClass.method(x)` | |
