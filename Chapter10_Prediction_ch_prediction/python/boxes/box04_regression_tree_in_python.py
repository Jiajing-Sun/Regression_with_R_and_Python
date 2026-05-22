# Chapter 10, Python box 04: Regression tree
# Source label: box:pregression_tree
# Runnable chapter script: ../chapter10.py

from pathlib import Path
import os

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.tree import DecisionTreeRegressor

chapter_dir = Path(__file__).resolve().parents[2]
os.chdir(chapter_dir)

df = pd.read_csv("data/apartment_price_data.csv")
df = df[["price", "living_area", "monthly_fee"]].dropna().copy()
X = df[["living_area", "monthly_fee"]].to_numpy()
y = df["price"].to_numpy()

tree = DecisionTreeRegressor(
    min_samples_split=20,
    min_samples_leaf=5,
    ccp_alpha=0.0,
    random_state=12,
).fit(X, y)

path = tree.cost_complexity_pruning_path(X, y)
cv = KFold(n_splits=5, shuffle=True, random_state=12)
mse_cv = []
for alpha in path.ccp_alphas:
    candidate = DecisionTreeRegressor(
        min_samples_split=20,
        min_samples_leaf=5,
        ccp_alpha=alpha,
        random_state=12,
    )
    mse_cv.append(-cross_val_score(
        candidate,
        X,
        y,
        cv=cv,
        scoring="neg_mean_squared_error",
    ).mean())

best_alpha = path.ccp_alphas[int(np.argmin(mse_cv))]
pruned_tree = DecisionTreeRegressor(
    min_samples_split=20,
    min_samples_leaf=5,
    ccp_alpha=best_alpha,
    random_state=12,
).fit(X, y)

print("Unpruned leaves:", tree.get_n_leaves())
print("Selected ccp_alpha:", round(float(best_alpha), 4))
print("Pruned leaves:", pruned_tree.get_n_leaves())
