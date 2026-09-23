# CUMODP / modpn — recovered SVN r230 snapshot

This repository preserves source recovered from my 2011–2012 M.Sc. work at the Ontario Research Centre for Computer Algebra (ORCCA), University of Western Ontario.

The surviving Subversion working-copy metadata identifies the snapshot as **r230** from:

`svn+ssh://jyang425@129.100.16.102/home/svn/modpn/modpn`

The archive includes CUDA/GPU work around modular polynomial computation: fast polynomial evaluation, subproduct-tree construction, polynomial division, power-series inversion, FFT-based arithmetic, tests/benchmarks, legacy modpn sources, and project slides.

The original `.svn/wc.db` records 354 versioned files. The recovered archive physically contained 229 of them; 125 versioned files were absent and the `.svn/pristine` bodies were not preserved.

## Recovered history

The branch [`svn-recovered-history`](../../tree/svn-recovered-history) reconstructs the surviving SVN timeline as far as the working-copy metadata allows:

- 88 observable SVN last-change revision markers, from **r2** through **r230**
- 42 revision markers attributed to SVN user **`jyang425`**
- original SVN author identifiers and timestamps preserved
- 229 recovered versioned files represented at the branch tip

This is intentionally a **partial metadata reconstruction**, not a claim to have recovered the original SVN diffs. For each file, `wc.db` preserves only its last-changed revision in the r230 working copy. The reconstructed commit at that revision therefore introduces the recovered r230 bytes for that file. Missing files are recorded in commit messages but are not fabricated.

See [README_RECOVERY.md](README_RECOVERY.md), [the recovered SVN node metadata](.svn-recovery/nodes.csv), and [the recovered revision timeline](.svn-recovery/revisions.csv) for details.

CUMODP/modpn was collaborative research software. Original copyright, license, and authorship notices in the recovered files are preserved.
