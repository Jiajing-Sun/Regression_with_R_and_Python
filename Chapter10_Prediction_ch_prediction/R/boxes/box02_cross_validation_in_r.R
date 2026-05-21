# Chapter 10, R box 02: Cross-validation in R
# Source label: box:crossval
# Full runnable chapter script: ../chapter10.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
df <- read.csv(file.path("data", "apartment_price_data.csv"))
set.seed(12)
n <- nrow(df)
m <- 5
fold_id <- sample(rep(1:m, length.out = n))
MSE_hat <- rep(NA, m)

for (i in 1:m) {
  train_df <- df[fold_id != i, ]
  test_df <- df[fold_id == i, ]
  ols_train <- lm(price ~ living_area, data = train_df)
  pred <- predict(ols_train, newdata = test_df)
  MSE_hat[i] <- mean((test_df$price - pred)^2)
}
mean(MSE_hat)
