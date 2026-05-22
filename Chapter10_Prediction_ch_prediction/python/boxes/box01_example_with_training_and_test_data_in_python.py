# Chapter 10, Python box 01: Example with training and test data
# Source label: box:ptraining_test
# Runnable chapter script: ../chapter10.py

from pathlib import Path
import os

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

chapter_dir = Path(__file__).resolve().parents[2]
os.chdir(chapter_dir)

df = pd.read_csv("data/apartment_price_data.csv")
df = df[["price", "living_area"]].dropna().copy()
for i in range(2, 11):
    df[f"living_area{i}"] = df["living_area"] ** i

rng = np.random.default_rng(12)
n = len(df)
train_ind = rng.choice(n, size=int(0.8 * n), replace=False)
test_ind = np.setdiff1d(np.arange(n), train_ind)
df_train = df.iloc[train_ind].copy()
df_test = df.iloc[test_ind].copy()

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

rows = []
for degree in [1, 2, 3, 4, 5, 10]:
    features = ["living_area"] + [f"living_area{i}" for i in range(2, degree + 1)]
    model = LinearRegression().fit(df_train[features], df_train["price"])
    rows.append({
        "polynomials": degree,
        "MSE_train": mse(df_train["price"], model.predict(df_train[features])),
        "MSE_test": mse(df_test["price"], model.predict(df_test[features])),
    })

print(pd.DataFrame(rows).round(3))
