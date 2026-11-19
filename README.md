# Dynamic Cellular Phenotype and Drug MoA Recognition

## Overview

This project studies dynamic cellular phenotypes in time-lapse microscopy after
drug treatment. Its research tasks include drug recognition, mechanism-of-action
(MoA) classification, and representation-based retrieval.

## Dataset

### MitoDataset

The project uses MitoDataset, introduced by Yu et al. in 2024. The dataset covers
1,068 US Food and Drug Administration approved drugs and a dimethyl sulfoxide
(DMSO) control. It contains 35,631 single-cell image sequences. Each sequence has
16 frames, for a total of 570,096 single-cell images.

No images, annotations, drug mappings, labels, or dataset splits are distributed
in this repository. Access to the dataset must follow the original authors'
release process and license terms.

### References

- Yu et al., *Deep learning large-scale drug discovery and repurposing*, 2024:
  [DOI 10.1038/s43588-024-00679-4](https://doi.org/10.1038/s43588-024-00679-4)
- Related method background:
  [MolCLIP](https://arxiv.org/abs/2507.07663)

## Technical Scope

The private research system investigates the following components at a high
level:

- an I3D/3D-ResNet50 temporal visual encoder;
- gated residual and multiscale spatiotemporal feature enhancement;
- MolFormer molecular representations and MolCLIP-style multimodal alignment;
- Hulu-Med, based on a Qwen2 language backbone, with parameter-efficient tuning;
- classification, metric learning, knowledge distillation, and retrieval.

These names describe the technical scope only. They do not disclose the private
architecture or training recipe.

## Environment

### Recommended Software

- Linux x86_64;
- Python 3.10;
- PyTorch 2.3 or later;
- Torchvision 0.18 or later;
- CUDA 12.1 for GPU execution;
- Transformers 4.46 or later;
- NumPy 1.24 or later;
- scikit-learn 1.3 or later.

### Installation

```bash
conda env create -f environment.yml
conda activate cell-public
```

The complete private project additionally requires separately licensed visual,
molecular, and language-model weights. This snapshot does not download or
redistribute those models.

## Hardware

The private experiments were developed on a Linux workstation with:

- 4 × NVIDIA GeForce RTX 3090 GPUs, 24 GB per GPU;
- 2 × Intel Xeon E5-2680 v4 CPUs, 28 cores and 56 threads in total;
- approximately 188 GB of system memory;
- NVIDIA driver 530.30.02.

This configuration describes the experimental workstation and is not a minimum
requirement. The public metric example can run on a CPU.

## Repository Contents

- `src/metrics.py`: generic classification and Rank-1 metric examples;
- `environment.yml`: Conda environment specification;
- `requirements.txt`: minimal dependencies;
- `.gitignore`: exclusions for data, weights, outputs, and local environments.

## Disclaimer

This repository is for research presentation only. It is not a clinical system
and must not be used for medical or drug-development decisions.

