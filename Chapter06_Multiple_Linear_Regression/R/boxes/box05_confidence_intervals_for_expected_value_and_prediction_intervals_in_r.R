# Chapter 06, R box 05: Confidence intervals for expected value and prediction intervals in R
# Source label: box:ci_pi
# Full runnable chapter script: ../chapter06.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
ols_model <- lm(price ~ living_area, data = df)
new80 <- data.frame(living_area = 80)

predict(ols_model, newdata = new80, interval = "confidence", level = 0.95)
predict(ols_model, newdata = new80, interval = "prediction", level = 0.95)
# --- Code block 2 ---
ols_model2 <- lm(price ~ living_area + monthly_fee + new_production, data = df)
eval_df <- data.frame(living_area = 80, monthly_fee = 3000, new_production = 1)
predict(ols_model2, newdata = eval_df, interval = "prediction", level = 0.95)
