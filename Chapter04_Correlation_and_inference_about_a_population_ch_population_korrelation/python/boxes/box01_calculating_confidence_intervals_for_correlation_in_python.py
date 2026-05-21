# Chapter 04, Python box 01: Calculating confidence intervals for correlation in Python
# Source label: box:pkonfidensintervall
# Full runnable chapter script: ../chapter04.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy pandas scipy
# --- Code block 2 ---
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("apartment_price_data.csv")
tmp = df[["living_area", "price"]].dropna()
x = tmp["living_area"]
y = tmp["price"]
n = len(tmp)

corrXY = x.corr(y)
Z = 0.5 * np.log((1 + corrXY) / (1 - corrXY))
z_alpha_2 = stats.norm.ppf(0.975)
Z_L = Z - z_alpha_2 * np.sqrt(1 / (n - 3))
Z_U = Z + z_alpha_2 * np.sqrt(1 / (n - 3))
CI = (np.exp(2 * np.array([Z_L, Z_U])) - 1) / (np.exp(2 * np.array([Z_L, Z_U])) + 1)

res = stats.pearsonr(x, y)
