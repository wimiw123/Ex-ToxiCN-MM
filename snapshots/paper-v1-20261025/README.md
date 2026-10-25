# Ex-ToxiCN-MM data snapshot: paper-v1-20261025

This is the text/annotation snapshot corresponding to Section III-D of *Distinguishing Right from Wrong in Relativity: Attribution Analysis of Chinese Harmful Memes*. It replaces the earlier 7,042-sample release as the data reference for this manuscript version. Earlier root-level files are legacy artifacts and must not be mixed with this version.

| Artifact | Count |
| --- | ---: |
| Training memes | 9,595 |
| Test memes | 2,400 |
| Total memes | 11,995 |
| Harmful / non-harmful | 3,815 / 8,180 |
| Paired relative-intent explanations | 23,990 |
| Mean explanation length (characters) | 60.274239 |
| Population standard deviation | 27.836951 |
| Clean C-HarmKB entries | 23,409 |

Length counts Python Unicode code points after trimming outer whitespace, over both `intent_harm` and `intent_noharm`. The rounded mean and standard deviation are 60.27 and 27.84. Statistics are derived from released data, not copied from the old README. `scripts/validate_snapshot.py` recomputes them and checks the fixed, disjoint image-ID splits.

## Files and schema

- `data/train.json`, `data/test.json`: fixed original split order, one row per meme; no new random split.
- `splits/train_ids.json`, `splits/test_ids.json`: exact image filenames in each split.
- `C-HarmKB.jsonl`: 23,409 cleaned semantic entries. Its `source_split` retains available split provenance; this is not a claim that every entry was constructed from training data alone.
- `runtime/V6-rule-KB.jsonl`: the separate 26,447-entry runtime rule dictionary used by the archived winning classifier. **It contains 257 test-error-mined rules and is diagnostic/transductive, not a strict train-only knowledge base.** It is included as a model input artifact needed to identify the historical configuration; it is not the 23,409-entry C-HarmKB statistic.
- `dataset_metadata.json`: versioned counts and definitions.
- `SHA256SUMS`: hashes of all snapshot files except itself.

Annotation fields: `path` (image filename only), `text`, `meme_discription`, `label` (1 harmful, 0 non-harmful), `type`, `text_modal`, `image_modal`, `target`, `intent_harm`, `intent_noharm`, `bk`, `use_bk`, and `final_explanation`. The source spelling `meme_discription` is preserved. `text_discription` preserves the processed archive's additional textual semantic description, required by the full historical classifier. It is an annotation input, not newly generated text. `bk` retains only knowledge identifiers, terms, meanings and relations.

Annotator-group metadata, cleanup bookkeeping, hierarchical derived fields, server paths, source-machine filenames and sample-level KB provenance were excluded. Dataset annotation targets are retained; model predictions and experiment outputs are not distributed.

## Images

The supplied archive contains no image files. The earlier repository links to [the image asset record](https://doi.org/10.5281/zenodo.18229215). This snapshot does not assert that that earlier image archive covers all 11,995 filenames; check coverage against the released split IDs. Multimodal reproduction requires the corresponding original images. No substitute images were created.

## Code and manuscript correspondence

Use the matching [RIKE paper snapshot](https://github.com/wimiw123/RIKE/tree/main/snapshots/paper-v1-20261025). It includes Direct SFT LoRA training, the Qwen3-4B selector training data and configuration, two-index lexical retrieval with RRF and companion rules, and the full RIR inference prompt without a risk gate. The root RIKE prototype's dense Chroma/reranker pipeline belongs to an older implementation.

This data revision resolves the previous README's version mismatch in dataset counts. It does not by itself establish strict held-out validity of the historical V6 experiment, reconcile every Table II ablation number, or verify the independent explanation-generation evaluation in Table III. See the code snapshot's explicit reproduction-status notes. Cite both exact Git commit SHAs, not only the mutable default branches.

## License and content

The dataset remains under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), as stated in the original release. It contains offensive and harmful language for research on detection and interpretation; dataset content does not express the authors' views. Refer to the manuscript for annotation and ethical procedures.
