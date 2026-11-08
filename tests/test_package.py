#!/usr/bin/env python3
"""Unittest wrapper around scripts/validate.py and generate_local_refs --check."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PackageStaticChecks(unittest.TestCase):
    def test_generate_local_refs_drift(self):
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "generate_local_refs.py"), "--check"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_validate_script(self):
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate.py")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
