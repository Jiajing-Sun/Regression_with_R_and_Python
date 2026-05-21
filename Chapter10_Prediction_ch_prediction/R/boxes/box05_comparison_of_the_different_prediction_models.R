# Chapter 10, R box 05: Comparison of the different prediction models
# Source label: box:prediction_comparison
# Full runnable chapter script: ../chapter10.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages(c("glmnet", "rpart"))  # run once if needed
# --- Code block 2 ---
library(glmnet)
library(rpart)
df <- read.csv(file.path("data", "apartment_price_data.csv"))
# The full script creates room, construction-year/decade,
# missing-value, polynomial, and interaction variables.
X1 <- as.matrix(df[, varlist_model1])
X10 <- as.matrix(df[, varlist_model10])
Y <- df$price

set.seed(12)
ind_train <- sample(1:nrow(df), 4/5 * nrow(df), replace = FALSE)
ind_test <- setdiff(1:nrow(df), ind_train)

models <- list(
  ols1 = lm(formOLS1, data = df[ind_train, ]),
  ridge1 = cv.glmnet(X1[ind_train, ], Y[ind_train], alpha = 0),
  lasso1 = cv.glmnet(X1[ind_train, ], Y[ind_train], alpha = 1),
  tree = rpart(formCART, data = df[ind_train, ])
)
# --- Code block 3 ---
mse <- function(y, yhat) mean((y - yhat)^2)
MSE_train <- c(ols1 = mse(Y[ind_train], yhat_ols1_train),
               ridge1 = mse(Y[ind_train], yhat_ridge1_train))
MSE_test <- c(ols1 = mse(Y[ind_test], yhat_ols1_test),
              ridge1 = mse(Y[ind_test], yhat_ridge1_test))
