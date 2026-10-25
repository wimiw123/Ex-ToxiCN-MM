# Ex-ToxiCN-MM data guide

Ex-ToxiCN-MM is an explainable Chinese harmful meme dataset introduced in *Distinguishing Right from Wrong in Relativity: Attribution Analysis of Chinese Harmful Memes*. It provides paired harmful and non-harmful interpretations for each meme and supports harmfulness classification, explanation generation, and culturally grounded attribution analysis.

## Statistics

| Item | Count |
| --- | ---: |
| Total memes | 11,995 |
| Training / test samples | 9,595 / 2,400 |
| Harmful / non-harmful memes | 3,815 / 8,180 |
| Interpretation texts | 23,990 |
| Mean interpretation length | 60.27 characters |
| Standard deviation | 27.84 characters |
| C-HarmKB contextual entries | 23,409 |
| Distinct knowledge terms | 19,430 |

## Files

| Path | Purpose |
| --- | --- |
| `data/train.json` | Training annotations |
| `data/test.json` | Test annotations |
| `splits/train_ids.json` | Training image filenames |
| `splits/test_ids.json` | Test image filenames |
| `C-HarmKB.jsonl` | Chinese contextual knowledge |
| `runtime/V6-rule-KB.jsonl` | Runtime knowledge dictionary consumed by the RIKE implementation |
| `dataset_metadata.json` | Dataset statistics |
| `scripts/validate_snapshot.py` | Data and file-integrity validation |
| `SHA256SUMS` | File checksums |

## Schema

Each JSON file contains a list of meme annotations. `label` is 1 for harmful and 0 for non-harmful. Image references use filenames in `path`.

| Fields | Contents |
| --- | --- |
| `text`, `meme_discription`, `text_discription` | Meme text, image description, and textual semantic description |
| `intent_harm`, `intent_noharm` | Paired interpretations under harmful and benign intent hypotheses |
| `bk` | Knowledge objects with `kid`, `term`, `meaning`, and `rel` where available |
| `use_bk` | Knowledge identifiers used in the explanation |
| `final_explanation` | Explanation for the classification decision |
| `type`, `text_modal`, `image_modal`, `target` | Category, modality, and target annotations |

The field spellings `meme_discription` and `text_discription` are used by the accompanying scripts. C-HarmKB is stored as JSON Lines, with one contextual knowledge entry per line.

## Loading the data

```python
import json
from pathlib import Path

root = Path(".")  # this directory
train = json.loads((root / "data/train.json").read_text(encoding="utf-8"))
test = json.loads((root / "data/test.json").read_text(encoding="utf-8"))
with (root / "C-HarmKB.jsonl").open(encoding="utf-8") as stream:
    knowledge = [json.loads(line) for line in stream if line.strip()]
```

Validate statistics, paired explanations, split membership, and checksums with:

```bash
python scripts/validate_snapshot.py
```

Explanation length is measured over both interpretation fields after trimming surrounding whitespace, using Unicode character counts.

## Images and RIKE

Download image assets from [the dataset image record](https://doi.org/10.5281/zenodo.18229215) and match them against the split filenames. Image binaries are distributed separately from these JSON annotations.

The [RIKE implementation guide](https://github.com/wimiw123/RIKE/tree/main/snapshots/paper-v1-20261025) explains data staging, LoRA training, knowledge retrieval, evidence selection, and inference. In that implementation, place images at `dataset/ex-toxcicn-mm/meme/<filename>`.

## License

The data are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). They contain offensive and harmful expressions intended for academic study of detection and explanation. The paper describes the annotation and review procedures.
