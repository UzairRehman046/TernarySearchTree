# Ternary Search Tree (TST) Project

This project implements a **Ternary Search Tree (TST)** in Python — a specialized data structure for efficient string storage and retrieval, combining properties of both binary search trees and tries. This implementation supports:

###  Functions

Insertion of strings (including the empty string)
Searching with prefix or exact match behavior
Counting and listing stored words
Pretty-printing the tree structure
Code benchmarking with performance plots
HPC execution via SLURM on KU Leuven Genius cluster

---

##  Project Structure

```
ternary-search-tree-project/
│
├── ternary_search_tree.py      # Main class implementation
├── benchmark_tst.py            # Benchmarking and performance evaluation script
├── data/search_trees/corncob_lowercase.txt       # Word list used for testing
├── benchmark_plot.png          # Saved plot of benchmark results
├── main_job.slurm              # SLURM job script for HPC execution
└── README.md                   # This file
```