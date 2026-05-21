# Chapter 05, Python box 01: Inference for regression in Python
# Source label: box:pinf_reg
# Full runnable chapter script: ../chapter05.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy scipy statsmodels
# --- Code block 2 ---
import statsmodels.formula.api as smf

ols_model = smf.ols("price ~ living_area", data=df).fit()

beta1_hat = ols_model.params["living_area"]
se_beta1 = ols_model.bse["living_area"]
t_stat = ols_model.tvalues["living_area"]
p_value = ols_model.pvalues["living_area"]
ci_beta1_90 = ols_model.conf_int(alpha=0.10).loc["living_area"]
# --- Code block 3 ---
ols_model2 = smf.ols("price ~ new_production", data=df).fit()
ols_model2.params
ols_model2.conf_int(alpha=0.10)
