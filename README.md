# Ex-ToxiCN-MM: Explainable Chinese Harmful Memes

The current manuscript, *Distinguishing Right from Wrong in Relativity: Attribution Analysis of Chinese Harmful Memes*, uses the versioned **[paper-v1-20261025 data snapshot](snapshots/paper-v1-20261025/README.md)**.

| Item | Current snapshot |
| --- | ---: |
| Memes | 11,995 |
| Training / test | 9,595 / 2,400 |
| Harmful / non-harmful | 3,815 / 8,180 |
| Paired interpretation texts | 23,990 |
| Mean interpretation length | 60.27 characters |
| Population standard deviation | 27.84 characters |
| Clean C-HarmKB entries | 23,409 |

These counts were recomputed from the released annotations. The snapshot includes fixed split IDs, metadata, an executable validation script and SHA-256 checksums. The matching **[RIKE source snapshot](https://github.com/wimiw123/RIKE/tree/main/snapshots/paper-v1-20261025)** contains the archived winning classification configuration and its training/retrieval entry points.

## Version clarification

The previous README described an earlier release: 7,042 memes, 14,084 explanations, 2,870 KB entries and a stated average explanation length of 33.29 characters. Those statements described the earlier public version and must not be used as statistics for the current manuscript. The older root-level `dataset_with_explanations_harm.json`, `dataset_with_explanations_noharm.json` and `C-harmKB.json` remain **legacy** files. Use the snapshot's `data/train.json`, `data/test.json` and `C-HarmKB.jsonl` for this revision.

The clean 23,409-entry KB is distinct from the archived classifier's **26,447-entry V6 runtime rule KB**, distributed separately inside the snapshot. **That runtime KB includes 257 rules mined from test errors, so the historical configuration is diagnostic/transductive rather than a strict train-only held-out evaluation.** The code snapshot documents this limitation, the additional semantic-description input, unresolved ablation correspondence and missing verification for Table III. Updating public files alone does not resolve those methodological questions.

## Images and usage

The supplied archive contains text and image filenames, not image binaries. The earlier release references [the image asset record](https://doi.org/10.5281/zenodo.18229215); coverage of this version's filenames must be verified separately. The snapshot does not claim a complete image redistribution. Read its README for field definitions and reproducibility requirements.

The dataset contains offensive and harmful language for academic research on recognition and interpretation. Dataset content does not express the authors' views. The data retain the original [CC BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/). See the manuscript for annotation procedures and ethical considerations.
