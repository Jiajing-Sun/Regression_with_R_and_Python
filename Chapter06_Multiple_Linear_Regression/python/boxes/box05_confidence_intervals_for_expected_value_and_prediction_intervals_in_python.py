# Chapter 06, Python box 05: Confidence intervals for expected value and prediction intervals in Python
# Source label: box:pci_pi
# Full runnable chapter script: ../chapter06.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install pandas statsmodels
# --- Code block 2 ---
import pandas as pd
import statsmodels.formula.api as smf

df_sr = df[["price", "living_area"]].dropna()
ols_model = smf.ols("price ~ living_area", data=df_sr).fit()

new80 = pd.DataFrame({"living_area": [80]})
pred = ols_model.get_prediction(new80).summary_frame(alpha=0.05)
