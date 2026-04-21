---
name: devkit-deploy
description: Deploy build artifacts to SiMa DevKit targets (Modalix/DaVinci) using SSH and rsync.
argument-hint: [TARGET=<hostname_or_ip>] [ARTIFACT_DIR=<path>] [DEST_PATH=<path>]
---

# Devkit Deploy

Deploy artifacts from a host machine to a SiMa DevKit device.

## Inputs
- `TARGET`: DevKit hostname or IP address.
- `ARTIFACT_DIR`: Local directory containing deployable artifacts.
- `DEST_PATH`: Destination path on the DevKit.

## Requirements
- Environment type: `devkit`
- Environment subtype: `modalix` or `davinci`
- Tools: `ssh`, `rsync`

## Workflow
1. Verify connectivity to `TARGET` over SSH.
2. Validate that `ARTIFACT_DIR` exists and is readable.
3. Create `DEST_PATH` on the target if needed.
4. Sync artifacts with `rsync` and preserve permissions.
5. Report transferred files and any skipped/failed items.

## Output
- Deployment summary with target host and source/destination paths.
- Transferred file count.
- Failures and suggested retries.
