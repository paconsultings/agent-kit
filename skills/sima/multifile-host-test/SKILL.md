---
name: multifile-host-test
description: Multi-file test skill used to verify how `skills describe` renders manifest YAML and SKILL.md.
user-invocable: true
argument-hint: "[INPUT=<path>] [WORKDIR=<path>] [MODE=<dry-run|run>]"
---

# Multifile Host Test

Use this skill to verify that multi-file skills install correctly and that `skills describe` surfaces readable metadata.

## Inputs
- `INPUT`: Optional input file path.
- `WORKDIR`: Optional working directory for test outputs.
- `MODE`: Optional mode (`dry-run` by default).

## Files Included
- `scripts/check_env.py`: prints Python and platform info.
- `scripts/process_input.py`: simulates processing an input file.
- `configs/defaults.yaml`: sample runtime configuration.
- `README.md`: quick local usage notes.

## Workflow
1. Run `scripts/check_env.py` to verify host prerequisites.
2. Optionally run `scripts/process_input.py --input <file> --workdir <dir>`.
3. Inspect generated summary in the chosen workdir.

## Output
- Environment compatibility summary.
- Optional processed output summary file.
