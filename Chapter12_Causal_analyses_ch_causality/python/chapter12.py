# Extracted Python code for Chapter 12: Causal analyses
# Source: CH12 Causal analyses.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: RD approach in Python
# Textbook context: Section: The regression discontinuity approach | Subsection: Example in R with municipal data
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

df = pd.read_csv("municip_data.csv")
df = df[df["municip_name"] != "Gotland"].copy()

df["rv"] = df["share_seats_left_last_election"] - 0.5
df["change_tax_rate"] = df["tax_rate"] - df["tax_rate_4_years_back"]

# remove missing tax changes (to use the same sample throughout)
df = df.dropna(subset=["change_tax_rate"]).copy()

df["Z"] = (df["rv"] >= 0).astype(int)
df["Zrv"] = df["Z"] * df["rv"]

# ------------------------------------------------------------------------------
# Box 02: RD approach in Python
# Textbook context: Section: The regression discontinuity approach | Subsection: Example in R with municipal data
# ------------------------------------------------------------------------------

import statsmodels.formula.api as smf

h = 0.05
df_h = df.loc[df["rv"].abs() <= h].copy()

# first stage (FS)
rd_fs = smf.ols("left_coalition_last_term ~ Z + rv + Zrv", data=df_h).fit()
rd_fs_hc0 = rd_fs.get_robustcov_results(cov_type="HC0")
print(rd_fs_hc0.summary())

# reduced form (RF)
rd_rf = smf.ols("change_tax_rate ~ Z + rv + Zrv", data=df_h).fit()
rd_rf_hc0 = rd_rf.get_robustcov_results(cov_type="HC0")
print(rd_rf_hc0.summary())

# ------------------------------------------------------------------------------
# Box 03: RD approach in Python
# Textbook context: Section: The regression discontinuity approach | Subsection: Example in R with municipal data
# ------------------------------------------------------------------------------

df_h["Dhat"] = rd_fs.predict(df_h)

rd_2sls_naive = smf.ols("change_tax_rate ~ Dhat + rv + Zrv", data=df_h).fit()
print(rd_2sls_naive.summary())

# ------------------------------------------------------------------------------
# Box 04: RD approach in Python
# Textbook context: Section: The regression discontinuity approach | Subsection: Example in R with municipal data
# ------------------------------------------------------------------------------

# pip install linearmodels
from linearmodels.iv import IV2SLS

rd_2sls = IV2SLS.from_formula(
    "change_tax_rate ~ 1 + rv + Zrv + [left_coalition_last_term ~ Z]",
    data=df_h
).fit(cov_type="robust")

print(rd_2sls.summary)

# ------------------------------------------------------------------------------
# Box 05: RD approach in Python
# Textbook context: Section: The regression discontinuity approach | Subsection: Example in R with municipal data
# ------------------------------------------------------------------------------

# pip install rdrobust
from rdrobust import rdrobust

rd_fs_alt = rdrobust(
    y=df["left_coalition_last_term"],
    x=df["share_seats_left_last_election"],
    c=0.5, kernel="uniform", h=h
)
print(rd_fs_alt)

# ------------------------------------------------------------------------------
# Box 06: RD approach in Python
# Textbook context: Section: The regression discontinuity approach | Subsection: Example in R with municipal data
# ------------------------------------------------------------------------------

rd_2sls_alt = rdrobust(
    y=df["change_tax_rate"],
    x=df["share_seats_left_last_election"],
    c=0.5, kernel="uniform", h=h,
    fuzzy=df["left_coalition_last_term"]
)
print(rd_2sls_alt)
