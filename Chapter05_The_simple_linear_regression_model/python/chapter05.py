# Extracted Python code for Chapter 05: The simple linear regression model
# Source: CH5 Simple linear regression.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Inference for regression in Python
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

import numpy as np
from scipy import stats

n = len(df)  # df should already be filtered to remove missing values on both variables

s2_epsilon = RSS / (n - 2)  # s_U^2 = RSS/(n-2)
SSX = ((df["living_area"] - df["living_area"].mean()) ** 2).sum()

var_hat_beta_1_hat = s2_epsilon / SSX
se_beta_1_hat = np.sqrt(var_hat_beta_1_hat)

# ------------------------------------------------------------------------------
# Box 02: Inference for regression in Python
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

beta_1_H0 = 0

t_stat = (beta_1_hat - beta_1_H0) / se_beta_1_hat
p_val = 2 * stats.t.sf(np.abs(t_stat), df=n-2)   # two-sided p-value

# ------------------------------------------------------------------------------
# Box 03: Inference for regression in Python
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

alpha = 0.10  # 90% confidence interval
t_crit = stats.t.ppf(1 - alpha/2, df=n-2)

lb = beta_1_hat - t_crit * se_beta_1_hat
ub = beta_1_hat + t_crit * se_beta_1_hat

# ------------------------------------------------------------------------------
# Box 04: Inference for regression in Python
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

import statsmodels.formula.api as smf

ols_model = smf.ols("price ~ living_area", data=df).fit()
print(ols_model.summary())

# ------------------------------------------------------------------------------
# Box 05: Inference for regression in Python
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

beta1_hat_sm = ols_model.params["living_area"]
se_beta1_hat_sm = ols_model.bse["living_area"]
t_beta1_sm = ols_model.tvalues["living_area"]
p_beta1_sm = ols_model.pvalues["living_area"]

ci_beta1_sm = ols_model.conf_int(alpha=0.10).loc["living_area"]  # 90% CI

# ------------------------------------------------------------------------------
# Box 06: Inference for regression in Python
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

# If new_production is coded 0/1, this is fine as-is.
# If it is a string/categorical variable (e.g. "Yes"/"No"), use: "price ~ C(new_production)"
ols_model2 = smf.ols("price ~ new_production", data=df).fit()
print(ols_model2.summary())

ci_model2_90 = ols_model2.conf_int(alpha=0.10)  # 90% CI for both coefficients

# ------------------------------------------------------------------------------
# Box 07: Robust inference in Python
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

import numpy as np
from scipy import stats

dx2 = (df["living_area"] - df["living_area"].mean()) ** 2

var_beta_1_hat_r = (dx2 * (u_hat ** 2)).sum() / (dx2.sum() ** 2)
se_beta_1_hat_r = np.sqrt(var_beta_1_hat_r)

# ------------------------------------------------------------------------------
# Box 08: Robust inference in Python
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

alpha = 0.10
t_crit = stats.t.ppf(1 - alpha/2, df=n-2)

lb_r = beta_1_hat - t_crit * se_beta_1_hat_r
ub_r = beta_1_hat + t_crit * se_beta_1_hat_r

# ------------------------------------------------------------------------------
# Box 09: Robust inference in Python
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

import statsmodels.formula.api as smf

ols_model = smf.ols("price ~ living_area", data=df).fit()

# robust (Eicker-Huber-White / "sandwich") covariance, HC0
ols_model_hc0 = ols_model.get_robustcov_results(cov_type="HC0")
print(ols_model_hc0.summary())

# ------------------------------------------------------------------------------
# Box 10: Robust inference in Python
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

# find the position of "living_area" in the parameter vector
names = ols_model.model.exog_names
j = names.index("living_area")

beta1_hat_hc0 = ols_model_hc0.params[j]
se_beta1_hat_hc0 = ols_model_hc0.bse[j]
t_beta1_hc0 = ols_model_hc0.tvalues[j]
p_beta1_hc0 = ols_model_hc0.pvalues[j]

ci_hc0 = ols_model_hc0.conf_int(alpha=0.10)[j, :]   # 90% CI for beta_1

# ------------------------------------------------------------------------------
# Box 11: Data generating process and Monte Carlo simulations in Python
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()  # optional: np.random.default_rng(123)

nr_samples = 10000
n = 30

tstat_dist = np.empty(nr_samples)

for i in range(nr_samples):
    X = rng.uniform(0, 1, size=n)
    E = rng.chisquare(df=1, size=n)
    Y = 0.3 + 0.2 * X * E

    xbar = X.mean()
    ybar = Y.mean()

    SXX = ((X - xbar) ** 2).sum()
    SXY = ((X - xbar) * (Y - ybar)).sum()

    beta1_hat = SXY / SXX
    beta0_hat = ybar - beta1_hat * xbar

    u_hat = Y - (beta0_hat + beta1_hat * X)
    RSS = (u_hat ** 2).sum()

    s2_epsilon = RSS / (n - 2)
    se_beta1_hat = np.sqrt(s2_epsilon / SXX)

    tstat_dist[i] = (beta1_hat - 0.2) / se_beta1_hat

    # optional progress indicator:
    # if (i + 1) % 1000 == 0:
    #     print(i + 1)

tstat_dist.mean()
tstat_dist.var(ddof=1)

plt.hist(tstat_dist, bins=100)
plt.show()

# ------------------------------------------------------------------------------
# Box 12: Data generating process and Monte Carlo simulations in Python
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

var_beta1_r = (((X - xbar) ** 2) * (u_hat ** 2)).sum() / (SXX ** 2)
se_beta1_hat_r = np.sqrt(var_beta1_r)

tstat_dist[i] = (beta1_hat - 0.2) / se_beta1_hat_r
