# Chapter 08, Python box 02: Project Star and multilevel models in Python
# Source label: box:pmultilevel
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

multi_model = smf.mixedlm(
    "read_score ~ small_class", data=df, groups=df["class_id"]
).fit(reml=True)
print(multi_model.summary())

sigma2_class = float(multi_model.cov_re.iloc[0, 0])
sigma2_u = float(multi_model.scale)
share_class = sigma2_class / (sigma2_class + sigma2_u)
print(share_class)
