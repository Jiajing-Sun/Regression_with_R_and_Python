# Chapter 06, Python box 02: Added-variable plot in Python
# Source label: box:added_variable_python
# Full runnable chapter script: ../chapter06.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install pandas statsmodels matplotlib
# --- Code block 2 ---
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("apartment_price_data.csv")
res_y = smf.ols("price ~ monthly_fee", data=df).fit().resid
res_x = smf.ols("living_area ~ monthly_fee", data=df).fit().resid

av_model = smf.ols("res_y ~ res_x", data={"res_y": res_y, "res_x": res_x}).fit()
multi_model = smf.ols("price ~ living_area + monthly_fee", data=df).fit()

av_model.params["res_x"], multi_model.params["living_area"]
