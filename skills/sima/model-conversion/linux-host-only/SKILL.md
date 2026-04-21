---
name: model-conversion-linux
description: Run Linux-only model conversion workflows for CI and server environments.
argument-hint: [MODEL=<path>] [OUT_DIR=<path>] [TOOLCHAIN=<path>] [PROFILE=<name>]
---

# Model Conversion (Linux Host)

Run model conversion tasks on Linux hosts for CI or server automation.

## Inputs
- `MODEL`: Source model path.
- `OUT_DIR`: Output directory for converted artifacts.
- `TOOLCHAIN`: Optional conversion toolchain location.
- `PROFILE`: Optional conversion profile.

## Requirements
- Environment type: `host`
- Environment subtype: `linux`
- Runtime dependencies: `python>=3.10`, `bash`

## Workflow
1. Confirm host OS is Linux.
2. Validate source model path and output directory.
3. Execute conversion command sequence for the selected profile.
4. Capture logs and generated artifacts.
5. Return conversion status and follow-up actions.

## Output
- Conversion exit status.
- Paths to generated artifacts.
- Error summary and remediation hints if conversion fails.
