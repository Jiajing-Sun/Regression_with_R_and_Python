# Chapter 05, R box 02: Robust inference in R
# Source label: box:inf_reg_robust
# Full runnable chapter script: ../chapter05.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages(c("lmtest", "sandwich"))  # run once if needed
# --- Code block 2 ---
library(lmtest)
library(sandwich)

ols_model <- lm(price ~ living_area, data = df)
coeftest(ols_model, vcov = vcovHC(ols_model, type = "HC0"))
