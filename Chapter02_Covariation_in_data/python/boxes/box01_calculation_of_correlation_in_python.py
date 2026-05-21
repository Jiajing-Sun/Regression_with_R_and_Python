# Chapter 02, Python box 01: Calculation of correlation in Python
# Source label: box:pkorr
# Full runnable chapter script: ../chapter02.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy pandas
# --- Code block 2 ---
import numpy as np
import pandas as pd

df = pd.read_csv("apartment_price_data.csv")
df = df[["living_area", "price"]].dropna()

xbar = df["living_area"].mean()
ybar = df["price"].mean()
n = len(df)

s_xy = ((df["living_area"] - xbar) * (df["price"] - ybar)).sum() / (n - 1)
s_x2 = ((df["living_area"] - xbar) ** 2).sum() / (n - 1)
s_y2 = ((df["price"] - ybar) ** 2).sum() / (n - 1)

corr_manual = s_xy / (np.sqrt(s_x2) * np.sqrt(s_y2))
corr_builtin = df["living_area"].corr(df["price"], method="pearson")
