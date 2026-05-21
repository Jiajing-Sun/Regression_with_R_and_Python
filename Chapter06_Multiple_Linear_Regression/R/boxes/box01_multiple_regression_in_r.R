# Chapter 06, R box 01: Multiple regression in R
# Source label: box:mult_reg
# Full runnable chapter script: ../chapter06.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages(c("lmtest", "sandwich"))  # run once if needed
# --- Code block 2 ---
library(lmtest)
library(sandwich)

df <- read.csv("apartment_price_data.csv")
ols_model <- lm(price ~ living_area + monthly_fee + new_production,
                data = df)

coeftest(ols_model, vcov = vcovHC(ols_model, type = "HC0"))
coefci(ols_model, vcov. = vcovHC(ols_model, type = "HC0"))
