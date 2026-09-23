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

No synthetic SVN-to-Git history has been created. This Git repository is a preservation snapshot of the files that were actually recovered.

One present file differs from the r230 checksum recorded in `wc.db`:

- `cumodp/tests/cumodp-create-test`

See `.svn-recovery/nodes.csv` and `.svn-recovery/missing-versioned-files.txt` for the recovered SVN metadata.

## Authorship / provenance

CUMODP/modpn was collaborative research software. Original copyright and license notices in source files are preserved. Individual files may identify their authors; for example, the recovered `cumodp/include/subproduct_tree.h` identifies **Jiajian Yang** as author for that component.

This repository does not claim sole authorship of the full CUMODP codebase.
