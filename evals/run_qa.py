#!/usr/bin/env python3
"""Run the additional deterministic QA regression suite."""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "scripts"))
from validate_output import check  # noqa: E402


def main() -> int:
    cfg = json.loads((HERE / "qa_cases.json").read_text(encoding="utf-8"))
    original = json.loads((HERE / "evals.json").read_text(encoding="utf-8"))
    cases = list(cfg["cases"])
    for case in original["cases"]:
        cases.append({
            "name": "original/" + case["name"],
            "lang": case["lang"],
            "input": case["input"],
            "output": case["output"],
        })
    ok = True
    for case in cases:
        result = check(case["input"], case["output"], case["lang"], case.get("preserve", []))
        passed = all(result.values())
        ok = ok and passed
        print(f"\n=== {case['name']} (lang={case['lang']}) ===")
        for name, value in result.items():
            print(f"  [{'PASS' if value else 'FAIL'}] {name}")
    print("\n" + ("ALL QA ASSERTIONS PASS" if ok else "SOME QA ASSERTIONS FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
