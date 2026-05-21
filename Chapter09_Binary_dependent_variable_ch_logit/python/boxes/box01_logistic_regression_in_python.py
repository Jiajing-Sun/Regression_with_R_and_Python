# Chapter 09, Python box 01: Logistic regression in Python
# Source label: box:plogit
# Full runnable chapter script: ../chapter09.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy pandas statsmodels
# --- Code block 2 ---
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv("data/municip_data.csv")
df = df[df["year"] == 2022].copy()

df["high_income"] = (df["tax_base"] > df["tax_base"].quantile(0.75)).astype(int)
df["lnpop"] = np.log(df["pop"])

logit_model2 = smf.glm(
    "high_income ~ share_tertiary_school + lnpop",
    data=df,
    family=sm.families.Binomial(link=sm.families.links.logit())
).fit()
print(logit_model2.summary())

beta1hat = float(logit_model2.params["share_tertiary_school"])
odds_ratio_x1 = np.exp(beta1hat * 0.01)
print(odds_ratio_x1)
