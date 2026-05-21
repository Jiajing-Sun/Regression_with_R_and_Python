# Chapter 02, Python box 03: Regression in Python
# Source label: box:pols
# Full runnable chapter script: ../chapter02.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy pandas statsmodels
# --- Code block 2 ---
import statsmodels.formula.api as smf

beta_1_hat = s_xy / s_x2
beta_0_hat = ybar - xbar * beta_1_hat

ols_model = smf.ols("price ~ living_area", data=df).fit()
ols_model.params
ols_model.rsquared
