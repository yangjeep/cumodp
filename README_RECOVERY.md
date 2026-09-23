# CUMODP / modpn — recovered 2011–2012 working copy

This repository preserves a recovered working copy from my M.Sc. work at the Ontario Research Centre for Computer Algebra (ORCCA), University of Western Ontario.

The recovered Subversion metadata identifies the working copy as:

- SVN repository: `svn+ssh://jyang425@129.100.16.102/home/svn/modpn/modpn`
- Repository UUID: `c22c0bd6-5691-0410-a3fe-d57a1563a474`
- Working-copy revision: **r230**
- SVN username visible in the metadata: `jyang425`

The archive contains CUDA/GPU work around modular polynomial computation, including fast polynomial evaluation, subproduct-tree construction, polynomial division, power-series inversion, FFT-based polynomial arithmetic, tests/benchmarks, and related `modpn` material.

## Recovery notes

The uploaded archive retained `.svn/wc.db` but did **not** retain the `.svn/pristine` file bodies. The database records 354 versioned files at r230; 229 of those files are physically present in the recovered archive and 125 are missing from the working tree/archive.

The recovered snapshot on `main` preserves the files that were actually found. Missing versioned files have not been synthesized from later CUMODP mirrors.

The apparent checksum mismatch for `cumodp/tests/cumodp-create-test` is explained by its SVN special/symlink representation in the archived working copy rather than a known source edit.

See `.svn-recovery/nodes.csv` and `.svn-recovery/missing-versioned-files.txt` for the recovered SVN metadata.

## Partial SVN history reconstruction

The branch `svn-recovered-history` is a metadata-based reconstruction using the surviving `wc.db` information.

It contains:

- **88** observable file last-change SVN revision markers from **r2** to **r230**
- **42** revision markers attributed to `jyang425`
- original recorded SVN timestamps
- original SVN author identifiers in every commit message
- **229** recovered versioned files at the r230 branch tip

For authors whose historical email address is directly evidenced, the reconstruction maps the SVN username to the corresponding name/email. For `jyang425`, commits are authored as **Jiajian Yang <yangjeep@gmail.com>**. The Git committer is explicitly `SVN Metadata Reconstruction`.

### Important limitation

This branch is **not the original SVN diff history**.

A Subversion working-copy database at r230 records the last-changed revision of each path, not every earlier version of that path. Because the old repository and pristine bodies are unavailable, the reconstruction cannot know the contents of a file at intermediate revisions.

Accordingly, each reconstructed revision:

1. uses the real SVN revision number, author identifier, and timestamp from `wc.db`;
2. introduces only recovered paths whose r230 metadata says that revision was their last change;
3. uses the recovered r230 file bytes for those paths;
4. creates an empty metadata commit when all paths associated with an observed revision are missing from the archive;
5. states these limitations directly in the commit message.

The process is reproducible from:

- `.svn-recovery/nodes.csv`
- `.svn-recovery/revisions.csv`
- `.svn-recovery/reconstruct_history.py`

## Authorship / provenance

CUMODP/modpn was collaborative research software. Original copyright and license notices in source files are preserved. Individual files may identify their authors; for example, the recovered `cumodp/include/subproduct_tree.h` identifies **Jiajian Yang** as author for that component.

This repository does not claim sole authorship of the full CUMODP codebase.
