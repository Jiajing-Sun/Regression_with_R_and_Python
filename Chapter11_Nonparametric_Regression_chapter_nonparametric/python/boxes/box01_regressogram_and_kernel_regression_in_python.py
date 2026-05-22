# Chapter 11, Python box 01: Regressogram and kernel regression in Python
# Source label: box:p_np_housing
# Full runnable chapter script: ../chapter11.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("data/apartment_price_data.csv")
df = df[["living_area", "price"]].dropna().copy()
x = df["living_area"].to_numpy()
y = df["price"].to_numpy()

ols = smf.ols("price ~ living_area", data=df).fit()
x_grid = np.linspace(20, 140, 250)


def gaussian_nw(x0, h=10):
    w = np.exp(-0.5 * ((x - x0) / h) ** 2)
    return np.sum(w * y) / np.sum(w)


kernel_fit = np.array([gaussian_nw(x, h=10) for x in x_grid])

bin_breaks = np.arange(15, 176, 10)
df["bin"] = pd.cut(df["living_area"], bins=bin_breaks, include_lowest=True)
regressogram = (
    df.groupby("bin", observed=True)
      .agg(price=("price", "mean"),
           living_area=("living_area", "mean"),
           n=("price", "size"))
      .reset_index()
)
regressogram_plot = regressogram.loc[regressogram["n"] >= 10]

selected_output = pd.DataFrame({
    "estimator": [
        "Linear regression at 50 sqm",
        "Regressogram, 45-55 sqm",
        "Gaussian kernel, h = 10",
    ],
    "estimate": [
        float(ols.predict(pd.DataFrame({"living_area": [50]})).iloc[0]),
        df.loc[df["living_area"].between(45, 55), "price"].mean(),
        gaussian_nw(50, h=10),
    ],
}).round({"estimate": 3})
print(selected_output)

Path("pdf").mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.size": 10})
fig, ax = plt.subplots(figsize=(5.69, 4.35))
ax.scatter(df["living_area"], df["price"], s=5.5, color="#F26B2A", alpha=0.75,
           linewidths=0)
linear_fit = ols.predict(pd.DataFrame({"living_area": x_grid}))
ax.plot(x_grid, linear_fit, color="0.15", linewidth=1.45, linestyle="-",
        label="Linear regression")
ax.plot(x_grid, kernel_fit, color="#005DAA", linewidth=1.75,
        linestyle="-.", label="Gaussian kernel")
ax.step(regressogram_plot["living_area"], regressogram_plot["price"],
        where="mid", color="#009E73", linewidth=1.45, linestyle="--",
        label="Regressogram")
ax.set_xlim(15, 150)
ax.set_ylim(0, 10)
ax.set_xlabel("Apartment size (sqm)")
ax.set_ylabel("Price (M. SEK)")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(direction="out", length=4, width=0.8)
ax.legend(frameon=False, loc="upper left", fontsize=8.2,
          handlelength=2.0, borderaxespad=0.2)
fig.tight_layout()
fig.savefig("pdf/apartment_price_nonparametric.pdf")
plt.close(fig)
