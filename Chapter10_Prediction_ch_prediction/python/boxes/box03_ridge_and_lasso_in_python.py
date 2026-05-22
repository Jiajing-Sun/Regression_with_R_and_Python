# Chapter 10, Python box 03: Ridge and lasso
# Source label: box:pridge_lasso
# Runnable chapter script: ../chapter10.py

from pathlib import Path
import os

import numpy as np
import pandas as pd
from sklearn.linear_model import LassoCV, RidgeCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

chapter_dir = Path(__file__).resolve().parents[2]
os.chdir(chapter_dir)

df = pd.read_csv("data/apartment_price_data.csv").dropna().copy()
y = df["price"].to_numpy()
X_df = pd.get_dummies(
    df.drop(columns=["price"]),
    columns=["build_year", "number_of_rooms"],
    drop_first=False,
)
X = X_df.to_numpy()

alphas = np.logspace(-4, 4, 100)
ridge_cv = make_pipeline(StandardScaler(), RidgeCV(alphas=alphas, cv=5)).fit(X, y)
lasso_cv = make_pipeline(
    StandardScaler(),
    LassoCV(alphas=alphas, cv=5, max_iter=100000),
).fit(X, y)

ridge_alpha = ridge_cv.named_steps["ridgecv"].alpha_
lasso_alpha = lasso_cv.named_steps["lassocv"].alpha_
lasso_nonzero = np.sum(lasso_cv.named_steps["lassocv"].coef_ != 0)

print("Selected ridge alpha:", round(float(ridge_alpha), 4))
print("Selected lasso alpha:", round(float(lasso_alpha), 4))
print("Non-zero lasso coefficients:", int(lasso_nonzero))
