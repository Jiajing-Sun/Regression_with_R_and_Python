# Extracted Python code for Chapter 02: Covariation in data
# Source: CH2 Covariation in data.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Calculation of correlation in Python
# Source lines: CH2 Covariation in data.tex:130-133
# ------------------------------------------------------------------------------

import pandas as pd
import numpy as np

df = pd.read_csv("apartment_price_data.csv")

# ------------------------------------------------------------------------------
# Box 02: Calculation of correlation in Python
# Source lines: CH2 Covariation in data.tex:137-138
# ------------------------------------------------------------------------------

mask = df["price"].notna() & df["living_area"].notna()
df = df.loc[mask].copy()

# ------------------------------------------------------------------------------
# Box 03: Calculation of correlation in Python
# Source lines: CH2 Covariation in data.tex:142-144
# ------------------------------------------------------------------------------

xbar = df["living_area"].mean()
ybar = df["price"].mean()
n = len(df)

# ------------------------------------------------------------------------------
# Box 04: Calculation of correlation in Python
# Source lines: CH2 Covariation in data.tex:148-148
# ------------------------------------------------------------------------------

s_xy = ((df["living_area"] - xbar) * (df["price"] - ybar)).sum() / (n - 1)

# ------------------------------------------------------------------------------
# Box 05: Calculation of correlation in Python
# Source lines: CH2 Covariation in data.tex:152-153
# ------------------------------------------------------------------------------

s_x2 = ((df["living_area"] - xbar) ** 2).sum() / (n - 1)
s_y2 = ((df["price"] - ybar) ** 2).sum() / (n - 1)

# ------------------------------------------------------------------------------
# Box 06: Calculation of correlation in Python
# Source lines: CH2 Covariation in data.tex:157-157
# ------------------------------------------------------------------------------

corr_xy = s_xy / (np.sqrt(s_x2) * np.sqrt(s_y2))

# ------------------------------------------------------------------------------
# Box 07: Calculation of correlation in Python
# Source lines: CH2 Covariation in data.tex:161-161
# ------------------------------------------------------------------------------

corr_xy = df["living_area"].corr(df["price"], method="pearson")

# ------------------------------------------------------------------------------
# Box 08: Calculation of correlation in Python
# Source lines: CH2 Covariation in data.tex:165-167
# ------------------------------------------------------------------------------

corr_xy = df["living_area"].cov(df["price"]) / (
    df["living_area"].std(ddof=1) * df["price"].std(ddof=1)
)

# ------------------------------------------------------------------------------
# Box 09: Calculation of Spearman's correlation in Python
# Source lines: CH2 Covariation in data.tex:245-246
# ------------------------------------------------------------------------------

df["Rx"] = df["living_area"].rank(method="average")
df["Ry"] = df["price"].rank(method="average")

# ------------------------------------------------------------------------------
# Box 10: Calculation of Spearman's correlation in Python
# Source lines: CH2 Covariation in data.tex:250-251
# ------------------------------------------------------------------------------

mean_Rx = (n + 1) / 2
mean_Ry = (n + 1) / 2

# ------------------------------------------------------------------------------
# Box 11: Calculation of Spearman's correlation in Python
# Source lines: CH2 Covariation in data.tex:255-257
# ------------------------------------------------------------------------------

covRxRy = ((df["Rx"] - mean_Rx) * (df["Ry"] - mean_Ry)).sum() / (n - 1)
sRx = np.sqrt(((df["Rx"] - mean_Rx) ** 2).sum() / (n - 1))
sRy = np.sqrt(((df["Ry"] - mean_Ry) ** 2).sum() / (n - 1))

# ------------------------------------------------------------------------------
# Box 12: Calculation of Spearman's correlation in Python
# Source lines: CH2 Covariation in data.tex:261-261
# ------------------------------------------------------------------------------

rS = covRxRy / (sRx * sRy)

# ------------------------------------------------------------------------------
# Box 13: Calculation of Spearman's correlation in Python
# Source lines: CH2 Covariation in data.tex:265-265
# ------------------------------------------------------------------------------

rS_alt = df["living_area"].corr(df["price"], method="spearman")

# ------------------------------------------------------------------------------
# Box 14: Calculation of Spearman's correlation in Python
# Source lines: CH2 Covariation in data.tex:270-273
# ------------------------------------------------------------------------------

df_sub = df[df["price"] <= 10]

pearson_sub = df_sub["living_area"].corr(df_sub["price"], method="pearson")
spearman_sub = df_sub["living_area"].corr(df_sub["price"], method="spearman")

# ------------------------------------------------------------------------------
# Box 15: Regression in Python
# Source lines: CH2 Covariation in data.tex:486-487
# ------------------------------------------------------------------------------

beta_1_hat = s_xy / s_x2
beta_0_hat = ybar - xbar * beta_1_hat

# ------------------------------------------------------------------------------
# Box 16: Regression in Python
# Source lines: CH2 Covariation in data.tex:491-491
# ------------------------------------------------------------------------------

y_hat = beta_0_hat + beta_1_hat * df["living_area"]

# ------------------------------------------------------------------------------
# Box 17: Regression in Python
# Source lines: CH2 Covariation in data.tex:495-495
# ------------------------------------------------------------------------------

u_hat = df["price"] - y_hat

# ------------------------------------------------------------------------------
# Box 18: Regression in Python
# Source lines: CH2 Covariation in data.tex:499-501
# ------------------------------------------------------------------------------

RSS = (u_hat ** 2).sum()
TSS = ((df["price"] - ybar) ** 2).sum()
R2 = 1 - RSS / TSS

# ------------------------------------------------------------------------------
# Box 19: Regression in Python
# Source lines: CH2 Covariation in data.tex:505-507
# ------------------------------------------------------------------------------

import statsmodels.formula.api as smf

ols_model = smf.ols("price ~ living_area", data=df).fit()

# ------------------------------------------------------------------------------
# Box 20: Regression in Python
# Source lines: CH2 Covariation in data.tex:511-511
# ------------------------------------------------------------------------------

print(ols_model.summary())

# ------------------------------------------------------------------------------
# Box 21: Regression in Python
# Source lines: CH2 Covariation in data.tex:515-518
# ------------------------------------------------------------------------------

coefs = ols_model.params
y_hat_sm = ols_model.predict(df)
u_hat_sm = ols_model.resid
R2_sm = ols_model.rsquared
