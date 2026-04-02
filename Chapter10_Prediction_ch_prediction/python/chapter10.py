# Extracted Python code for Chapter 10: Prediction and Nonparametric regression
# Source: CH10 Prediction.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Example with training and test data in Python
# Textbook context: Section: Training data, test data and cross-validation
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

df = pd.read_csv("apartment_price_data.csv")
df = df[["price", "living_area"]].dropna().copy()

# ------------------------------------------------------------------------------
# Box 02: Example with training and test data in Python
# Textbook context: Section: Training data, test data and cross-validation
# ------------------------------------------------------------------------------

for i in range(2, 11):
    df[f"living_area{i}"] = df["living_area"] ** i

# ------------------------------------------------------------------------------
# Box 03: Example with training and test data in Python
# Textbook context: Section: Training data, test data and cross-validation
# ------------------------------------------------------------------------------

rng = np.random.default_rng(12)

n = len(df)
train_share = 0.8

train_ind = rng.choice(n, size=int(train_share * n), replace=False)
test_ind = np.setdiff1d(np.arange(n), train_ind)

df_train = df.iloc[train_ind].copy()
df_test = df.iloc[test_ind].copy()

# ------------------------------------------------------------------------------
# Box 04: Example with training and test data in Python
# Textbook context: Section: Training data, test data and cross-validation
# ------------------------------------------------------------------------------

from sklearn.linear_model import LinearRegression

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# K=1 (only living_area)
features = ["living_area"]

ols_model = LinearRegression().fit(df_train[features], df_train["price"])

yhat_train = ols_model.predict(df_train[features])
yhat_test = ols_model.predict(df_test[features])

mse_train = mse(df_train["price"].to_numpy(), yhat_train)
mse_test = mse(df_test["price"].to_numpy(), yhat_test)

mse_train_list = [mse_train]
mse_test_list = [mse_test]

# ------------------------------------------------------------------------------
# Box 05: Example with training and test data in Python
# Textbook context: Section: Training data, test data and cross-validation
# ------------------------------------------------------------------------------

for i in range(2, 11):
    features = features + [f"living_area{i}"]

    ols_model = LinearRegression().fit(df_train[features], df_train["price"])
    yhat_train = ols_model.predict(df_train[features])
    yhat_test = ols_model.predict(df_test[features])

    mse_train_list.append(mse(df_train["price"].to_numpy(), yhat_train))
    mse_test_list.append(mse(df_test["price"].to_numpy(), yhat_test))

results = pd.DataFrame(
    {
        "Number of polynomials": np.arange(1, 11),
        "MSE_train": mse_train_list,
        "MSE_test": mse_test_list,
    }
)

results

# ------------------------------------------------------------------------------
# Box 06: Cross-validation in Python
# Textbook context: Section: Training data, test data and cross-validation | Subsection: Cross-validation
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

df = pd.read_csv("apartment_price_data.csv")
df = df[["price", "living_area"]].dropna().copy()

X = df[["living_area"]].to_numpy()
y = df["price"].to_numpy()

# ------------------------------------------------------------------------------
# Box 07: Cross-validation in Python
# Textbook context: Section: Training data, test data and cross-validation | Subsection: Cross-validation
# ------------------------------------------------------------------------------

m = 5
kf = KFold(n_splits=m, shuffle=True, random_state=12)

MSE_hat = np.empty(m)

for j, (train_idx, test_idx) in enumerate(kf.split(X)):
    model = LinearRegression().fit(X[train_idx], y[train_idx])
    pred = model.predict(X[test_idx])
    MSE_hat[j] = np.mean((y[test_idx] - pred) ** 2)

MSE_hat, MSE_hat.mean()

# ------------------------------------------------------------------------------
# Box 08: Ridge and lasso in Python
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

df = pd.read_csv("apartment_price_data.csv")
df = df.dropna().copy()

y = df["price"].to_numpy()

dfX = df.drop(columns=["price"])

# ------------------------------------------------------------------------------
# Box 09: Ridge and lasso in Python
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

X_df = pd.get_dummies(
    dfX,
    columns=["build_year", "number_of_rooms"],
    drop_first=False  # glmnet/makeX also keeps many dummies; we let the model handle the intercept
)

X = X_df.to_numpy()

# ------------------------------------------------------------------------------
# Box 10: Ridge and lasso in Python
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

ridge_model = make_pipeline(
    StandardScaler(),
    Ridge(alpha=0.1)
).fit(X, y)

yhat = ridge_model.predict(X)

# ------------------------------------------------------------------------------
# Box 11: Ridge and lasso in Python
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

from sklearn.linear_model import RidgeCV

alphas = np.logspace(-4, 4, 100)

ridge_model_cv = make_pipeline(
    StandardScaler(),
    RidgeCV(alphas=alphas, cv=5)
).fit(X, y)

best_alpha_ridge = ridge_model_cv.named_steps["ridgecv"].alpha_
best_alpha_ridge

