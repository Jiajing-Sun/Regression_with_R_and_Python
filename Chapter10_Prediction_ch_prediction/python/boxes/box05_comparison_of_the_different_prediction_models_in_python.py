# Chapter 10, Python box 05: Comparison of prediction models
# Source label: box:pprediction_comparison
# Runnable chapter script: ../chapter10.py

from pathlib import Path
import os

import numpy as np
import pandas as pd
from sklearn.linear_model import LassoCV, LinearRegression, RidgeCV
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

chapter_dir = Path(__file__).resolve().parents[2]
os.chdir(chapter_dir)

df = pd.read_csv("data/apartment_price_data.csv")
df["elevator_missing"] = df["elevator"].isna().astype(int)
df["elevator"] = df["elevator"].fillna(0)
df["living_area2"] = df["living_area"] ** 2
df["monthly_fee2"] = df["monthly_fee"] ** 2
df = df.dropna().copy()

room_data = {}
for room_size in range(2, 7):
    room = (df["number_of_rooms"] == room_size).astype(int)
    room_data[f"room_size_{room_size}"] = room
    room_data[f"city_area_room_size_{room_size}"] = df["city_area"] * room
room_df = pd.DataFrame(room_data, index=df.index)

decade_data = {}
for year in range(1900, 2011, 10):
    name = f"build_decade_{year}"
    decade = ((df["build_year"] >= year) & (df["build_year"] <= year + 9)).astype(int)
    decade_data[name] = decade
    decade_data[f"city_area_build_decade_{year}"] = df["city_area"] * decade
decade_df = pd.DataFrame(decade_data, index=df.index)

year_data = {}
year_values = sorted(df["build_year"].unique())
for year in year_values[1:]:
    name = f"build_year_{year}"
    year_dummy = (df["build_year"] == year).astype(int)
    year_data[name] = year_dummy
    year_data[f"city_area_build_year_{year}"] = df["city_area"] * year_dummy
year_df = pd.DataFrame(year_data, index=df.index)

df = pd.concat([df, room_df, decade_df, year_df], axis=1)

room_vars = list(room_df.columns)
decade_vars = list(decade_df.columns)
year_vars = list(year_df.columns)
rest_vars = [
    "living_area", "new_production", "monthly_fee", "city_area",
    "elevator", "elevator_missing", "living_area2", "monthly_fee2",
]
tree_vars = [
    "living_area", "new_production", "monthly_fee", "city_area",
    "elevator", "number_of_rooms", "build_year",
]

Y = df["price"].to_numpy()
X_year = df[room_vars + year_vars + rest_vars].to_numpy()
X_decade = df[room_vars + decade_vars + rest_vars].to_numpy()
X_tree = df[tree_vars].to_numpy()

rng = np.random.default_rng(12)
n = len(df)
train = rng.choice(n, size=int(0.8 * n), replace=False)
test = np.setdiff1d(np.arange(n), train)

alphas = np.logspace(-4, 4, 100)
models = {
    "OLS (year)": (LinearRegression(), X_year),
    "Ridge (year)": (make_pipeline(StandardScaler(), RidgeCV(alphas=alphas, cv=5)), X_year),
    "Lasso (year)": (make_pipeline(StandardScaler(), LassoCV(alphas=alphas, cv=5, max_iter=200000)), X_year),
    "OLS (decade)": (LinearRegression(), X_decade),
    "Ridge (decade)": (make_pipeline(StandardScaler(), RidgeCV(alphas=alphas, cv=5)), X_decade),
    "Lasso (decade)": (make_pipeline(StandardScaler(), LassoCV(alphas=alphas, cv=5, max_iter=200000)), X_decade),
}

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

rows = []
for name, (model, X) in models.items():
    fit = model.fit(X[train, :], Y[train])
    yhat = fit.predict(X)
    rows.append({"model": name, "MSE_train": mse(Y[train], yhat[train]), "MSE_test": mse(Y[test], yhat[test])})

tree0 = DecisionTreeRegressor(min_samples_split=20, min_samples_leaf=5, ccp_alpha=0, random_state=12)
path = tree0.fit(X_tree[train, :], Y[train]).cost_complexity_pruning_path(X_tree[train, :], Y[train])
cv = KFold(n_splits=5, shuffle=True, random_state=12)
tree_mse = []
for alpha in path.ccp_alphas:
    candidate = DecisionTreeRegressor(min_samples_split=20, min_samples_leaf=5, ccp_alpha=alpha, random_state=12)
    tree_mse.append(-cross_val_score(candidate, X_tree[train, :], Y[train], cv=cv, scoring="neg_mean_squared_error").mean())
tree = DecisionTreeRegressor(
    min_samples_split=20,
    min_samples_leaf=5,
    ccp_alpha=path.ccp_alphas[int(np.argmin(tree_mse))],
    random_state=12,
).fit(X_tree[train, :], Y[train])
yhat_tree = tree.predict(X_tree)
rows.append({"model": "CART", "MSE_train": mse(Y[train], yhat_tree[train]), "MSE_test": mse(Y[test], yhat_tree[test])})

print(pd.DataFrame(rows).round(3))
