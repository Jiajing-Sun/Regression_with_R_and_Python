# Chapter 13, Python box 01: RD approach in Python
# Source label: box:prd
# Full runnable chapter script: ../chapter13.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy pandas statsmodels linearmodels rdrobust
# --- Code block 2 ---
import pandas as pd
import statsmodels.formula.api as smf
from linearmodels.iv import IV2SLS
from rdrobust import rdrobust

df = pd.read_csv("data/municip_data.csv")
df = df[df["municip_name"] != "Gotland"].copy()
df["rv"] = df["share_seats_left_last_election"] - 0.5
df["change_tax_rate"] = df["tax_rate"] - df["tax_rate_4_years_back"]
df = df.dropna(subset=["change_tax_rate"]).copy()
df["Z"] = (df["rv"] >= 0).astype(int)
df["Zrv"] = df["Z"] * df["rv"]

h = 0.05
df_h = df.loc[df["rv"].abs() <= h].copy()
rd_fs = smf.ols("left_coalition_last_term ~ Z + rv + Zrv", data=df_h).fit()
rd_rf = smf.ols("change_tax_rate ~ Z + rv + Zrv", data=df_h).fit()
print(rd_fs.get_robustcov_results(cov_type="HC0").summary())
print(rd_rf.get_robustcov_results(cov_type="HC0").summary())
# --- Code block 3 ---
rd_2sls = IV2SLS.from_formula(
    "change_tax_rate ~ 1 + rv + Zrv + [left_coalition_last_term ~ Z]",
    data=df_h).fit(cov_type="robust")
print(rd_2sls.summary)
print(rdrobust(y=df["change_tax_rate"],
               x=df["share_seats_left_last_election"],
               c=0.5, kernel="uniform", h=h,
               fuzzy=df["left_coalition_last_term"]))