# ------------------------------------------------------------------------------
# Box 12: Ridge and lasso in Python
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

from sklearn.linear_model import LassoCV

lasso_model_cv = make_pipeline(
    StandardScaler(),
    LassoCV(alphas=alphas, cv=5, max_iter=100000)
).fit(X, y)

best_alpha_lasso = lasso_model_cv.named_steps["lassocv"].alpha_
best_alpha_lasso

# ------------------------------------------------------------------------------
# Box 13: Ridge and lasso in Python
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

ridge_coefs = ridge_model_cv.named_steps["ridgecv"].coef_
lasso_coefs = lasso_model_cv.named_steps["lassocv"].coef_

coef_table = pd.DataFrame(
    {"ridge": ridge_coefs, "lasso": lasso_coefs},
    index=X_df.columns
)

coef_table.head()

# ------------------------------------------------------------------------------
# Box 14: Regression tree in Python
# Textbook context: Section: Tree-based regression models
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("apartment_price_data.csv")
df = df[["price", "living_area", "monthly_fee"]].dropna().copy()

X = df[["living_area", "monthly_fee"]].to_numpy()
y = df["price"].to_numpy()

tree_model = DecisionTreeRegressor(
    min_samples_split=20,
    min_samples_leaf=5,
    ccp_alpha=0.0,
    random_state=12
).fit(X, y)

tree_model.get_n_leaves()

# ------------------------------------------------------------------------------
# Box 15: Regression tree in Python
# Textbook context: Section: Tree-based regression models
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(12, 6))
plot_tree(tree_model, feature_names=["living_area", "monthly_fee"], filled=False)
plt.show()

# ------------------------------------------------------------------------------
# Box 16: Regression tree in Python
# Textbook context: Section: Tree-based regression models
# ------------------------------------------------------------------------------

from sklearn.model_selection import KFold, cross_val_score

path = tree_model.cost_complexity_pruning_path(X, y)
ccp_alphas = path.ccp_alphas

cv = KFold(n_splits=5, shuffle=True, random_state=12)

mse_list = []
for a in ccp_alphas:
    t = DecisionTreeRegressor(
        min_samples_split=20,
        min_samples_leaf=5,
        ccp_alpha=a,
        random_state=12
    )
    # cross_val_score returns negative MSE when using "neg_mean_squared_error"
    mse_cv = -cross_val_score(t, X, y, cv=cv, scoring="neg_mean_squared_error").mean()
    mse_list.append(mse_cv)

mse_list = np.array(mse_list)
best_alpha = ccp_alphas[np.argmin(mse_list)]
best_alpha

# ------------------------------------------------------------------------------
# Box 17: Regression tree in Python
# Textbook context: Section: Tree-based regression models
# ------------------------------------------------------------------------------

pruned_tree = DecisionTreeRegressor(
    min_samples_split=20,
    min_samples_leaf=5,
    ccp_alpha=best_alpha,
    random_state=12
).fit(X, y)

pruned_tree.get_n_leaves()

# ------------------------------------------------------------------------------
# Box 18: Comparison of the different prediction models in Python
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

df = pd.read_csv("apartment_price_data.csv")

df["elevator_missing"] = df["elevator"].isna().astype(int)
df["elevator"] = df["elevator"].fillna(0)

df["living_area2"] = df["living_area"] ** 2
df["monthly_fee2"] = df["monthly_fee"] ** 2

# listwise deletion (after handling elevator missingness)
df = df.dropna().copy()

# ------------------------------------------------------------------------------
# Box 19: Comparison of the different prediction models in Python
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

for room_size in range(2, 7):
    df[f"room_size_{room_size}"] = (df["number_of_rooms"] == room_size).astype(int)
    df[f"city_area_room_size_{room_size}"] = df["city_area"] * df[f"room_size_{room_size}"]

# ------------------------------------------------------------------------------
# Box 20: Comparison of the different prediction models in Python
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

# --- decade dummies (reference: < 1900) ---
year_list10 = list(range(1900, 2011, 10))
for year in year_list10:
    name = f"build_decade_{year}"
    df[name] = ((df["build_year"] >= year) & (df["build_year"] <= year + 9)).astype(int)
    df[f"city_area_build_decade_{year}"] = df["city_area"] * df[name]

# --- year dummies (omit one year as reference to avoid perfect collinearity) ---
year_list1 = sorted(df["build_year"].unique())
ref_year = year_list1[0]

for year in year_list1:
    if year == ref_year:
        continue
    name = f"build_year_{year}"
    df[name] = (df["build_year"] == year).astype(int)
    df[f"city_area_build_year_{year}"] = df["city_area"] * df[name]

# ------------------------------------------------------------------------------
# Box 21: Comparison of the different prediction models in Python
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

room_vars = [c for c in df.columns if c.startswith("room_size_") or c.startswith("city_area_room_size_")]

