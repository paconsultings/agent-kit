#!/usr/bin/env python3
import platform
import sys


def main() -> int:
    print("multifile-host-test: environment check")
    print(f"python: {sys.version.split()[0]}")
    print(f"platform: {platform.system().lower()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
