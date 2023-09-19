# Discrete Morse theory
This repository contains the implementation of discrete Morse theory "[Topology-aware Segmentation Using Discrete Morse Theory](https://openreview.net/pdf?id=LGgdb4TS4Z)", **accepted to ICLR 2021 (Spotlight)**. 

## This folder contains two subfolders:

1. morse_DMT: this folder contains the implementation for real discrete morse theory and captures the real morse structure. 

It works for 2D and 3D vessel data.

2. persistence_ws: this folder contains the implementation for persistence-based watershed algorithm. It's a relaxed version of morse structure.

It works for 2D and 3D volume data.

## Citation
Please consider citing our paper if you find it useful.
```
@article{hu2019topology,
  title={Topology-preserving deep image segmentation},
  author={Hu, Xiaoling and Li, Fuxin and Samaras, Dimitris and Chen, Chao},
  journal={Advances in neural information processing systems},
  volume={32},
  year={2019}
}

@inproceedings{hu2020topology,
  title={Topology-Aware Segmentation Using Discrete Morse Theory},
  author={Hu, Xiaoling and Wang, Yusu and Fuxin, Li and Samaras, Dimitris and Chen, Chao},
  booktitle={International Conference on Learning Representations},
  year={2021}
}
