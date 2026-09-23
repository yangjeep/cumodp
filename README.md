# CUMODP / modpn

Historical CUDA/GPU research source recovered from my 2011–2012 M.Sc. work at the Ontario Research Centre for Computer Algebra (ORCCA), University of Western Ontario.

This repository preserves a surviving **Subversion r230 working copy** together with as much of its original development timeline as could be recovered from the remaining SVN metadata.

## What this work was about

The recovered code covers modular polynomial computation on GPUs, including:

- fast polynomial evaluation over finite fields
- GPU subproduct-tree construction
- polynomial division and remainder computation
- power-series inversion
- FFT-based polynomial arithmetic
- CUDA kernels, memory-management and performance work
- Maple-based correctness checks
- shell-based testing and benchmarking
- related legacy `modpn` sources

The source includes work from multiple ORCCA contributors. Original copyright, license and authorship notices have been preserved.

## My work in this snapshot

My SVN username was **`jyang425`**. The surviving metadata records **42 observable revision markers** attributed to that account between November 2011 and February 2012.

The recovered source also contains direct authorship evidence. For example:

`cumodp/include/subproduct_tree.h`

identifies:

`@author: Jiajian Yang`

The recovered development records and source cover my work around fast polynomial evaluation, subproduct-tree construction, polynomial division, power-series inversion, testing and benchmarking.

## Recovered SVN snapshot

The surviving working-copy metadata identifies the source as:

- SVN repository: `svn+ssh://jyang425@129.100.16.102/home/svn/modpn/modpn`
- repository UUID: `c22c0bd6-5691-0410-a3fe-d57a1563a474`
- working-copy revision: **r230**

The original `.svn/wc.db` records **354 versioned files** at r230. The recovered archive physically contained **229** of them. The other 125 files and the `.svn/pristine` bodies were no longer available.

No missing source files were synthesized from later versions.

## Recovered history

The reconstructed SVN timeline has been merged into `main`.

From the surviving working-copy metadata we recovered:

- **88** observable SVN last-change revision markers
- revision range **r2 → r230**
- original SVN author identifiers
- original SVN timestamps
- **42** revision markers attributed to `jyang425`
- all **229** recovered versioned files represented by the r230 point in the reconstructed history

This is a **partial metadata reconstruction**, not the original SVN diff history.

An SVN working copy at r230 records the last-changed revision for each path, but not every earlier version of that path. Therefore, each reconstructed revision introduces the recovered r230 bytes for files whose surviving metadata names that revision as their last change. When a referenced file was missing from the archive, the revision is retained as a metadata-only commit.

The reconstruction is intentionally explicit about this limitation in every reconstructed commit.

For the recovery details and reproducible tooling, see:

- [README_RECOVERY.md](README_RECOVERY.md)
- [recovered SVN node metadata](.svn-recovery/nodes.csv)
- [recovered revision timeline](.svn-recovery/revisions.csv)
- [history reconstruction script](.svn-recovery/reconstruct_history.py)

## Related CUMODP repository

A later public CUMODP codebase is available at:

**[davidtranhq/cumodp](https://github.com/davidtranhq/cumodp)**

That repository contains a later CUMODP release lineage; its README identifies **CUMODP 2.0, released 2017-05-30**. It is useful for comparing the later project state with this recovered 2011–2012 research snapshot.

This repository is not a fork of that GitHub repository. The source here was recovered independently from my old SVN working copy.

## Provenance

CUMODP/modpn was collaborative research software. This repository does **not** claim sole authorship of the full codebase.

Its purpose is to preserve the source, provenance, development metadata and research context that survived from my original working copy.
