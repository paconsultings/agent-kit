#!/usr/bin/env python3
import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Process a text input for multifile-host-test")
    parser.add_argument("--input", required=False, help="Optional input file path")
    parser.add_argument("--workdir", required=False, default=".", help="Output working directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    workdir = Path(args.workdir).expanduser().resolve()
    workdir.mkdir(parents=True, exist_ok=True)

    if args.input:
        input_path = Path(args.input).expanduser().resolve()
        content = input_path.read_text(encoding="utf-8") if input_path.exists() else ""
        summary = f"input={input_path}\nchars={len(content)}\n"
    else:
        summary = "input=<none>\nchars=0\n"

    output_path = workdir / "summary.txt"
    output_path.write_text(summary, encoding="utf-8")
    print(str(output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
