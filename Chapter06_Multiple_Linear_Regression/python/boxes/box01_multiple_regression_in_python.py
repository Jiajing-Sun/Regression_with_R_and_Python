# Chapter 06, Python box 01: Multiple regression in Python
# Source label: box:pmult_reg
# Full runnable chapter script: ../chapter06.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install pandas statsmodels
# --- Code block 2 ---
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("apartment_price_data.csv")
ols_model = smf.ols(
    "price ~ living_area + monthly_fee + new_production", data=df
).fit()

ols_model_hc0 = ols_model.get_robustcov_results(cov_type="HC0", use_t=True)
print(ols_model_hc0.summary())
