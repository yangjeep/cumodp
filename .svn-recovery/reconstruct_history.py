#!/usr/bin/env python3
"""Reconstruct a partial Git history from an SVN 1.8+ wc.db metadata export.

This does NOT claim to recreate historical SVN file contents. Each recovered file is
introduced at the SVN revision recorded as its last-changed revision in the recovered
r230 working copy, using that file's r230 bytes. Revisions whose referenced files are
missing are represented by empty commits.
"""

from __future__ import annotations

import csv
import os
import shutil
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path

BRANCH = os.environ.get("RECOVERED_BRANCH", "svn-recovered-history")
NODES = Path(".svn-recovery/nodes.csv")
REVISIONS = Path(".svn-recovery/revisions.csv")

AUTHOR_MAP = {
    "jyang425": ("Jiajian Yang", "yangjeep@gmail.com"),
    "moreno": ("Marc Moreno Maza", "moreno@csd.uwo.ca"),
    "shaque4": ("Sardar Anisul Haque", "shaque4@uwo.ca"),
    "panwei": ("Wei Pan", "panwei@svn.invalid"),
}

def run(*args: str, env=None) -> None:
    subprocess.run(args, check=True, env=env)

def copy_entry(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_symlink():
        if dst.exists() or dst.is_symlink():
            dst.unlink()
        dst.symlink_to(os.readlink(src))
    else:
        shutil.copy2(src, dst)

def main() -> None:
    repo = Path.cwd()
    if not NODES.exists() or not REVISIONS.exists():
        raise SystemExit("Run from repository root with .svn-recovery metadata present")

    with NODES.open(newline="", encoding="utf-8") as f:
        node_rows = list(csv.DictReader(f))
    with REVISIONS.open(newline="", encoding="utf-8") as f:
        revision_rows = list(csv.DictReader(f))

    by_rev = defaultdict(list)
    for row in node_rows:
        try:
            rev = int(row["last_changed_revision"])
        except (ValueError, TypeError):
            continue
        by_rev[rev].append(row)

    tmp = Path(tempfile.mkdtemp(prefix="cumodp-svn-recovery-"))
    snapshot = tmp / "snapshot"
    snapshot.mkdir()
    present_paths = set()
    for row in node_rows:
        if row.get("present_in_archive") != "yes":
            continue
        rel = row["path"]
        src = repo / rel
        if not (src.exists() or src.is_symlink()):
            continue
        copy_entry(src, snapshot / rel)
        present_paths.add(rel)

    run("git", "checkout", "--orphan", BRANCH)
    run("git", "rm", "-rf", ".")
    run("git", "clean", "-fdx")

    for rev_row in revision_rows:
        rev = int(rev_row["revision"])
        author_id = rev_row["author"]
        timestamp = rev_row["changed_at_utc"]
        all_rows = by_rev.get(rev, [])
        recovered = [r for r in all_rows if r["path"] in present_paths]
        missing = [r for r in all_rows if r["path"] not in present_paths]

        for row in recovered:
            copy_entry(snapshot / row["path"], repo / row["path"])

        if recovered:
            run("git", "add", "--", *[r["path"] for r in recovered])

        name, email = AUTHOR_MAP.get(author_id, (author_id, f"{author_id}@svn.invalid"))
        lines = [
            f"SVN r{rev} — partial metadata reconstruction",
            "",
            f"Original SVN author: {author_id}",
            f"Original SVN timestamp: {timestamp}",
            f"Recovered files introduced: {len(recovered)}",
            f"Referenced files missing from recovered snapshot: {len(missing)}",
            "",
            "This commit is reconstructed from SVN wc.db metadata. File contents are",
            "the recovered r230 working-copy bytes for files whose last-changed revision",
            f"is r{rev}; intermediate historical contents and diffs are unavailable.",
        ]
        if recovered:
            lines += ["", "Recovered paths:"] + [f"- {r['path']}" for r in recovered]
        if missing:
            lines += ["", "Missing paths recorded for this revision:"] + [f"- {r['path']}" for r in missing]
        message = "\n".join(lines)

        env = os.environ.copy()
        env.update({
            "GIT_AUTHOR_NAME": name,
            "GIT_AUTHOR_EMAIL": email,
            "GIT_AUTHOR_DATE": timestamp,
            "GIT_COMMITTER_NAME": "SVN Metadata Reconstruction",
            "GIT_COMMITTER_EMAIL": "svn-reconstruction@invalid",
            "GIT_COMMITTER_DATE": timestamp,
        })
        run("git", "commit", "--allow-empty", "-m", message, env=env)

    run("git", "push", "--force", "origin", f"HEAD:refs/heads/{BRANCH}")
    print(f"Reconstructed {len(revision_rows)} SVN revision markers on {BRANCH}")
    print(f"Recovered versioned files at branch tip: {len(present_paths)}")

if __name__ == "__main__":
    main()
