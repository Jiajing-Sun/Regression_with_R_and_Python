# Chapter 12, Python box 01: Time series analysis with Python
# Source label: box:ptime_series
# Full runnable chapter script: ../chapter12.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy pandas matplotlib statsmodels
# --- Code block 2 ---
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.ar_model import AutoReg

df = pd.read_csv("data/time_series_sweden.csv")
idx = pd.period_range(start="1981Q1", periods=len(df), freq="Q")
gdp = pd.Series(df["gdp"].to_numpy(), index=idx, name="gdp")

gdpL1 = gdp.shift(1); gdpL2 = gdp.shift(2)
gdpF1 = gdp.shift(-1); gdpF2 = gdp.shift(-2)
ma = (gdpL2/2 + gdpL1 + gdp + gdpF1 + gdpF2/2) / 4
acf_vals = acf(gdp.dropna(), fft=False)

dloggdp = (np.log(gdp) - np.log(gdpL1)) * 100
dft = pd.DataFrame({"dloggdp": dloggdp,
                    "dloggdpL1": dloggdp.shift(1)}).dropna()
ar1_model = smf.ols("dloggdp ~ dloggdpL1", data=dft).fit()
print(ar1_model.summary())
# --- Code block 3 ---
print(ar1_model.get_robustcov_results(cov_type="HAC", maxlags=5).summary())
y = dloggdp.dropna()
res_store = {p: AutoReg(y, lags=p, trend="c", hold_back=5,
                        old_names=False).fit() for p in range(1, 6)}
best_p = min(res_store, key=lambda p: res_store[p].aic)
print(best_p, res_store[best_p].summary())
