# Chapter 05, Python box 02: Robust inference in Python
# Source label: box:pinf_reg_robust
# Full runnable chapter script: ../chapter05.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install statsmodels
# --- Code block 2 ---
import statsmodels.formula.api as smf

ols_model = smf.ols("price ~ living_area", data=df).fit()
ols_model_hc0 = ols_model.get_robustcov_results(cov_type="HC0")
print(ols_model_hc0.summary())
