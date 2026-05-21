# Chapter 02, R box 03: Regression in R
# Source label: box:ols
# Full runnable chapter script: ../chapter02.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
beta_1_hat <- s_xy / s_x2
beta_0_hat <- ybar - xbar * beta_1_hat

ols_model <- lm(price ~ living_area, data = df)
coef(ols_model)
summary(ols_model)$r.squared
