# Chapter 08, Python box 01: Project Star and clustering in Python
# Source label: box:pklustring
# Full runnable chapter script: ../chapter08.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy pandas statsmodels
# --- Code block 2 ---
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("data/star.csv")
df["small_class"] = np.where(df["class_type"] == "SMALL", 1.0, np.nan)
df.loc[df["class_type"].isin(["AIDE", "REGULAR"]), "small_class"] = 0.0
df = df.dropna(subset=["read_score", "small_class", "class_id"]).copy()

ols_model = smf.ols("read_score ~ small_class", data=df).fit()
ols_hc0 = ols_model.get_robustcov_results(cov_type="HC0", use_t=True)
ols_cl = ols_model.get_robustcov_results(
    cov_type="cluster", groups=df["class_id"], use_t=True
)

print(ols_model.summary().tables[1])
print(ols_hc0.summary().tables[1])
print(ols_cl.summary().tables[1])
