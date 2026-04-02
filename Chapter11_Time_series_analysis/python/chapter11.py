# Extracted Python code for Chapter 11: Time series analysis
# Source: CH11 Time series analysis.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

df = pd.read_csv("data/time_series_sweden.csv")

# ------------------------------------------------------------------------------
# Box 02: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

idx = pd.period_range(start="1981Q1", periods=len(df), freq="Q")
gdp = pd.Series(df["gdp"].to_numpy(), index=idx, name="gdp")

# ------------------------------------------------------------------------------
# Box 03: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt

gdp.plot()
plt.show()

# ------------------------------------------------------------------------------
# Box 04: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

gdpL1 = gdp.shift(1)
gdpL2 = gdp.shift(2)
gdpF1 = gdp.shift(-1)
gdpF2 = gdp.shift(-2)

# ------------------------------------------------------------------------------
# Box 05: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

ma = (gdpL2/2 + gdpL1 + gdp + gdpF1 + gdpF2/2) / 4

# ------------------------------------------------------------------------------
# Box 06: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

ma.plot()
plt.show()

# ------------------------------------------------------------------------------
# Box 07: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

mean_gdp = gdp.mean()

r_1 = ((gdp - mean_gdp) * (gdpL1 - mean_gdp)).sum() / ((gdp - mean_gdp) ** 2).sum()
r_1

# ------------------------------------------------------------------------------
# Box 08: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

acf_vals = acf(gdp.dropna(), fft=False)  # acf_vals[1] is the lag-1 autocorrelation

plot_acf(gdp.dropna(), lags=40)
plt.show()

# ------------------------------------------------------------------------------
# Box 09: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

dloggdp = (np.log(gdp) - np.log(gdpL1)) * 100

maL1 = ma.shift(1)
dlogma = (np.log(ma) - np.log(maL1)) * 100

# ------------------------------------------------------------------------------
# Box 10: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

dloggdp.plot()
plt.show()

dlogma.plot()
plt.show()

# ------------------------------------------------------------------------------
# Box 11: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

dloggdpL1 = dloggdp.shift(1)
dlogmaL1 = dlogma.shift(1)

dft = pd.concat(
    [gdp, gdpL1, gdpL2, gdpF1, gdpF2, ma, dloggdp, dlogma, dloggdpL1, dlogmaL1],
    axis=1
)
dft.columns = ["gdp", "gdpL1", "gdpL2", "gdpF1", "gdpF2", "ma",
               "dloggdp", "dlogma", "dloggdpL1", "dlogmaL1"]

# for regressions we usually drop missing rows created by leads/lags
dft_reg = dft[["dloggdp", "dloggdpL1"]].dropna()

# ------------------------------------------------------------------------------
# Box 12: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

import statsmodels.formula.api as smf

ar1_model = smf.ols("dloggdp ~ dloggdpL1", data=dft_reg).fit()
print(ar1_model.summary())

# ------------------------------------------------------------------------------
# Box 13: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

ar1_model_hac = ar1_model.get_robustcov_results(cov_type="HAC", maxlags=5)
print(ar1_model_hac.summary())

cov_matrix = ar1_model_hac.cov_params()
std_errors = np.sqrt(np.diag(cov_matrix))
std_errors

# ------------------------------------------------------------------------------
# Box 14: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

from statsmodels.tsa.ar_model import AutoReg

# AR(1) with intercept (trend="c")
ar1_model_alt = AutoReg(dloggdp.dropna(), lags=1, trend="c", old_names=False).fit()
print(ar1_model_alt.summary())

# ------------------------------------------------------------------------------
# Box 15: Time series analysis with Python
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

max_p = 5
y = dloggdp.dropna()

aic_table = []
res_store = {}

for p in range(1, max_p + 1):
    res_p = AutoReg(y, lags=p, trend="c", hold_back=max_p, old_names=False).fit()
    aic_table.append({"p": p, "AIC": res_p.aic})
    res_store[p] = res_p

aic_table = pd.DataFrame(aic_table).sort_values("AIC")
best_p = int(aic_table.iloc[0]["p"])

print(aic_table)
print("Selected order:", best_p)
print(res_store[best_p].summary())
