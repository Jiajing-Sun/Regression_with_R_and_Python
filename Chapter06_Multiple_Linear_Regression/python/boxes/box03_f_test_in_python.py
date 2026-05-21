# Chapter 06, Python box 03: $F$-test in Python
# Source label: box:pf_test
# Full runnable chapter script: ../chapter06.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install pandas statsmodels
# --- Code block 2 ---
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("apartment_price_data.csv")
cols = ["price", "living_area", "monthly_fee", "new_production", "build_year"]
df_cc = df[cols].dropna()

ols_model_l = smf.ols(
    "price ~ living_area + monthly_fee + new_production + build_year", data=df_cc
).fit()
ols_model_s = smf.ols("price ~ living_area + monthly_fee", data=df_cc).fit()

F_sm, p_sm, df_diff = ols_model_l.compare_f_test(ols_model_s)
