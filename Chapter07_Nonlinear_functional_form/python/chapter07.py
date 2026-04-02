# Extracted Python code for Chapter 07: Nonlinear functional form
# Source: CH7 Nonlinear functional form.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

df = pd.read_csv("pollution_sf.csv")

# ------------------------------------------------------------------------------
# Box 02: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

bins = np.arange(0, 361, 10)  # 0,10,20,...,360
df["wind_cat"] = pd.cut(df["wind_direction"], bins=bins, include_lowest=True)

# ------------------------------------------------------------------------------
# Box 03: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

df_agg = (
    df.groupby("wind_cat", observed=True)["pm25"]
      .mean()
      .reset_index(name="pm25_mean")
)

# midpoint of each interval (e.g. (0,10] -> 5, (10,20] -> 15, ...)
df_agg["wind_direction"] = df_agg["wind_cat"].apply(
    lambda iv: (iv.left + iv.right) / 2
)

# ------------------------------------------------------------------------------
# Box 04: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.scatter(df_agg["wind_direction"], df_agg["pm25_mean"])
plt.show()

# ------------------------------------------------------------------------------
# Box 05: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

wd = df["wind_direction"]
ws = df["wind_speed"]

df["north_wind"] = np.where(wd.isna(), np.nan, ((wd > 315) | (wd <= 45)).astype(int))
df["east_wind"]  = np.where(wd.isna(), np.nan, ((wd > 45)  & (wd <= 135)).astype(int))
df["south_wind"] = np.where(wd.isna(), np.nan, ((wd > 135) & (wd <= 225)).astype(int))
df["west_wind"]  = np.where(wd.isna(), np.nan, ((wd > 225) & (wd <= 315)).astype(int))

df["land_wind"]   = np.where(wd.isna(), np.nan, ((wd > 330) | (wd <= 150)).astype(int))
df["strong_wind"] = np.where(ws.isna(), np.nan, (ws >= 3).astype(int))

# ------------------------------------------------------------------------------
# Box 06: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

df["wind_direction2"] = df["wind_direction"] ** 2
df["wind_direction3"] = df["wind_direction"] ** 3
df["wind_direction4"] = df["wind_direction"] ** 4

# ------------------------------------------------------------------------------
# Box 07: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

import statsmodels.formula.api as smf

ols_model_poly = smf.ols(
    "pm25 ~ wind_direction + wind_direction2 + wind_direction3 + wind_direction4",
    data=df
).fit()

# ------------------------------------------------------------------------------
# Box 08: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

ols_model_poly_alt = smf.ols(
    "pm25 ~ wind_direction + I(wind_direction**2) + I(wind_direction**3) + I(wind_direction**4)",
    data=df
).fit()

# ------------------------------------------------------------------------------
# Box 09: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

newdata = pd.DataFrame({"wind_direction": np.arange(0, 361, 1)})
newdata["pred"] = ols_model_poly_alt.predict(newdata)

# ------------------------------------------------------------------------------
# Box 10: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

newdata2 = newdata.copy()
newdata2["wind_direction2"] = newdata2["wind_direction"] ** 2
newdata2["wind_direction3"] = newdata2["wind_direction"] ** 3
newdata2["wind_direction4"] = newdata2["wind_direction"] ** 4

newdata["pred_alt"] = ols_model_poly.predict(newdata2)

# ------------------------------------------------------------------------------
# Box 11: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

plt.scatter(df_agg["wind_direction"], df_agg["pm25_mean"])
plt.plot(newdata["wind_direction"], newdata["pred"])
plt.show()

# ------------------------------------------------------------------------------
# Box 12: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

df["land_wind_strong_wind"] = df["land_wind"] * df["strong_wind"]
df["land_wind_wind_speed"]  = df["land_wind"] * df["wind_speed"]

# ------------------------------------------------------------------------------
# Box 13: Air pollution and weather in Python
# Textbook context: Section: Example: Relationship between weather and air pollution
# ------------------------------------------------------------------------------

ols_model1 = smf.ols("pm25 ~ land_wind", data=df).fit()
ols_model2 = smf.ols(
    "pm25 ~ land_wind + strong_wind + land_wind_strong_wind",
    data=df
).fit()
ols_model3 = smf.ols(
    "pm25 ~ land_wind + wind_speed + land_wind_wind_speed",
    data=df
).fit()

ols_model1_hc0 = ols_model1.get_robustcov_results(cov_type="HC0", use_t=True)
ols_model2_hc0 = ols_model2.get_robustcov_results(cov_type="HC0", use_t=True)
ols_model3_hc0 = ols_model3.get_robustcov_results(cov_type="HC0", use_t=True)

print(ols_model1_hc0.summary())
print(ols_model2_hc0.summary())
print(ols_model3_hc0.summary())
