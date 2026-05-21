# Chapter 03, Python box 02: Hypothesis tests and confidence intervals with Python
# Source label: box:inference_py
# Full runnable chapter script: ../chapter03.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy scipy
# --- Code block 2 ---
import numpy as np
from scipy import stats

dice_throws = np.repeat([1, 2, 3, 4, 5, 6], [13, 7, 8, 9, 9, 4])

n = dice_throws.size
ybar = dice_throws.mean()
se = dice_throws.std(ddof=1) / np.sqrt(n)

t_stat = (ybar - 3.5) / se
p_value = 2 * stats.t.sf(np.abs(t_stat), df=n - 1)

alpha = 0.05
t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
ci = ybar + np.array([-1, 1]) * t_crit * se

ttest_res = stats.ttest_1samp(dice_throws, popmean=3.5)
