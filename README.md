# Ex-ToxiCN-MM: A Large-Scale Explainable Chinese Harmful Meme Dataset

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18229215.svg)](https://doi.org/10.5281/zenodo.18229215)  <-- Image Dataset

This repository contains the dataset and code for the paper: **"Distinguishing Right from Wrong in Debates: Attribution Analysis of Chinese Harmful Memes"**.


## 📖 Introduction

**Ex-ToxiCN-MM** is the first explainable Chinese harmful meme dataset designed to address the challenges of cultural dependency and semantic ambiguity in meme detection. Unlike traditional datasets that only provide classification labels, Ex-ToxiCN-MM offers **dual-opposing interpretations** for each meme:
1.  **Harmful Interpretation:** Investigates the underlying malicious intent or cultural bias.
2.  **Non-harmful Interpretation:** Simulates a superficial or benign reading of the content.

We also release **C-HarmKB** (Chinese Harmful Semantic Knowledge Base), which contains 2,870 entries of Chinese slang, offensive vocabulary, and cultural concepts to support knowledge-enhanced reasoning.

## 📊 Dataset Statistics

The dataset consists of **7,042 samples** collected from major Chinese social platforms (e.g., Weibo, Tieba).

| Category          |   Count    | Description                                                            |
| :---------------- | :--------: | :--------------------------------------------------------------------- |
| **Total Samples** | **7,042**  |                                                                        |
| Harmful Memes     |   3,735    | Memes containing Targeted Harm, Sexual Innuendo, General Offense, etc. |
| Non-harmful Memes |   3,307    | Benign humor, self-deprecation, or daily life sharing.                 |
| **Explanations**  | **14,084** | Avg. length: 33.29 characters.                                         |

### Harmful Categories Breakdown
- **Targeted Harm:** 889
- **General Offense:** 1,078
- **Sexual Innuendo:** 1,367
- **Disparaging Culture:** 1,040

## 📚 C-HarmKB: Chinese Harmful Semantic Knowledge Base

[cite_start]To address the challenges posed by the lack of cultural background knowledge in detecting Chinese harmful memes, we constructed **C-HarmKB** (Chinese Harmful Semantic Knowledge Base)[cite: 10, 66]. This knowledge base empowers models to decipher implicit meanings and metaphors rooted in Chinese internet culture.

### 🛠️ Construction & Statistics
* [cite_start]**Scale:** The knowledge base comprises **2,870 entries** of Chinese slang, offensive vocabulary, and cultural concepts[cite: 248].
* [cite_start]**Data Sources:** Terms were systematically harvested via web crawlers from encyclopedic sources (e.g., **Baidu Baike**, **Wikipedia**) and specialized subculture forums[cite: 250].
* [cite_start]**Quality Control:** All terms underwent a rigorous multi-step annotation process by native speakers proficient in Chinese internet culture to ensure accurate definitions and classifications[cite: 254].

### 🗂️ Taxonomy
[cite_start]To facilitate fine-grained analysis, entries are categorized into predefined classes[cite: 254]:
* **Sexism**
* **Racism**
* **Region**
* **LGBTQ**
* **Others** (including general insults and political slang)

### 📝 Data Example
Each entry includes the slang term, its category, and a detailed definition clarifying its cultural context and harmful connotation. [cite_start]Below is a sample entry derived from the "Vegetable Dog" meme example[cite: 56, 57, 210, 211, 212]:

```json
{
  "term": "菜狗 (Vegetable Dog)",
  "category": "General Offense",
  "definition": "Describes someone who is very poor at skills and has a low level, like a combination of 'newbie' and 'dog'. It is often used to insult and demean others' abilities."
}
```
---
## 📂 Repository Structure

```text
.
├── data/
│   ├── train.json       # Training set annotations
│   ├── test.json        # Test set annotations
│   ├── C-HarmKB.json    # The knowledge base
│   └── images/          # Image files (see Release for full download)
├── code/                # Source code for the RIKE framework
├── README.md            # This file
└── LICENSE              # License file
📝 Data Format
Each entry in the JSON file follows this format:

JSON

{
  "id": "image_filename.jpg",
  "text": "Meme text content",
  "label": "harmful",
  "category": "General Offense",
  "interpretations": {
    "harmful": "Explanation from a harmful perspective...",
    "non_harmful": "Explanation from a non-harmful perspective..."
  }
}

```
---
## ⚠️ Ethics Statement & Disclaimer
Warning: This dataset contains content that may be offensive, hateful, or disturbing, including hate speech, stereotypes, and sexual innuendo. These materials are provided solely for academic research purposes (e.g., improving content moderation systems).

The views expressed in the dataset do not reflect the views of the authors or their affiliations.

We strongly condemn the misuse of this dataset to generate or promote harmful content.

Please refer to the paper for details on annotator well-being protection measures.

## 📜 License
This dataset is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. Commercial use is strictly prohibited.

## 🖊️ Citation
If you find this work useful, please cite our paper:

代码段
```text
@article{wang2026distinguishing,
  title={Distinguishing Right from Wrong in Debates: Attribution Analysis of Chinese Harmful Memes},
  author={Wang, Weiming and Lu, Junyu and Wang, Han and Zhang, Xiaokun and Bai, Zewen and Xu, Bo and Yang, Liang and Lin, Hongfei},
  journal={arXiv preprint/Submission},
  year={2026}
}
```
## 🙏 Acknowledgments
This research is supported by the Natural Science Foundation of China (No. 62376051) and the Fundamental Research Funds for the Central Universities.