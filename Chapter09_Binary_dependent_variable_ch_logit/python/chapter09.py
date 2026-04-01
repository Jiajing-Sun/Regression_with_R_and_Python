# Extracted Python code for Chapter 09: Binary dependent variable
# Source: CH9 Binary dependent variable.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Logistic regression in Python
# Source lines: CH9 Binary dependent variable.tex:373-377
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

df = pd.read_csv("municip_data.csv")
df = df[df["year"] == 2022].copy()

# ------------------------------------------------------------------------------
# Box 02: Logistic regression in Python
# Source lines: CH9 Binary dependent variable.tex:381-381
# ------------------------------------------------------------------------------

highest_quartile_limit = df["tax_base"].quantile(0.75)

# ------------------------------------------------------------------------------
# Box 03: Logistic regression in Python
# Source lines: CH9 Binary dependent variable.tex:385-385
# ------------------------------------------------------------------------------

df["high_income"] = (df["tax_base"] > highest_quartile_limit).astype(int)

# ------------------------------------------------------------------------------
# Box 04: Logistic regression in Python
# Source lines: CH9 Binary dependent variable.tex:389-396
# ------------------------------------------------------------------------------

import statsmodels.api as sm
import statsmodels.formula.api as smf

logit_model = smf.glm(
    "high_income ~ share_tertiary_school",
    data=df,
    family=sm.families.Binomial(link=sm.families.links.logit())
).fit()

# ------------------------------------------------------------------------------
# Box 05: Logistic regression in Python
# Source lines: CH9 Binary dependent variable.tex:400-400
# ------------------------------------------------------------------------------

print(logit_model.summary())

# ------------------------------------------------------------------------------
# Box 06: Logistic regression in Python
# Source lines: CH9 Binary dependent variable.tex:404-412
# ------------------------------------------------------------------------------

df["lnpop"] = np.log(df["pop"])

logit_model2 = smf.glm(
    "high_income ~ share_tertiary_school + lnpop",
    data=df,
    family=sm.families.Binomial(link=sm.families.links.logit())
).fit()

print(logit_model2.summary())

# ------------------------------------------------------------------------------
# Box 07: Logistic regression in Python
# Source lines: CH9 Binary dependent variable.tex:416-417
# ------------------------------------------------------------------------------

beta1hat = float(logit_model2.params["share_tertiary_school"])
beta2hat = float(logit_model2.params["lnpop"])

# ------------------------------------------------------------------------------
# Box 08: Logistic regression in Python
# Source lines: CH9 Binary dependent variable.tex:421-422
# ------------------------------------------------------------------------------

odds_ratio_x1 = np.exp(beta1hat * 0.01)
odds_ratio_x1

# ------------------------------------------------------------------------------
# Box 09: Example in Python with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:612-625
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv("heart_disease.csv")

logit_model = smf.glm(
    "heart_disease ~ blood_pressure",
    data=df,
    family=sm.families.Binomial(link=sm.families.links.logit())
).fit()

print(logit_model.summary())

# ------------------------------------------------------------------------------
# Box 10: Example in Python with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:630-646
# ------------------------------------------------------------------------------

from scipy import stats

beta_1_hat = float(logit_model.params["blood_pressure"])
se_beta_1_hat = float(logit_model.bse["blood_pressure"])

std_dev_blood_pressure = float(df["blood_pressure"].std(ddof=1))

alpha = 0.05
zstat = stats.norm.ppf(1 - alpha/2)

lb_beta_1_hat = beta_1_hat - zstat * se_beta_1_hat
ub_beta_1_hat = beta_1_hat + zstat * se_beta_1_hat

lb_odds_ratio = np.exp(lb_beta_1_hat * std_dev_blood_pressure)
ub_odds_ratio = np.exp(ub_beta_1_hat * std_dev_blood_pressure)

print([lb_odds_ratio, ub_odds_ratio])

# ------------------------------------------------------------------------------
# Box 11: Example in Python with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:651-657
# ------------------------------------------------------------------------------

logit_model2 = smf.glm(
    "heart_disease ~ blood_pressure + male + age",
    data=df,
    family=sm.families.Binomial(link=sm.families.links.logit())
).fit()

print(logit_model2.summary())

# ------------------------------------------------------------------------------
# Box 12: Example in Python with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:662-672
# ------------------------------------------------------------------------------

beta_1_hat_b = float(logit_model2.params["blood_pressure"])
beta_2_hat_b = float(logit_model2.params["male"])
beta_3_hat_b = float(logit_model2.params["age"])

std_dev_age = float(df["age"].std(ddof=1))

odds_ratio_blood_pressure = np.exp(beta_1_hat_b * std_dev_blood_pressure)
odds_ratio_male = np.exp(beta_2_hat_b * 1)
odds_ratio_age = np.exp(beta_3_hat_b * std_dev_age)

odds_ratio_blood_pressure, odds_ratio_male, odds_ratio_age

# ------------------------------------------------------------------------------
# Box 13: Example in Python with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:677-681
# ------------------------------------------------------------------------------

beta_hat_b = logit_model2.params[["blood_pressure", "male", "age"]]
increases = np.array([std_dev_blood_pressure, 1, std_dev_age])

odds_ratios = np.exp(beta_hat_b.to_numpy() * increases)
odds_ratios

# ------------------------------------------------------------------------------
# Box 14: Example in Python with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:686-690
# ------------------------------------------------------------------------------

pred_heart_disease = logit_model2.predict(
    pd.DataFrame({"blood_pressure": [140], "male": [1], "age": [50]})
)[0]

pred_heart_disease

# ------------------------------------------------------------------------------
# Box 15: Example in Python with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:695-696
# ------------------------------------------------------------------------------

df = df.copy()
df["pred"] = logit_model2.predict(df)

# ------------------------------------------------------------------------------
# Box 16: Example in Python with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:700-710
# ------------------------------------------------------------------------------

df_incr_blood_pressure = df.copy()
df_incr_blood_pressure["blood_pressure"] = (
    df_incr_blood_pressure["blood_pressure"] + std_dev_blood_pressure
)
df_incr_blood_pressure["pred"] = logit_model2.predict(df_incr_blood_pressure)

df["risk_ratio_blood_pressure"] = df_incr_blood_pressure["pred"] / df["pred"]
df["risk_diff_blood_pressure"] = df_incr_blood_pressure["pred"] - df["pred"]

GRR_blood_pressure = float(df["risk_ratio_blood_pressure"].mean())
GRD_blood_pressure = float(df["risk_diff_blood_pressure"].mean())

# ------------------------------------------------------------------------------
# Box 17: Example in Python with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:714-722
# ------------------------------------------------------------------------------

df_incr_age = df.copy()
df_incr_age["age"] = df_incr_age["age"] + std_dev_age
df_incr_age["pred"] = logit_model2.predict(df_incr_age)

df["risk_ratio_age"] = df_incr_age["pred"] / df["pred"]
df["risk_diff_age"] = df_incr_age["pred"] - df["pred"]

GRR_age = float(df["risk_ratio_age"].mean())
GRD_age = float(df["risk_diff_age"].mean())

# ------------------------------------------------------------------------------
# Box 18: Example in Python with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:726-738
# ------------------------------------------------------------------------------

df_female = df.copy()
df_female["male"] = 0
pred_female = logit_model2.predict(df_female)

df_male = df.copy()
df_male["male"] = 1
pred_male = logit_model2.predict(df_male)

df["risk_ratio_male"] = pred_male / pred_female
df["risk_diff_male"] = pred_male - pred_female

GRR_male = float(df["risk_ratio_male"].mean())
GRD_male = float(df["risk_diff_male"].mean())
