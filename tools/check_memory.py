#!/usr/bin/env python3
"""
Claude Code memory drift checker.
Compares function names in JS files against js_functions.md,
and CSS class names against html_css_reference.md.

Usage:
  python tools/check_memory.py            # normal mode — always prints result
  python tools/check_memory.py --silent   # silent mode — prints only if drift found (used by hooks)

Run from the project root (or any subdirectory).

CONFIGURE the three blocks below for your project.
"""

import re
import sys
from pathlib import Path

SILENT = "--silent" in sys.argv

# ─── CONFIGURE FOR YOUR PROJECT ──────────────────────────────────────────────

# Locate project root (directory that contains this script's parent = tools/)
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent  # project root

# JS files to scan for top-level function definitions
JS_FILES = [
    # ROOT / "js/YourFunctions.js",
    # ROOT / "js/YourOtherFunctions.js",
]

# CSS files to scan for class definitions
CSS_FILES = [
    # ROOT / "css/YourStyle.css",
]

# CSS class prefix to track (e.g. r'\.(ttw-[\w-]+)' or r'\.(app-[\w-]+)')
# Set to r'\.([\w-]+)' to track ALL classes (noisy on large projects)
CSS_CLASS_PATTERN = r'\.(your-prefix-[\w-]+)'

# Modifier/state suffixes that are self-explanatory — skip forward-detection for these
MODIFIER_SUFFIXES = (
    '-active', '-open', '-disabled', '-locked', '-empty', '-success',
    '-error', '-loading', '-collapsed', '-dirty', '-sm', '-lg', '-xs',
    '-full', '-inline', '-new', '-replied', '-flush',
)

# ─────────────────────────────────────────────────────────────────────────────

MEMORY_DIR = ROOT / ".claude/memory"
JS_MEMORY  = MEMORY_DIR / "js_functions.md"
CSS_MEMORY = MEMORY_DIR / "html_css_reference.md"


FUNC_PATTERNS = [
    re.compile(r'^function\s+(\w+)\s*\(', re.MULTILINE),
    re.compile(r'^async\s+function\s+(\w+)\s*\(', re.MULTILINE),
    re.compile(r'^(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?function\s*\(', re.MULTILINE),
    re.compile(r'^(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>', re.MULTILINE),
    re.compile(r'^(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\w+\s*=>', re.MULTILINE),
    re.compile(r'^\s{2,}(\w+)\s*\([^)]*\)\s*\{', re.MULTILINE),
    re.compile(r'^\s+(\w+)\s*:\s*(?:async\s+)?function', re.MULTILINE),
]


def extract_js_functions(paths):
    """Extract all function names from JS files (top-level, arrow, class methods, object methods)."""
    found = {}  # name -> filename
    for path in paths:
        if not path.exists():
            if not SILENT:
                print(f"  WARN: JS file not found: {path}")
            continue
        if path.stat().st_size > 500_000:
            if not SILENT:
                print(f"  WARN: Skipping {path.name} — file exceeds 500KB (likely bundled/minified)")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in FUNC_PATTERNS:
            for m in pattern.finditer(text):
                name = m.group(1)
                if name not in found:
                    found[name] = path.name
    return found


def extract_memory_functions(md_path):
    """Extract function names listed in js_functions.md (backtick format, with or without params)."""
    if not md_path.exists():
        if not SILENT:
            print(f"  WARN: memory file not found: {md_path}")
        return set()
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    # Match | `functionName` | or | `functionName(params)` | table rows
    pattern = re.compile(r'\|\s*`(\w+)(?:\([^)]*\))?`\s*\|')
    return set(m.group(1) for m in pattern.finditer(text))


def extract_css_classes(paths):
    """Extract CSS class names matching CSS_CLASS_PATTERN from CSS files."""
    found = set()
    pattern = re.compile(CSS_CLASS_PATTERN)
    for path in paths:
        if not path.exists():
            if not SILENT:
                print(f"  WARN: CSS file not found: {path}")
            continue
        if path.stat().st_size > 500_000:
            if not SILENT:
                print(f"  WARN: Skipping {path.name} — file exceeds 500KB (likely bundled/minified)")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for m in pattern.finditer(text):
            found.add(m.group(1))
    return found


def extract_memory_css_classes(md_path):
    """Extract CSS class names matching CSS_CLASS_PATTERN from html_css_reference.md."""
    if not md_path.exists():
        return set()
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    pattern = re.compile(CSS_CLASS_PATTERN)
    return set(m.group(1) for m in pattern.finditer(text))


def main():
    if not JS_FILES and not CSS_FILES:
        if not SILENT:
            print("No JS_FILES or CSS_FILES configured. Edit tools/check_memory.py.")
        sys.exit(0)

    drift = False

    # --- JS function drift ---
    if JS_FILES:
        code_fns  = extract_js_functions(JS_FILES)
        mem_fns   = extract_memory_functions(JS_MEMORY)

        code_names = set(code_fns.keys())
        missing_from_memory = code_names - mem_fns
        stale_in_memory     = mem_fns - code_names

        if missing_from_memory:
            drift = True
            print("DRIFT DETECTED — MISSING from js_functions.md (exist in code):")
            for fn in sorted(missing_from_memory):
                print(f"  + {fn}  [{code_fns[fn]}]")

        if stale_in_memory:
            drift = True
            print("DRIFT DETECTED — STALE in js_functions.md (no longer in code):")
            for fn in sorted(stale_in_memory):
                print(f"  - {fn}")

    # --- CSS class drift ---
    if CSS_FILES and CSS_CLASS_PATTERN != r'\.(your-prefix-[\w-]+)':
        code_classes = extract_css_classes(CSS_FILES)
        mem_classes  = extract_memory_css_classes(CSS_MEMORY)

        stale_css = mem_classes - code_classes
        if stale_css:
            drift = True
            print("DRIFT DETECTED — STALE in html_css_reference.md (no longer in CSS):")
            for cls in sorted(stale_css):
                print(f"  - .{cls}")

        missing_css = code_classes - mem_classes
        significant_missing = {
            cls for cls in missing_css
            if not any(cls.endswith(suf) for suf in MODIFIER_SUFFIXES)
        }
        if significant_missing:
            drift = True
            print("DRIFT DETECTED — NEW CSS classes not yet in html_css_reference.md:")
            for cls in sorted(significant_missing):
                print(f"  + .{cls}")

    if not drift:
        if not SILENT:
            print("OK — no drift detected")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
