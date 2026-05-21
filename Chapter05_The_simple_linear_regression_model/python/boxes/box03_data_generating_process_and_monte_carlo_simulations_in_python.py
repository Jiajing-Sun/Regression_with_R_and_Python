# Chapter 05, Python box 03: Data generating process and Monte Carlo simulations in Python
# Source label: box:pdgp
# Full runnable chapter script: ../chapter05.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy matplotlib
# --- Code block 2 ---
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(123)
nr_samples, n = 10000, 30
tstat_dist = np.empty(nr_samples)

for i in range(nr_samples):
    X = rng.uniform(0, 1, size=n)
    E = rng.chisquare(df=1, size=n)
    Y = 0.3 + 0.2 * X * E

    SXX = ((X - X.mean()) ** 2).sum()
    beta1_hat = ((X - X.mean()) * (Y - Y.mean())).sum() / SXX
    beta0_hat = Y.mean() - beta1_hat * X.mean()
    u_hat = Y - (beta0_hat + beta1_hat * X)

    se_beta1 = np.sqrt(((u_hat ** 2).sum() / (n - 2)) / SXX)
    tstat_dist[i] = (beta1_hat - 0.2) / se_beta1

plt.hist(tstat_dist, bins=100)