build_decade_vars = [c for c in df.columns if c.startswith("build_decade_") or c.startswith("city_area_build_decade_")]
build_year_vars = [c for c in df.columns if c.startswith("build_year_") or c.startswith("city_area_build_year_")]

rest_vars = [
    "living_area", "new_production", "monthly_fee", "city_area", "elevator",
    "elevator_missing", "living_area2", "monthly_fee2"
]

tree_vars = [
    "living_area", "new_production", "monthly_fee", "city_area",
    "elevator", "number_of_rooms", "build_year"
]

varlist_model1 = room_vars + build_year_vars + rest_vars      # (1): year dummies
varlist_model10 = room_vars + build_decade_vars + rest_vars   # (10): decade dummies

X1 = df[varlist_model1].to_numpy()
X10 = df[varlist_model10].to_numpy()
Xtree = df[tree_vars].to_numpy()

Y = df["price"].to_numpy()

# ------------------------------------------------------------------------------
# Box 22: Comparison of the different prediction models in Python
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

rng = np.random.default_rng(12)

n = len(df)
ind_train = rng.choice(n, size=int((4/5) * n), replace=False)
ind_test = np.setdiff1d(np.arange(n), ind_train)

# ------------------------------------------------------------------------------
# Box 23: Comparison of the different prediction models in Python
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

alphas = np.logspace(-4, 4, 100)

# --- (1): year-dummy model ---
ols_model1 = LinearRegression().fit(X1[ind_train, :], Y[ind_train])

ridge_model1 = make_pipeline(
    StandardScaler(),
    RidgeCV(alphas=alphas, cv=5)
).fit(X1[ind_train, :], Y[ind_train])

lasso_model1 = make_pipeline(
    StandardScaler(),
    LassoCV(alphas=alphas, cv=5, max_iter=200000)
).fit(X1[ind_train, :], Y[ind_train])

# --- (10): decade-dummy model ---
ols_model10 = LinearRegression().fit(X10[ind_train, :], Y[ind_train])

ridge_model10 = make_pipeline(
    StandardScaler(),
    RidgeCV(alphas=alphas, cv=5)
).fit(X10[ind_train, :], Y[ind_train])

lasso_model10 = make_pipeline(
    StandardScaler(),
    LassoCV(alphas=alphas, cv=5, max_iter=200000)
).fit(X10[ind_train, :], Y[ind_train])

# ------------------------------------------------------------------------------
# Box 24: Comparison of the different prediction models in Python
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import KFold, cross_val_score

tree0 = DecisionTreeRegressor(
    min_samples_split=20,
    min_samples_leaf=5,
    ccp_alpha=0.0,
    random_state=12
).fit(Xtree[ind_train, :], Y[ind_train])

path = tree0.cost_complexity_pruning_path(Xtree[ind_train, :], Y[ind_train])
ccp_alphas = path.ccp_alphas

cv = KFold(n_splits=5, shuffle=True, random_state=12)

mse_list = []
for a in ccp_alphas:
    t = DecisionTreeRegressor(
        min_samples_split=20,
        min_samples_leaf=5,
        ccp_alpha=a,
        random_state=12
    )
    mse_cv = -cross_val_score(
        t, Xtree[ind_train, :], Y[ind_train],
        cv=cv, scoring="neg_mean_squared_error"
    ).mean()
    mse_list.append(mse_cv)

best_alpha = ccp_alphas[int(np.argmin(mse_list))]

pruned_tree = DecisionTreeRegressor(
    min_samples_split=20,
    min_samples_leaf=5,
    ccp_alpha=best_alpha,
    random_state=12
).fit(Xtree[ind_train, :], Y[ind_train])

# ------------------------------------------------------------------------------
# Box 25: Comparison of the different prediction models in Python
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

yhat_ols1 = ols_model1.predict(X1)
yhat_ridge1 = ridge_model1.predict(X1)
yhat_lasso1 = lasso_model1.predict(X1)

yhat_ols10 = ols_model10.predict(X10)
yhat_ridge10 = ridge_model10.predict(X10)
yhat_lasso10 = lasso_model10.predict(X10)

yhat_tree = pruned_tree.predict(Xtree)

YHAT_models = [
    yhat_ols1, yhat_ridge1, yhat_lasso1,
    yhat_ols10, yhat_ridge10, yhat_lasso10,
    yhat_tree
]

model_names = [
    "OLS (1)", "Ridge (1)", "Lasso (1)",
    "OLS (10)", "Ridge (10)", "Lasso (10)",
    "CART"
]

MSE_train = []
MSE_test = []

for yhat in YHAT_models:
    MSE_train.append(mse(Y[ind_train], yhat[ind_train]))
    MSE_test.append(mse(Y[ind_test], yhat[ind_test]))

pd.DataFrame({"Model": model_names, "MSE_train": MSE_train, "MSE_test": MSE_test})
