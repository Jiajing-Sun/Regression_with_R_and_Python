# Chapter 07, Python box 01: Air pollution and weather in Python
# Source label: box:ppollution_weather
# Full runnable chapter script: ../chapter07.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy pandas statsmodels matplotlib
# --- Code block 2 ---
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("pollution_sf.csv")

bins = np.arange(0, 361, 10)
df["wind_cat"] = pd.cut(df["wind_direction"], bins=bins, include_lowest=True)
df_agg = df.groupby("wind_cat", observed=True)["pm25"].mean().reset_index(name="pm25_mean")
df_agg["wind_direction"] = np.arange(5, 360, 10)

wd, ws = df["wind_direction"], df["wind_speed"]
df["land_wind"] = np.where((wd > 330) | (wd <= 150), 1, 0)
df["strong_wind"] = np.where(ws >= 3, 1, 0)
df["land_wind_strong_wind"] = df["land_wind"] * df["strong_wind"]
df["land_wind_wind_speed"] = df["land_wind"] * df["wind_speed"]

ols_model_poly = smf.ols(
    "pm25 ~ wind_direction + I(wind_direction**2) + I(wind_direction**3) + I(wind_direction**4)",
    data=df
).fit()
ols_model2 = smf.ols(
    "pm25 ~ land_wind + strong_wind + land_wind_strong_wind", data=df
).fit()
ols_model2_hc0 = ols_model2.get_robustcov_results(cov_type="HC0", use_t=True)
