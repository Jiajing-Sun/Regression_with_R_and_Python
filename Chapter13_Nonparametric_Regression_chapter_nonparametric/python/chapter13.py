# Extracted Python code for Chapter 13: Nonparametric Regression
# Source: nonparametric-chapter.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Nonparametric RD in Python (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:779-792
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("municip_data.csv")
df = df.loc[df["municip_name"] != "Gotland"].copy()

c0 = 0.5
df["rv"] = df["share_seats_left_last_election"] - c0
df["change_tax_rate"] = df["tax_rate"] - df["tax_rate_4_years_back"]
df = df.dropna(subset=["change_tax_rate"]).copy()

df["Z"] = (df["rv"] >= 0).astype(int)   # cutoff indicator
df["Zrv"] = df["Z"] * df["rv"]          # slope interaction

# ------------------------------------------------------------------------------
# Box 02: Nonparametric RD in Python (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:797-803
# ------------------------------------------------------------------------------

def tri(u):
    return np.maximum(0.0, 1.0 - np.abs(u))

h = 0.10

df_h = df.loc[df["rv"].abs() <= h].copy()
df_h["w"] = tri(df_h["rv"] / h)

# ------------------------------------------------------------------------------
# Box 03: Nonparametric RD in Python (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:808-826
# ------------------------------------------------------------------------------

# First stage (FS)
rd_fs_np = smf.wls(
    "left_coalition_last_term ~ Z + rv + Zrv",
    data=df_h,
    weights=df_h["w"]
).fit()

rd_fs_np_hc0 = rd_fs_np.get_robustcov_results(cov_type="HC0")
print(rd_fs_np_hc0.summary())

# Reduced form (RF)
rd_rf_np = smf.wls(
    "change_tax_rate ~ Z + rv + Zrv",
    data=df_h,
    weights=df_h["w"]
).fit()

rd_rf_np_hc0 = rd_rf_np.get_robustcov_results(cov_type="HC0")
print(rd_rf_np_hc0.summary())

# ------------------------------------------------------------------------------
# Box 04: Nonparametric RD in Python (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:835-839
# ------------------------------------------------------------------------------

delta_hat = float(rd_fs_np.params["Z"])
alpha_hat = float(rd_rf_np.params["Z"])
wald_hat  = alpha_hat / delta_hat

wald_hat

# ------------------------------------------------------------------------------
# Box 05: Nonparametric RD in Python (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:844-857
# ------------------------------------------------------------------------------

# pip install linearmodels
from linearmodels.iv import IV2SLS

# Option A (formula interface; works in recent versions of linearmodels):
rd_fuzzy_np = IV2SLS.from_formula(
    "change_tax_rate ~ 1 + rv + Zrv + [left_coalition_last_term ~ Z]",
    data=df_h,
    weights=df_h["w"]
).fit(cov_type="robust")

print(rd_fuzzy_np.summary)

iv_hat = float(rd_fuzzy_np.params["left_coalition_last_term"])
{"wald_hat": wald_hat, "iv_hat": iv_hat}

# ------------------------------------------------------------------------------
# Box 06: Nonparametric RD in Python (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:862-873
# ------------------------------------------------------------------------------

df_h2 = df_h.copy()
df_h2["const"] = 1.0

rd_fuzzy_np2 = IV2SLS(
    dependent=df_h2["change_tax_rate"],
    exog=df_h2[["const", "rv", "Zrv"]],
    endog=df_h2[["left_coalition_last_term"]],
    instruments=df_h2[["Z"]],
    weights=df_h2["w"]
).fit(cov_type="robust")

print(rd_fuzzy_np2.summary)

# ------------------------------------------------------------------------------
# Box 07: Nonparametric RD in Python (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:878-943
# ------------------------------------------------------------------------------

import os
import matplotlib.pyplot as plt

fig_dir = "pdf"
os.makedirs(fig_dir, exist_ok=True)

binwidth = 0.01
x = df["share_seats_left_last_election"]

# bin centers, matching the R construction
df["bin"] = (
    np.minimum(np.floor(x / binwidth) * binwidth, 1 - binwidth)
    + binwidth / 2
)

agg_fs = df.groupby("bin", as_index=False)["left_coalition_last_term"].mean()
agg_rf = df.groupby("bin", as_index=False)["change_tax_rate"].mean()

xlim = (c0 - h, c0 + h)

def fitted_side(params, xgrid, side="left"):
    rv = xgrid - c0
    b0 = params["Intercept"]
    b1 = params["Z"]
    b2 = params["rv"]
    b3 = params["Zrv"]
    if side == "left":
        return b0 + b2 * rv
    return (b0 + b1) + (b2 + b3) * rv

b_fs = rd_fs_np.params
b_rf = rd_rf_np.params

xL = np.linspace(xlim[0], c0, 200)
xR = np.linspace(c0, xlim[1], 200)

# --- First stage plot ---
agg_fs2 = agg_fs.loc[(agg_fs["bin"] >= xlim[0]) & (agg_fs["bin"] <= xlim[1])]

plt.figure(figsize=(4.2, 3.4))
plt.scatter(agg_fs2["bin"], agg_fs2["left_coalition_last_term"], s=18)
plt.axvline(c0, linestyle="--", linewidth=1.2)
plt.plot(xL, fitted_side(b_fs, xL, "left"),  linewidth=2.2)
plt.plot(xR, fitted_side(b_fs, xR, "right"), linewidth=2.2)
plt.xlim(xlim)
plt.ylim(0, 1)
plt.xlabel("# seats left-wing parties")
plt.ylabel("Left-wing ruling coalition")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "rd_municip_fs_agg_np.pdf"))
plt.close()

# --- Reduced form plot ---
agg_rf2 = agg_rf.loc[(agg_rf["bin"] >= xlim[0]) & (agg_rf["bin"] <= xlim[1])]

plt.figure(figsize=(4.2, 3.4))
plt.scatter(agg_rf2["bin"], agg_rf2["change_tax_rate"], s=18)
plt.axvline(c0, linestyle="--", linewidth=1.2)
plt.plot(xL, fitted_side(b_rf, xL, "left"),  linewidth=2.2)
plt.plot(xR, fitted_side(b_rf, xR, "right"), linewidth=2.2)
plt.xlim(xlim)
plt.xlabel("# seats left-wing parties")
plt.ylabel("Change in tax rate")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "rd_municip_rf_agg_d_np.pdf"))
plt.close()

# ------------------------------------------------------------------------------
# Box 08: Nonparametric RD in Python (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:948-959
# ------------------------------------------------------------------------------

# pip install rdrobust
from rdrobust import rdrobust

out_np = rdrobust(
    y=df["change_tax_rate"],
    x=df["share_seats_left_last_election"],
    c=0.5,
    kernel="triangular",
    fuzzy=df["left_coalition_last_term"]
)

print(out_np)
