# Chapter 10, Python box 02: Cross-validation
# Source label: box:pcrossval
# Runnable chapter script: ../chapter10.py

from pathlib import Path
import os

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

chapter_dir = Path(__file__).resolve().parents[2]
os.chdir(chapter_dir)

df = pd.read_csv("data/apartment_price_data.csv")
df = df[["price", "living_area"]].dropna().copy()
X = df[["living_area"]].to_numpy()
y = df["price"].to_numpy()

kf = KFold(n_splits=5, shuffle=True, random_state=12)
MSE_hat = []
for train_idx, test_idx in kf.split(X):
    model = LinearRegression().fit(X[train_idx], y[train_idx])
    pred = model.predict(X[test_idx])
    MSE_hat.append(np.mean((y[test_idx] - pred) ** 2))

print("Fold MSE:", np.round(MSE_hat, 3))
print("Cross-validated MSE:", round(float(np.mean(MSE_hat)), 3))
