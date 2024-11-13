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