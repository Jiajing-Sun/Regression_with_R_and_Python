# Extracted Python code for Chapter 06: Multiple Linear Regression
# Source: CH6 Multiple linear regression.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# Run from the chapter data directory when data/ exists, so printed paths such as
# "apartment_price_data.csv" work from the companion repository.
from pathlib import Path
import os as _os

_data_dir = Path(__file__).resolve().parents[1] / "data"
if _data_dir.exists():
    _os.chdir(_data_dir)

# ------------------------------------------------------------------------------
# Box 01: Multiple regression in Python
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("apartment_price_data.csv")

ols_model = smf.ols(
    "price ~ living_area + monthly_fee + new_production",
    data=df
).fit()

print(ols_model.summary())

# ------------------------------------------------------------------------------
# Box 02: Multiple regression in Python
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

ols_model_hc0 = ols_model.get_robustcov_results(cov_type="HC0", use_t=True)
print(ols_model_hc0.summary())

# ------------------------------------------------------------------------------
# Box 03: Multiple regression in Python
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

import numpy as np

coef_names = ols_model.model.exog_names

rob_table = pd.DataFrame(
    {
        "Estimate": ols_model_hc0.params,
        "Std. Error": ols_model_hc0.bse,
    },
    index=coef_names
)

rob_table

# ------------------------------------------------------------------------------
# Box 04: Multiple regression in Python
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

ci_95 = pd.DataFrame(
    ols_model_hc0.conf_int(alpha=0.05),
    columns=["2.5%", "97.5%"],
    index=coef_names
)

ci_95

# ------------------------------------------------------------------------------
# Box 05: Multiple regression in Python
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

from scipy import stats

b1 = rob_table.loc["living_area", "Estimate"]
se1 = rob_table.loc["living_area", "Std. Error"]

t_stat = (b1 - 0.04) / se1
df_resid = int(ols_model.df_resid)
p_value = 2 * stats.t.sf(np.abs(t_stat), df=df_resid)

# ------------------------------------------------------------------------------
# Box 06: Multiple regression in Python
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

ols_model_hc0.t_test("living_area = 0.04")

# ------------------------------------------------------------------------------
# Box 07: Added-variable plot in Python
# Textbook context: Section: Regression anatomy and partial regression plots | Subsection: Added-variable plots
# ------------------------------------------------------------------------------

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

df = pd.read_csv("apartment_price_data.csv")

res_y = smf.ols("price ~ monthly_fee", data=df).fit().resid
res_x = smf.ols("living_area ~ monthly_fee", data=df).fit().resid

av_df = pd.DataFrame({"res_y": res_y, "res_x": res_x})
av_model = smf.ols("res_y ~ res_x", data=av_df).fit()

multi_model = smf.ols(
    "price ~ living_area + monthly_fee", data=df
).fit()

print(av_model.params["res_x"])
print(multi_model.params["living_area"])

# ------------------------------------------------------------------------------
# Box 08: Added-variable plot in Python
# Textbook context: Section: Regression anatomy and partial regression plots | Subsection: Added-variable plots
# ------------------------------------------------------------------------------

plt.scatter(res_x, res_y, alpha=0.5)
plt.axline((0, av_model.params["Intercept"]),
           slope=av_model.params["res_x"])
plt.xlabel("Living area residuals")
plt.ylabel("Price residuals")
plt.show()

# ------------------------------------------------------------------------------
# Box 09: $F$-test in Python
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats

df = pd.read_csv("apartment_price_data.csv")

# keep complete cases for all variables in the full model
cols = ["price", "living_area", "monthly_fee", "new_production", "build_year"]
df_cc = df[cols].dropna()

n = len(df_cc)

# ------------------------------------------------------------------------------
# Box 10: $F$-test in Python
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

ols_model_l = smf.ols(
    "price ~ living_area + monthly_fee + new_production + build_year",
    data=df_cc
).fit()

ols_model_s = smf.ols(
    "price ~ living_area + monthly_fee",
    data=df_cc
).fit()

# ------------------------------------------------------------------------------
# Box 11: $F$-test in Python
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

RSS_l = np.sum(ols_model_l.resid ** 2)
RSS_s = np.sum(ols_model_s.resid ** 2)

