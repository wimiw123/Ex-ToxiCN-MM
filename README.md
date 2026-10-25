# Ex-ToxiCN-MM: Explainable Chinese Harmful Memes

This repository provides **Ex-ToxiCN-MM** and **C-HarmKB**, introduced in *Relative Intent Reasoning for Attribution Analysis of Chinese Harmful Memes*.

Ex-ToxiCN-MM supports harmful meme detection and attribution analysis in Chinese. Each meme is paired with a harmful interpretation and a non-harmful interpretation, allowing models to compare competing readings of the same image-text context. C-HarmKB supplies cultural and semantic knowledge for interpreting Chinese slang, implicit references, and context-dependent expressions.

The accompanying **[RIKE framework](https://github.com/wimiw123/RIKE)** combines Attribution Knowledge Enhancement (AKE) with Relative Intent Reasoning (RIR).

## Dataset statistics

Ex-ToxiCN-MM extends the 12,000-sample ToxiCN-MM corpus and contains 11,995 memes after cleaning.

| Item | Count |
| --- | ---: |
| Memes | 11,995 |
| Training samples | 9,595 |
| Test samples | 2,400 |
| Harmful memes | 3,815 |
| Non-harmful memes | 8,180 |
| Paired interpretation texts | 23,990 |
| Mean interpretation length | 60.27 characters |
| Standard deviation of interpretation length | 27.84 characters |
| C-HarmKB contextual entries | 23,409 |
| Distinct C-HarmKB terms | 19,430 |

## Paired relative-intent annotations

Each meme has two complementary explanations:

- **Harmful interpretation:** identifies a plausible harmful intent and explains the relevant target, semantic cues, cultural knowledge, and image-text relationship.
- **Non-harmful interpretation:** develops a plausible benign reading, such as humor, self-deprecation, a literal interpretation, or everyday commentary.

The annotation process combines LLM-assisted drafts with human editing, cross-review, and adjudication. Explanations are assessed for informativeness, soundness, cultural relevance, conciseness, and persuasiveness.

## C-HarmKB

C-HarmKB contains contextual meanings and relations for Chinese online expressions. Its construction combines an existing Chinese insult lexicon, encyclopedic and subculture sources, automatic candidate discovery, and expert verification. Knowledge entries support context-aware retrieval and evidence-grounded meme interpretation.

## Repository files

| File | Contents |
| --- | --- |
| [dataset_with_explanations_harm.json](dataset_with_explanations_harm.json) | 3,815 harmful memes with paired interpretations |
| [dataset_with_explanations_noharm.json](dataset_with_explanations_noharm.json) | 8,180 non-harmful memes with paired interpretations |
| [C-harmKB.json](C-harmKB.json) | 23,409 contextual knowledge entries under the `terms` key |

Both annotation files contain samples from the training and test sets. Each sample's `split` field identifies its partition (`train` or `test`), and `split_index` records its zero-based position within that partition. Combine the two files, filter by `split`, and sort by `split_index` to recover the 9,595 training and 2,400 test samples in their original order.

For image assets, see [the dataset image record](https://doi.org/10.5281/zenodo.18229215). The JSON annotations identify images by filename; prepare the corresponding image files for multimodal experiments.

## Annotation fields

| Field | Meaning |
| --- | --- |
| `path` | Image filename |
| `text` | Meme text |
| `meme_discription` | Image description |
| `text_discription` | Textual semantic description |
| `label` | Harmfulness label: 1 harmful, 0 non-harmful |
| `split`, `split_index` | Train/test partition and position within that partition |
| `intent_harm` | Harmful interpretation |
| `intent_noharm` | Non-harmful interpretation |
| `bk` | Annotated background knowledge |
| `use_bk` | References to background knowledge used in the explanation |
| `final_explanation` | Decision explanation |

Additional category, modality, and target annotations are available in `type`, `text_modal`, `image_modal`, and `target`. The field spellings `meme_discription` and `text_discription` are used by the accompanying code.

## Loading the data

```python
import json
from pathlib import Path

root = Path(".")
harmful = json.loads((root / "dataset_with_explanations_harm.json").read_text(encoding="utf-8"))
benign = json.loads((root / "dataset_with_explanations_noharm.json").read_text(encoding="utf-8"))
samples = harmful + benign
train = sorted((row for row in samples if row["split"] == "train"), key=lambda row: row["split_index"])
test = sorted((row for row in samples if row["split"] == "test"), key=lambda row: row["split_index"])
knowledge = json.loads((root / "C-harmKB.json").read_text(encoding="utf-8"))["terms"]
```

The [RIKE implementation guide](https://github.com/wimiw123/RIKE) provides the data-staging, training, retrieval, and inference commands.

## License

The dataset is provided under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). It contains offensive and harmful language for research on harmful content detection and interpretation. Dataset content does not express the authors' views.
