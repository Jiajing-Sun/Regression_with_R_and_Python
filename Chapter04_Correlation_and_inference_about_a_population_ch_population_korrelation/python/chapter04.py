# Extracted Python code for Chapter 04: Correlation and inference about a population
# Source: CH4 Correlation and inference.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Calculating confidence intervals for correlation in Python
# Source lines: CH4 Correlation and inference.tex:115-140
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("apartment_price_data.csv")

# ensure we use the same observations for both variables
tmp = df[["living_area", "price"]].dropna()
x = tmp["living_area"].to_numpy()
y = tmp["price"].to_numpy()
n = len(tmp)

# Pearson correlation
corrXY = np.corrcoef(x, y)[0, 1]

# Fisher z-transform
Z = 0.5 * np.log((1 + corrXY) / (1 - corrXY))

alpha = 0.05
z_alpha_2 = stats.norm.ppf(1 - alpha/2)

Z_L = Z - z_alpha_2 * np.sqrt(1 / (n - 3))
Z_U = Z + z_alpha_2 * np.sqrt(1 / (n - 3))

CI_L = (np.exp(2 * Z_L) - 1) / (np.exp(2 * Z_L) + 1)
CI_U = (np.exp(2 * Z_U) - 1) / (np.exp(2 * Z_U) + 1)

# ------------------------------------------------------------------------------
# Box 02: Calculating confidence intervals for correlation in Python
# Source lines: CH4 Correlation and inference.tex:148-156
# ------------------------------------------------------------------------------

res = stats.pearsonr(x, y)              # two-sided test by default
corrXY2 = res.statistic
p_value = res.pvalue

ci = res.confidence_interval(confidence_level=0.95)
CI_L2, CI_U2 = ci.low, ci.high

# if you also want the t-statistic (as reported by R's cor.test):
t_stat = corrXY2 * np.sqrt((n - 2) / (1 - corrXY2**2))
