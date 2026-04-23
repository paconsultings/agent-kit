# paconsultings/skills

Test repository for `sima-cli agent-kit` installation from GitHub sources.

## Layout
- `skills/`: reusable skill artifacts (`SKILL.md` + `playbook.yaml`)
- `rules/`: repository guideline artifacts (`AGENTS.md` + `playbook.yaml`)

## Example artifacts
- Skill: `skills/sima/onnx-afe-pipeline`
- Rule: `rules/sima/default-coding-rule`

## Install examples
- Install a skill:
  - `sima-cli playbooks install gh:paconsultings/skills/skills/sima/onnx-afe-pipeline`
- Install a rule package (for future `apply` flow):
  - `sima-cli playbooks install gh:paconsultings/skills/rules/sima/default-coding-rule`

## Rename recommendation
When feasible, rename this repository to `paconsultings/agent-kit` to better match the command surface and mixed artifact types.
