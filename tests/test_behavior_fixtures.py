#!/usr/bin/env python3
"""Load behavior fixtures and check they are well-formed.

This is a static fixture test. It does not run a model. Cases in
tests/fixtures/behavior_cases.json remain unevaluated as agent behavior.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT / "tests" / "fixtures" / "behavior_cases.json").read_text())
CATALOG = json.loads((ROOT / "research" / "catalog.json").read_text())
SLUGS = {s["slug"] for s in CATALOG["skills"]}


class BehaviorFixtureShape(unittest.TestCase):
    def test_not_marked_as_model_run(self):
        self.assertFalse(CASES["model_evaluations_run"])
        self.assertEqual(CASES["kind"], "static-behavior-fixtures")

    def test_trigger_skills_exist(self):
        for row in CASES["trigger_routing"]:
            if row["expect_skill"]:
                self.assertIn(row["expect_skill"], SLUGS, row["id"])
            if row.get("reject_skill"):
                self.assertIn(row["reject_skill"], SLUGS, row["id"])
                self.assertNotEqual(row.get("expect_skill"), row["reject_skill"])

    def test_fn_cases_cover_required_risks(self):
        ids = {r["id"] for r in CASES["fn"]}
        for needed in {
            "wrong-school",
            "absent-role",
            "duplicate-names",
            "no-leak",
            "unapproved-notification",
            "retry-duplicate",
            "financial-mutation",
        }:
            self.assertIn(needed, ids)

    def test_financial_math(self):
        for row in CASES["financial_arithmetic"]:
            total = sum(x["quantity"] * x["unit_price"] for x in row["invoice_lines"])
            self.assertAlmostEqual(total, row["expect_remaining"], places=2, msg=row["id"])

    def test_safety_skills_mention_overrides(self):
        text = (ROOT / "skills" / "montessori-family-routines" / "SKILL.md").read_text().lower()
        self.assertIn("spoiled food", text)
        grace = (ROOT / "skills" / "grace-and-courtesy" / "SKILL.md").read_text()
        self.assertIn("eye contact", grace.lower())
        home = (ROOT / "skills" / "prepared-home-environment" / "SKILL.md").read_text()
        self.assertIn("Anchor", home)


if __name__ == "__main__":
    unittest.main()
