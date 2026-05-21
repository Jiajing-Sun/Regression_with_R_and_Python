# Chapter 10, R box 01: Example with training and test data
# Source label: box:training_test
# Full runnable chapter script: ../chapter10.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
df <- read.csv(file.path("data", "apartment_price_data.csv"))
for (i in 2:10) {
  df[, paste0("living_area", i)] <- df$living_area^i
}

set.seed(12)
n <- nrow(df)
train_ind <- sample(1:n, .8 * n, replace = FALSE)
test_ind <- setdiff(1:n, train_ind)
df_train <- df[train_ind, ]
df_test <- df[test_ind, ]

ols_model <- lm(price ~ living_area, data = df_train)
yhat_train <- predict(ols_model)
yhat_test <- predict(ols_model, newdata = df_test)
c(train = mean((df_train$price - yhat_train)^2),
  test  = mean((df_test$price - yhat_test)^2))
