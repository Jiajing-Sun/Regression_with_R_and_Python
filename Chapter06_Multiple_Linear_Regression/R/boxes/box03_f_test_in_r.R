# Chapter 06, R box 03: $F$-test in R
# Source label: box:f_test
# Full runnable chapter script: ../chapter06.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
vars <- c("price", "living_area", "monthly_fee", "new_production", "build_year")
df_cc <- df[complete.cases(df[, vars]), vars]

ols_model_l <- lm(price ~ living_area + monthly_fee + new_production + build_year,
                  data = df_cc)
ols_model_s <- lm(price ~ living_area + monthly_fee, data = df_cc)

anova(ols_model_s, ols_model_l)
summary(ols_model_l)$fstatistic
