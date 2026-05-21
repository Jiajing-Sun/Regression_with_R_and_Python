# Chapter 11, Python box 01: Nonparametric RD in Python
# Source label: box:p_nonparametric_rd
# Full runnable chapter script: ../chapter11.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy pandas statsmodels linearmodels rdrobust
# --- Code block 2 ---
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from rdrobust import rdrobust

df = pd.read_csv("data/municip_data.csv")
df = df[df["municip_name"] != "Gotland"].copy()
df["rv"] = df["share_seats_left_last_election"] - 0.5
df["change_tax_rate"] = df["tax_rate"] - df["tax_rate_4_years_back"]
df = df.dropna(subset=["change_tax_rate"]).copy()
df["Z"] = (df["rv"] >= 0).astype(int)
df["Zrv"] = df["Z"] * df["rv"]

tri = lambda u: np.maximum(0.0, 1.0 - np.abs(u))
h = 0.10
df_h = df.loc[df["rv"].abs() <= h].copy()
df_h["w"] = tri(df_h["rv"] / h)
rd_fs_np = smf.wls("left_coalition_last_term ~ Z + rv + Zrv",
                   data=df_h, weights=df_h["w"]).fit()
rd_rf_np = smf.wls("change_tax_rate ~ Z + rv + Zrv",
                   data=df_h, weights=df_h["w"]).fit()
# --- Code block 3 ---
print(float(rd_rf_np.params["Z"] / rd_fs_np.params["Z"]))
print(rdrobust(y=df["change_tax_rate"],
               x=df["share_seats_left_last_election"],
               c=0.5, kernel="triangular",
               fuzzy=df["left_coalition_last_term"]))
