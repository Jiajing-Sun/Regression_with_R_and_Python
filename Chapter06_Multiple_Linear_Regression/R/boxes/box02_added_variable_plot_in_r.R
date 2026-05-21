# Chapter 06, R box 02: Added-variable plot in R
# Source label: box:added_variable_r
# Full runnable chapter script: ../chapter06.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
df <- read.csv("apartment_price_data.csv")

res_y <- residuals(lm(price ~ monthly_fee, data = df))
res_x <- residuals(lm(living_area ~ monthly_fee, data = df))
av_model <- lm(res_y ~ res_x)

coef(av_model)["res_x"]
coef(lm(price ~ living_area + monthly_fee, data = df))["living_area"]