K = int(ols_model_l.df_model)   # regressors in full model (excluding intercept)
G = int(ols_model_s.df_model)   # regressors in restricted model (excluding intercept)

F_obs = ((RSS_s - RSS_l) / (K - G)) / (RSS_l / (n - (K + 1)))
p_value = stats.f.sf(F_obs, dfn=K - G, dfd=n - (K + 1))

# ------------------------------------------------------------------------------
# Box 12: $F$-test in Python
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

F_sm, p_sm, df_diff = ols_model_l.compare_f_test(ols_model_s)

# ------------------------------------------------------------------------------
# Box 13: $F$-test in Python
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

F_overall = ols_model_l.fvalue
p_overall = ols_model_l.f_pvalue
df1 = int(ols_model_l.df_model)
df2 = int(ols_model_l.df_resid)

# ------------------------------------------------------------------------------
# Box 14: Robust $F$-test in Python
# Textbook context: Section: $F$-test | Subsection: Robust $F$-test
# ------------------------------------------------------------------------------

ols_model_l_hc0 = ols_model_l.get_robustcov_results(
    cov_type="HC0",
    use_t=True,
)

# ------------------------------------------------------------------------------
# Box 15: Robust $F$-test in Python
# Textbook context: Section: $F$-test | Subsection: Robust $F$-test
# ------------------------------------------------------------------------------

ftest_rob = ols_model_l_hc0.f_test(
    "new_production = 0, build_year = 0"
)

F_rob = float(ftest_rob.fvalue)
p_rob = float(ftest_rob.pvalue)

# ------------------------------------------------------------------------------
# Box 16: Confidence intervals for expected value and prediction intervals in Python
# Textbook context: Section: Uncertainty of the conditional expectation | Subsection: Prediction interval
# ------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats

df = pd.read_csv("apartment_price_data.csv")

# use the same observations as the regression (listwise deletion)
df_sr = df[["price", "living_area"]].dropna()

ols_model = smf.ols("price ~ living_area", data=df_sr).fit()

x0 = 80
yhat_x80 = float(ols_model.predict(pd.DataFrame({"living_area": [x0]}))[0])

n = int(ols_model.nobs)
RSS = np.sum(ols_model.resid ** 2)
s2_epsilon = RSS / (n - 2)

xbar = df_sr["living_area"].mean()
SSX = np.sum((df_sr["living_area"] - xbar) ** 2)

# var( Ehat(Y|X=x0) )
var_eY_x0 = s2_epsilon * (1 / n + (x0 - xbar) ** 2 / SSX)

alpha = 0.05
t_crit = stats.t.ppf(1 - alpha / 2, df=n - 2)

lb_ci = yhat_x80 - t_crit * np.sqrt(var_eY_x0)
ub_ci = yhat_x80 + t_crit * np.sqrt(var_eY_x0)

# var( prediction error | X=x0 )
var_pred_x0 = var_eY_x0 + s2_epsilon

lb_pi = yhat_x80 - t_crit * np.sqrt(var_pred_x0)
ub_pi = yhat_x80 + t_crit * np.sqrt(var_pred_x0)

# ------------------------------------------------------------------------------
# Box 17: Confidence intervals for expected value and prediction intervals in Python
# Textbook context: Section: Uncertainty of the conditional expectation | Subsection: Prediction interval
# ------------------------------------------------------------------------------

pred1 = ols_model.get_prediction(pd.DataFrame({"living_area": [x0]}))
pred1.summary_frame(alpha=0.05)

# ------------------------------------------------------------------------------
# Box 18: Confidence intervals for expected value and prediction intervals in Python
# Textbook context: Section: Uncertainty of the conditional expectation | Subsection: Prediction interval
# ------------------------------------------------------------------------------

df_mr = df[["price", "living_area", "monthly_fee", "new_production"]].dropna()

ols_model2 = smf.ols(
    "price ~ living_area + monthly_fee + new_production",
    data=df_mr
).fit()

eval_df = pd.DataFrame(
    {"living_area": [80], "monthly_fee": [3000], "new_production": [1]}
)

pred2 = ols_model2.get_prediction(eval_df)
pred2.summary_frame(alpha=0.05)
