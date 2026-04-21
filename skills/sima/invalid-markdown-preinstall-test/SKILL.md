---
name: invalid-markdown-preinstall-test
description: This skill intentionally contains broken markdown frontmatter for preinstall validation testing.
user-invocable: true
argument-hint: "[fixture]"
bad_yaml: [unterminated
---

# Invalid Markdown Preinstall Test

This file intentionally includes malformed frontmatter and should fail validation.

## Why
- Used to test `sima-cli` preinstall check behavior.
