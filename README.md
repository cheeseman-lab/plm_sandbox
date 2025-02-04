# plm_sandbox

General sandbox for running plms to extract mean embeddings of various proteins.

## Sandbox Environment
First, create and activate a conda environment for the sandbox:

```bash
conda env create -f environment.yml
conda activate sandbox
```

## Protein Language Models Environment
For installing all underlying protein language models, we use a different environment:

```bash
sh setup_plm.sh
conda activate plm
```

# Protein Language Model Sandbox

A toolkit for extracting embeddings from various protein language models (PLMs). This repository provides a standardized interface for working with different PLMs and processing protein sequence data.

## Project Structure

```
sandbox/
├── plm/                    # Protein Language Model implementations
│   ├── ankh/              # ANKH model extractor
│   ├── esm/               # ESM model extractor
│   ├── one-hot/           # One-hot encoding implementation
│   ├── prot_t5/           # ProtT5 model extractor
│   ├── proteinbert/       # ProteinBERT model extractor
│   ├── unirep/            # UniRep model extractor
│   └── clone_git_plms.py  # Script to clone external PLM repositories
├── src/                   # Core source code
│   ├── process.py         # Data processing utilities
│   └── utils.py          # General utility functions
└── scripts/              # Runtime scripts
    └── process/          # Data processing scripts
```

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Install the conda environment for working with embeddings:
```bash
conda env create -f environment.yml
conda activate emmentalembed
```

3. Install the conda environment for generating embeddings:
```bash
sh setup_plm.sh
conda activate plm
```

## Usage

### Generating Embeddings

Each PLM has its own `extract.py` script with a standardized interface. The general usage pattern is:

Sample SLURM scripts (for use on the Whitehead cluster reside in the `scripts/` directory)

### Processing & Analyzing Isoform Data

The toolkit includes utilities for processing isoform data:

```python
from sandbox.src.process import process_isoform_data

process_isoform_data(
    input_file='path/to/input.csv',
    output_label_file='path/to/labels.csv',
    output_fasta_file='path/to/sequences.fasta'
)
```

