#!/usr/bin/env python3
"""Static validation for the 33-skill package. Not a runtime or model evaluation."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "research" / "catalog.json").read_text())
SLUGS = [s["slug"] for s in CATALOG["skills"]]
BANNED = [
    "\u2014",  # em dash
    "delve",
    "unpack",
    "leverage",
    "utilize",
    "game-changer",
    "cutting-edge",
    "seamless",
    "holistic",
    "empower",
    "supercharge",
]
PRIVATE_MARKERS = [
    "private-reading",
    "BEGIN PRIVATE KEY",
    "sk-ant-",
    "SUPABASE_SERVICE_ROLE",
    "eyJhbGciOi",  # likely JWT
]


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)


def load_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unclosed frontmatter")
    data = yaml.safe_load(text[4:end])
    if not isinstance(data, dict):
        raise ValueError("frontmatter not a mapping")
    return data


def test_catalog_counts(errors: list[str]) -> None:
    if len(SLUGS) != 33 or len(set(SLUGS)) != 33:
        fail(f"catalog slug count {len(SLUGS)} unique {len(set(SLUGS))}", errors)
    from collections import Counter

    c = Counter(s["audience"] for s in CATALOG["skills"])
    expected = {"Parents": 10, "Guides": 12, "Admin": 10, "Integration": 1}
    if dict(c) != expected:
        fail(f"audience counts {dict(c)} != {expected}", errors)


def test_skill_files(errors: list[str]) -> None:
    skill_dirs = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())
    if skill_dirs != sorted(SLUGS):
        fail(f"skills/ dirs {skill_dirs} != catalog", errors)
    catalog_desc = {s["slug"]: s["description"] for s in CATALOG["skills"]}
    name_re = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    for slug in SLUGS:
        path = ROOT / "skills" / slug / "SKILL.md"
        if not path.exists():
            fail(f"missing {path}", errors)
            continue
        text = path.read_text()
        try:
            fm = load_frontmatter(text)
        except Exception as e:
            fail(f"{slug} frontmatter: {e}", errors)
            continue
        if fm.get("name") != slug:
            fail(f"{slug} name {fm.get('name')!r}", errors)
        desc = fm.get("description") or ""
        if not (1 <= len(desc) <= 1024):
            fail(f"{slug} description length {len(desc)}", errors)
        if desc != catalog_desc[slug]:
            fail(f"{slug} description differs from research/catalog.json", errors)
        if text.count("\n") + 1 > 500:
            fail(f"{slug} SKILL.md exceeds 500 lines", errors)
        if not name_re.match(slug) or len(slug) > 64:
            fail(f"{slug} name pattern", errors)
        meta = fm.get("metadata") or {}
        if meta and any(not isinstance(v, str) for v in meta.values()):
            fail(f"{slug} metadata values must be strings", errors)
        if "../" in text:
            fail(f"{slug} SKILL.md escapes with ../", errors)
        ev = ROOT / "skills" / slug / "references" / "evidence.md"
        if not ev.exists():
            fail(f"{slug} missing evidence.md", errors)
        for ref in ("integration.md", "records.md"):
            if f"references/{ref}" in text and not (ROOT / "skills" / slug / "references" / ref).exists():
                fail(f"{slug} references {ref} but copy missing", errors)


def test_readme(errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text()
    for s in CATALOG["skills"]:
        slug = s["slug"]
        if f"](skills/{slug}/)" not in readme and f"](skills/{slug}/SKILL.md)" not in readme:
            fail(f"README missing link for {slug}", errors)
        if s["purpose"] not in readme:
            fail(f"README missing purpose for {slug}", errors)
        if s["example_prompt"] not in readme:
            fail(f"README missing example for {slug}", errors)


def test_relative_links(errors: list[str]) -> None:
    link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for md in (ROOT / "skills").rglob("*.md"):
        rel_root = md.parent
        text = md.read_text()
        for url in link_re.findall(text):
            if url.startswith(("http://", "https://", "mailto:")):
                continue
            if url.startswith("#"):
                continue
            if url.startswith("../") or url.startswith("/"):
                fail(f"{md.relative_to(ROOT)} outbound path {url}", errors)
                continue
            target = (rel_root / url.split("#")[0]).resolve()
            try:
                target.relative_to((md.parents[1] if md.name != "SKILL.md" else md.parent).resolve())
            except ValueError:
                # For files in references/, skill root is parents[1]
                pass
            skill_root = md.parents[0] if md.name == "SKILL.md" else md.parents[1]
            try:
                target.relative_to(skill_root.resolve())
            except ValueError:
                fail(f"{md.relative_to(ROOT)} link leaves skill: {url}", errors)
                continue
            if not target.exists():
                fail(f"{md.relative_to(ROOT)} broken relative {url}", errors)


def test_plugin_schema(errors: list[str]) -> None:
    import jsonschema

    schema = json.loads((ROOT / "tests" / "fixtures" / "plugin.schema.json").read_text())
    plugin = json.loads((ROOT / "plugin.json").read_text())
    try:
        jsonschema.validate(plugin, schema)
    except Exception as e:
        fail(f"portable plugin.json: {e}", errors)
    if plugin.get("license"):
        fail("license present without authorization", errors)
    claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    if claude.get("name") != "montessori-skills":
        fail("claude plugin name", errors)
    if "license" in claude:
        fail("claude license present without authorization", errors)
    if "mcpServers" in claude or (ROOT / "mcp.json").exists() or (ROOT / ".mcp.json").exists():
        fail("unexpected MCP config", errors)


def test_banned_and_private(errors: list[str]) -> None:
    for path in list((ROOT / "skills").rglob("*.md")) + [ROOT / "README.md"]:
        text = path.read_text()
        lower = text.lower()
        for b in BANNED:
            if b.lower() in lower:
                fail(f"{path.relative_to(ROOT)} contains {b!r}", errors)
        for m in PRIVATE_MARKERS:
            if m in text:
                fail(f"{path.relative_to(ROOT)} private marker {m}", errors)


def test_standalone_copy(errors: list[str]) -> None:
    src = ROOT / "skills" / "montessori-at-home"
    with tempfile.TemporaryDirectory() as td:
        dest = Path(td) / "montessori-at-home"
        shutil.copytree(src, dest)
        skill = dest / "SKILL.md"
        text = skill.read_text()
        if "../" in text:
            fail("standalone copy still has ../", errors)
        for url in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if url.startswith(("http://", "https://", "#")):
                continue
            target = (dest / url.split("#")[0]).resolve()
            if not target.exists():
                fail(f"standalone broken {url}", errors)


def test_overlap_disambiguation(errors: list[str]) -> None:
    pairs = [
        ("family-school-messages", "school-announcements"),
        ("factual-observation-notes", "progress-report-drafting"),
        ("observation-to-lesson-plan", "montessori-lesson-preparation"),
        ("tuition-billing-explanations", "payment-record-reconciliation"),
    ]
    descs = {s["slug"]: s["description"] for s in CATALOG["skills"]}
    for a, b in pairs:
        if b not in descs[a]:
            fail(f"{a} description should mention {b}", errors)
        if a not in descs[b]:
            fail(f"{b} description should mention {a}", errors)


def test_agentskills_cli(errors: list[str]) -> None:
    exe = shutil.which("agentskills") or str(Path.home() / ".local/bin/agentskills")
    if not Path(exe).exists():
        fail("agentskills CLI not installed", errors)
        return
    for slug in SLUGS:
        r = subprocess.run(
            [exe, "validate", str(ROOT / "skills" / slug)],
            capture_output=True,
            text=True,
        )
        if r.returncode != 0:
            fail(f"agentskills validate {slug}: {r.stdout} {r.stderr}", errors)


def main() -> int:
    errors: list[str] = []
    test_catalog_counts(errors)
    test_skill_files(errors)
    test_readme(errors)
    test_relative_links(errors)
    test_plugin_schema(errors)
    test_banned_and_private(errors)
    test_standalone_copy(errors)
    test_overlap_disambiguation(errors)
    test_agentskills_cli(errors)
    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print(f"PASS static validation: {len(SLUGS)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
