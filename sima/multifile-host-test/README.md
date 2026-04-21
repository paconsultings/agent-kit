# Multifile Host Test Skill

This directory intentionally contains multiple files so `sima-cli skills describe` can be validated against a realistic skill package.

Example local checks:

```bash
python3 scripts/check_env.py
python3 scripts/process_input.py --input /tmp/example.txt --workdir /tmp/multifile-test
```
