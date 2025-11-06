# Release Notes - v0.1.1

## Overview

This patch release improves the package documentation, adds automated CI/CD workflows, and establishes the package as a companion to the upcoming **clip-conformal** package.

## What's New

### Documentation Improvements

- **Enhanced README**: Repositioned the package as a companion data package for clip-conformal
- **Installation Guide**: Added clear pip installation instructions
- **Quick Start Example**: Included Python code snippet for immediate usage
- **Relationship Section**: Explained the complementary nature with clip-conformal package
- **Proper Citations**: Added BibTeX format citations with correct author information
- **Improved Table Formatting**: Fixed dataset summary table to render properly in Markdown

### Automation & Infrastructure

- **GitHub Actions CI**: Automated testing across Python 3.9-3.12
- **Automated PyPI Publishing**: Push a version tag to automatically release to PyPI
- **Release Instructions**: Comprehensive guide for maintainers (RELEASE.md)
- **Development Setup**: Added .gitignore for cleaner repository management

## Installation

```bash
pip install conformal-clip-data==0.1.1
```

## Quick Start

```python
from conformal_clip_data import get_data_path

# Access the textile dataset
data_path = get_data_path("textile")
print(f"Dataset location: {data_path}")
```

## Dataset Contents

The textile image dataset remains unchanged from v0.1.0:

| Class | Count |
|-------|-------|
| Nominal images | 1,000 |
| Local defects | 500 |
| Global defects | 500 |

All images are 250 × 250 px, generated using the spc4sts R package.

## Citation

If you use this dataset, please cite:

```bibtex
@misc{megahed2025adaptingopenaisclipmodel,
      title={Adapting OpenAI's CLIP Model for Few-Shot Image Inspection in Manufacturing Quality Control: An Expository Case Study with Multiple Application Examples},
      author={Fadel M. Megahed and Ying-Ju Chen and Bianca Maria Colosimo and Marco Luigi Giuseppe Grasso and L. Allison Jones-Farmer and Sven Knoth and Hongyue Sun and Inez Zwetsloot},
      year={2025},
      eprint={2501.12596},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2501.12596},
}
```

## Coming Soon

The **clip-conformal** package will be released to PyPI shortly, providing full implementation of conformal prediction methods for CLIP models, with complete examples using this dataset.

## Full Changelog

See [CHANGELOG.md](CHANGELOG.md) for complete details.
