# Chapter 03, Python box 01: Monte Carlo simulation in Python
# Source label: box:sim_py
# Full runnable chapter script: ../chapter03.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy matplotlib
# --- Code block 2 ---
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(123)
n = 50
nr_samples = 10000

ybar_dist = rng.integers(1, 7, size=(nr_samples, n)).mean(axis=1)

mean_ybar = ybar_dist.mean()
var_ybar = ybar_dist.var(ddof=1)
plt.hist(ybar_dist, bins=50)
