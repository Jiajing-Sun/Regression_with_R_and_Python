# Chapter 06, R box 04: Robust $F$-test in R
# Source label: box:f_test_robust
# Full runnable chapter script: ../chapter06.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages(c("lmtest", "sandwich"))  # run once if needed
# --- Code block 2 ---
library(lmtest)
library(sandwich)

waldtest(ols_model_s, ols_model_l,
         vcov = vcovHC(ols_model_l, type = "HC0"))
