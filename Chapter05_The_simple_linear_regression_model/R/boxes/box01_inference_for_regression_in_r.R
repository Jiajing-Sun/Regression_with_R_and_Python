# Chapter 05, R box 01: Inference for regression in R
# Source label: box:inf_reg
# Full runnable chapter script: ../chapter05.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
ols_model <- lm(price ~ living_area, data = df)
reg_table <- summary(ols_model)$coefficients

beta1_hat <- reg_table["living_area", "Estimate"]
se_beta1 <- reg_table["living_area", "Std. Error"]
t_stat <- reg_table["living_area", "t value"]
p_value <- reg_table["living_area", "Pr(>|t|)"]

confint(ols_model, level = 0.90)
# --- Code block 2 ---
ols_model2 <- lm(price ~ new_production, data = df)
summary(ols_model2)$coefficients
confint(ols_model2, level = 0.90)
