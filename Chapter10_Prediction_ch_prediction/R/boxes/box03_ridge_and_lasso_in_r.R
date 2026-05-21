# Chapter 10, R box 03: Ridge and lasso in R
# Source label: box:ridge_lasso
# Full runnable chapter script: ../chapter10.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages("glmnet")  # run once if needed
# --- Code block 2 ---
library(glmnet)
df <- read.csv(file.path("data", "apartment_price_data.csv"))
df <- df[complete.cases(df), ]

dfX <- df[, names(df) != "price"]
dfX$build_year <- as.factor(dfX$build_year)
dfX$number_of_rooms <- as.factor(dfX$number_of_rooms)
X <- makeX(dfX)

ridge_model_cv <- cv.glmnet(X, df$price, alpha = 0)
lasso_model_cv <- cv.glmnet(X, df$price, alpha = 1)
ridge_model_cv$lambda.min
lasso_model_cv$lambda.min
