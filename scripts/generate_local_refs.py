#!/usr/bin/env python3
"""Copy bounded shared references into skill directories that declare them."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "research" / "catalog.json"
SHARED = Path(__file__).resolve().parent / "shared-refs"

# Skills that may propose FN reads or writes. Parent educational skills stay local-only.
FN_SKILLS = {
    "factual-observation-notes",
    "progress-report-drafting",
    "learning-portfolios",
    "family-school-messages",
    "admissions-inquiry-replies",
    "family-onboarding",
    "school-calendar-planning",
    "school-announcements",
    "tuition-billing-explanations",
    "payment-record-reconciliation",
    "future-nerds",
}

RECORD_SKILLS = {
    "factual-observation-notes",
    "observation-to-lesson-plan",
    "progress-report-drafting",
    "learning-portfolios",
    "family-school-messages",
    "substitute-guide-handoff",
    "admissions-inquiry-replies",
    "family-onboarding",
    "school-announcements",
    "tuition-billing-explanations",
    "payment-record-reconciliation",
    "family-feedback-review",
    "future-nerds",
}


def copies_for(slug: str) -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    if slug in FN_SKILLS:
        mapping["integration.md"] = SHARED / "integration.md"
    if slug in RECORD_SKILLS:
        mapping["records.md"] = SHARED / "records.md"
    return mapping


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated copies drifted.")
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text())
    slugs = [s["slug"] for s in catalog["skills"]]
    errors: list[str] = []
    written = 0
    for slug in slugs:
        dest_dir = ROOT / "skills" / slug / "references"
        for name, src in copies_for(slug).items():
            dest = dest_dir / name
            if not src.exists():
                errors.append(f"missing source {src}")
                continue
            src_text = src.read_text()
            if args.check:
                if not dest.exists():
                    errors.append(f"missing copy {dest.relative_to(ROOT)}")
                elif dest.read_text() != src_text:
                    errors.append(f"drift {dest.relative_to(ROOT)}")
            else:
                dest_dir.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dest)
                written += 1
    if errors:
        print("generate_local_refs errors:")
        for e in errors:
            print(f"  {e}")
        return 1
    if args.check:
        print(f"generate_local_refs: {len(slugs)} skills, copies match shared sources")
    else:
        print(f"generate_local_refs: wrote {written} copies")
    return 0


if __name__ == "__main__":
    sys.exit(main())
