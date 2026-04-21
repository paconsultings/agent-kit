---
name: onnx-afe-pipeline
description: Validate ONNX AFE models, run conversion and compile steps, and summarize deployable outputs.
user-invocable: true
argument-hint: "[MODEL=<path>] [WORKDIR=<path>] [TARGET=<modalix|davinci>] [CONFIG=<path>]"
---

# ONNX AFE Pipeline

Build and validate an ONNX AFE pipeline for SiMa tooling.

## Inputs
- `MODEL`: Path to the ONNX model file.
- `WORKDIR`: Working directory for intermediate and final artifacts.
- `TARGET`: Deployment target profile such as `modalix` or `davinci`.
- `CONFIG`: Optional pipeline configuration file.

## Requirements
- Environment type: `host` (`mac` or `linux`)
- Runtime dependencies: `python>=3.10`, `onnx`, `onnxruntime`
- Optional: `docker`

## Workflow
1. Validate ONNX model integrity and expected I/O signatures.
2. Run conversion steps for the requested target profile.
3. Execute compile and packaging commands.
4. Collect generated artifacts and logs in `WORKDIR`.
5. Summarize artifact readiness for deployment.

## Output
- Validation status with key model checks.
- Conversion and compile command results.
- Artifact inventory with paths and file sizes.
- Final deployment-readiness summary.
