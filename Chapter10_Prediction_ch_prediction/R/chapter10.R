# Extracted R code for Chapter 10: Prediction
# Source: CH10 Prediction.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Example with training and test data
# Textbook context: Section: Training data, test data and cross-validation
# ------------------------------------------------------------------------------

    set.seed(12)
    n <- nrow(df)
    train_share <- .8
    train_ind <- sample(1:n, train_share * n, replace=FALSE)
    test_ind <- setdiff(1:n, train_ind)
    df_train <- df[train_ind, ]
    df_test <- df[test_ind, ]

# ------------------------------------------------------------------------------
# Box 02: Ridge and lasso in R
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

 install.packages("glmnet")
 library(glmnet)

# ------------------------------------------------------------------------------
# Box 03: Ridge and lasso in R
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

  df <- read.csv("apartment_price_data.csv")
  df <- df[complete.cases(df), ]

# ------------------------------------------------------------------------------
# Box 04: Ridge and lasso in R
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

 dfX <- df[, names(df) != "price"]

# ------------------------------------------------------------------------------
# Box 05: Ridge and lasso in R
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

 X <- makeX(dfX)

# ------------------------------------------------------------------------------
# Box 06: Ridge and lasso in R
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

 yhat <- predict(ridge_model, newx = X)

# ------------------------------------------------------------------------------
# Box 07: Ridge and lasso in R
# Textbook context: Section: Predictions with many independent variables | Subsection: Scale dependence with ridge and lasso regression
# ------------------------------------------------------------------------------

 plot(ridge_model_cv)

# ------------------------------------------------------------------------------
# Box 08: Regression tree in R
# Textbook context: Section: Tree-based regression models
# ------------------------------------------------------------------------------

  install.packages("rpart")
  install.packages("rpart.plot")
  library(rpart)
  library(rpart.plot)

# ------------------------------------------------------------------------------
# Box 09: Regression tree in R
# Textbook context: Section: Tree-based regression models
# ------------------------------------------------------------------------------

 df <- read.csv("apartment_price_data.csv")

# ------------------------------------------------------------------------------
# Box 10: Regression tree in R
# Textbook context: Section: Tree-based regression models
# ------------------------------------------------------------------------------

 tree_model <- rpart(price ~ living_area + monthly_fee,
 data=df, control=rpart.control(
 minsplit = 20, minsbucket = 5, cp=0))

# ------------------------------------------------------------------------------
# Box 11: Regression tree in R
# Textbook context: Section: Tree-based regression models
# ------------------------------------------------------------------------------

  rpart.plot(tree_model)

# ------------------------------------------------------------------------------
# Box 12: Regression tree in R
# Textbook context: Section: Tree-based regression models
# ------------------------------------------------------------------------------

 pruned_tree <- prune(tree_model, cp=.03)

# ------------------------------------------------------------------------------
# Box 13: Regression tree in R
# Textbook context: Section: Tree-based regression models
# ------------------------------------------------------------------------------

 printcp(tree_model)

# ------------------------------------------------------------------------------
# Box 14: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

 year_list10 <- seq(from=1900, to=2010, by=10)

# ------------------------------------------------------------------------------
# Box 15: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

  room_vars <- ls(df, pat="^room_size_|^city_area_room_size_")

# ------------------------------------------------------------------------------
# Box 16: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

 build_decade_vars <- ls(df,
 pat="^build_decade_|^city_area_build_decade_")
 build_year_vars <- ls(df,
 pat="^build_year_|^city_area_build_year_")

# ------------------------------------------------------------------------------
# Box 17: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

  rest_vars <- c("living_area", "new_production",
                 "monthly_fee", "city_area", "elevator",
                 "elevator_missing", "living_area2",
                 "monthly_fee2")
  tree_vars <- c("living_area", "new_production",
                 "monthly_fee", "city_area", "elevator",
                 "number_of_rooms", "build_year")

# ------------------------------------------------------------------------------
# Box 18: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

 varlist_model1 <- c(room_vars, build_year_vars, rest_vars)
 varlist_model10 <- c(room_vars, build_decade_vars, rest_vars)

# ------------------------------------------------------------------------------
# Box 19: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

 formOLS1 <- paste(varlist_model1, collapse="+")
 formOLS1 <- paste("price ~ ", formOLS1)

# ------------------------------------------------------------------------------
# Box 20: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

  formOLS10 <- paste("price ~ ",
    paste(varlist_model10, collapse="+"))
  formCART <- paste("price ~ ",
    paste(tree_vars, collapse="+"))

# ------------------------------------------------------------------------------
# Box 21: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

 set.seed(12)
 n <- nrow(df)
 ind_train <- sample(1:n, 4/5 * n, replace=FALSE)
 ind_test <- setdiff(1:n, ind_train)

# ------------------------------------------------------------------------------
# Box 22: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

  ols_model1 <- lm(formOLS1, data=df[ind_train, ])
  ridge_model1 <- cv.glmnet(
    X1[ind_train, ], Y[ind_train], alpha=0)
  lasso_model1 <- cv.glmnet(
    X1[ind_train, ], Y[ind_train], alpha=1)

  ols_model10 <- lm(formOLS10, data=df[ind_train, ])
  ridge_model10 <- cv.glmnet(
    X10[ind_train, ], Y[ind_train], alpha=0)
  lasso_model10 <- cv.glmnet(
    X10[ind_train, ], Y[ind_train], alpha=1)

    CART_model = rpart(formCART, data=df[ind_train, ], 
                     control=rpart.control(
                      minsplit = 20, minbucket = 5, cp=0))
  c <- printcp(CART_model)
  s <- c[, "xerror"]
  alpha <- c[, "CP"][s == min(s)]
  pruned_tree <- prune(CART_model, cp=alpha)

# ------------------------------------------------------------------------------
# Box 23: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

  yhat_ols1 <- predict(ols_model1, newdata=df)
  yhat_ols10 <- predict(ols_model10, newdata=df)
  yhat_ridge1 <- predict(ridge_model1, newx=X1,
                         s="lambda.min")
  yhat_ridge10 <- predict(ridge_model10, newx=X10,
                          s="lambda.min")
  yhat_lasso1 <- predict(lasso_model1, newx=X1,
                         s="lambda.min")
  yhat_lasso10 <- predict(lasso_model10, newx=X10,
                          s="lambda.min")
  yhat_tree <- predict(pruned_tree, newdata = df)

# ------------------------------------------------------------------------------
# Box 24: Comparison of the different prediction models
# Textbook context: Section: Example: housing prices
# ------------------------------------------------------------------------------

 YHAT_models <- list(yhat_ols1, yhat_ridge1, yhat_lasso1,
 yhat_ols10, yhat_ridge10, yhat_lasso10,
 yhat_tree)
 MSE_train <- c()
 MSE_test <- c()
 for (yhat in YHAT_models) {
 mse_train <- mean((Y[ind_train] - yhat[ind_train])^2)
 mse_test <- mean((Y[ind_test] - yhat[ind_test])^2)
 MSE_train <- c(MSE_train, mse_train)
 MSE_test <- c(MSE_test, mse_test)
 }
