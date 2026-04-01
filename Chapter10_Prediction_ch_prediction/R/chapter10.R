# Extracted R code for Chapter 10: Prediction and Nonparametric regression
# Source: CH10 Prediction.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Example with training and test data
# Source lines: CH10 Prediction.tex:154-163
# ------------------------------------------------------------------------------

 df <- read.csv("apartment_price_data.csv")
 df$living_area2 <- df$living_area^2
 df$living_area3 <- df$living_area^3
 df$living_area4 <- df$living_area^4
 df$living_area5 <- df$living_area^5
 df$living_area6 <- df$living_area^6
 df$living_area7 <- df$living_area^7
 df$living_area8 <- df$living_area^2
 df$living_area9 <- df$living_area^9
 df$living_area10 <- df$living_area^10

# ------------------------------------------------------------------------------
# Box 02: Example with training and test data
# Source lines: CH10 Prediction.tex:166-168
# ------------------------------------------------------------------------------

    for (i in 2:10) {
      df[, paste0("living_area", i)] <- df$living_area^i
    }

# ------------------------------------------------------------------------------
# Box 03: Example with training and test data
# Source lines: CH10 Prediction.tex:174-180
# ------------------------------------------------------------------------------

    set.seed(12)
    n <- nrow(df)
    train_share <- .8
    train_ind <- sample(1:n, train_share * n, replace=FALSE)
    test_ind <- setdiff(1:n, train_ind)
    df_train <- df[train_ind, ]
    df_test <- df[test_ind, ]

# ------------------------------------------------------------------------------
# Box 04: Example with training and test data
# Source lines: CH10 Prediction.tex:186-190
# ------------------------------------------------------------------------------

    ols_model <- lm(price ~ living_area, data=df_train)
    yhat_train <- predict(ols_model)
    yhat_test <- predict(ols_model, newdata=df_test)
    mse_train <- mean((df_train$price - yhat_train)^2)
    mse_test <- mean((df_test$price - yhat_test)^2)

# ------------------------------------------------------------------------------
# Box 05: Example with training and test data
# Source lines: CH10 Prediction.tex:194-206
# ------------------------------------------------------------------------------

    f <- "price ~ living_area"
    mse_train_list <- c(mse_train)
    mse_test_list <- c(mse_test)
    for (i in 2:10) {
      f <- paste0(f, " + living_area", i)
      ols_model <- lm(as.formula(f), data=df_train)
      yhat_train <- predict(ols_model)
      yhat_test <- predict(ols_model, newdata=df_test)
      mse_train_list <- append(mse_train_list, 
        mean((df_train$price - yhat_train)^2))
      mse_test_list <- append(mse_test_list,
        mean((df_test$price - yhat_test)^2))
    }

# ------------------------------------------------------------------------------
# Box 06: Cross-validation in R
# Source lines: CH10 Prediction.tex:337-352
# ------------------------------------------------------------------------------

    df <- read.csv("apartment_price_data.csv")
    n <- nrow(df)
    m <- 5
    shuffle_ind <- sample(1:n, n, replace=FALSE)
    fold_indexes <- cut(shuffle_ind, breaks=m, labels=FALSE)
    MSE_hat <- rep(NA, m)
    for (i in 1:m){
      leave_out_ind <- (1:n)[fold_indexes == i]
      leave_in_ind <- setdiff(1:n, leave_out_ind)
      train_df <- df[leave_in_ind, ]
      test_df <- df[leave_out_ind, ]
      ols_train <- lm(price ~ living_area, data=train_df)
      pred <- predict(ols_train, test_df)
      MSE_hat[i] <- mean((test_df$price - pred)^2)
    }
    mean(MSE_hat)

# ------------------------------------------------------------------------------
# Box 07: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:454-455
# ------------------------------------------------------------------------------

 install.packages("glmnet")
 library(glmnet)

# ------------------------------------------------------------------------------
# Box 08: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:459-460
# ------------------------------------------------------------------------------

  df <- read.csv("apartment_price_data.csv")
  df <- df[complete.cases(df), ]

# ------------------------------------------------------------------------------
# Box 09: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:464-464
# ------------------------------------------------------------------------------

 dfX <- df[, names(df) != "price"]

# ------------------------------------------------------------------------------
# Box 10: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:468-469
# ------------------------------------------------------------------------------

 dfX$build_year <- as.factor(dfX$build_year)
 dfX$number_of_rooms <- as.factor(dfX$number_of_rooms)

# ------------------------------------------------------------------------------
# Box 11: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:473-473
# ------------------------------------------------------------------------------

 X <- makeX(dfX)

# ------------------------------------------------------------------------------
# Box 12: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:479-479
# ------------------------------------------------------------------------------

  ridge_model <- glmnet(X, df$price, alpha=0)

# ------------------------------------------------------------------------------
# Box 13: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:483-483
# ------------------------------------------------------------------------------

 ridge_model <- glmnet(X, df$price, alpha=0, lambda=.1)

# ------------------------------------------------------------------------------
# Box 14: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:487-487
# ------------------------------------------------------------------------------

 yhat <- predict(ridge_model, newx = X)

# ------------------------------------------------------------------------------
# Box 15: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:491-491
# ------------------------------------------------------------------------------

  ridge_model_cv <- cv.glmnet(X, df$price, alpha=0)

# ------------------------------------------------------------------------------
# Box 16: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:495-495
# ------------------------------------------------------------------------------

 plot(ridge_model_cv)

# ------------------------------------------------------------------------------
# Box 17: Ridge and lasso in R
# Source lines: CH10 Prediction.tex:499-499
# ------------------------------------------------------------------------------

 lasso_model_cv <- cv.glmnet(X, df$price, alpha=1)

# ------------------------------------------------------------------------------
# Box 18: Regression tree in R
# Source lines: CH10 Prediction.tex:704-707
# ------------------------------------------------------------------------------

  install.packages("rpart")
  install.packages("rpart.plot")
  library(rpart)
  library(rpart.plot)

# ------------------------------------------------------------------------------
# Box 19: Regression tree in R
# Source lines: CH10 Prediction.tex:711-711
# ------------------------------------------------------------------------------

 df <- read.csv("apartment_price_data.csv")

# ------------------------------------------------------------------------------
# Box 20: Regression tree in R
# Source lines: CH10 Prediction.tex:715-717
# ------------------------------------------------------------------------------

 tree_model <- rpart(price ~ living_area + monthly_fee,
 data=df, control=rpart.control(
 minsplit = 20, minbucket = 5, cp=0))

# ------------------------------------------------------------------------------
# Box 21: Regression tree in R
# Source lines: CH10 Prediction.tex:721-721
# ------------------------------------------------------------------------------

  rpart.plot(tree_model)

# ------------------------------------------------------------------------------
# Box 22: Regression tree in R
# Source lines: CH10 Prediction.tex:725-725
# ------------------------------------------------------------------------------

 pruned_tree <- prune(tree_model, cp=.03)

# ------------------------------------------------------------------------------
# Box 23: Regression tree in R
# Source lines: CH10 Prediction.tex:729-729
# ------------------------------------------------------------------------------

 printcp(tree_model)

# ------------------------------------------------------------------------------
# Box 24: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:897-904
# ------------------------------------------------------------------------------

 library(glmnet)
 library(rpart)
 df <- read.csv("apartment_price_data.csv")
 df$elevator_missing <- ifelse(is.na(df$elevator), 1, 0)
 df$elevator[is.na(df$elevator)] <- 0
 df$living_area2 <- df$living_area^2
 df$monthly_fee2 <- df$monthly_fee^2
 df <- df[complete.cases(df), ]

# ------------------------------------------------------------------------------
# Box 25: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:908-914
# ------------------------------------------------------------------------------

  for (room_size in 2:6){
    df[, paste0("room_size_", room_size)] <- ifelse(
      df$number_of_rooms == room_size, 1, 0)
    df[, paste0("city_area_room_size_", room_size)] <- (
      df$city_area * 
      df[, paste0("room_size_", room_size)]) 
  }

# ------------------------------------------------------------------------------
# Box 26: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:918-918
# ------------------------------------------------------------------------------

 year_list10 <- seq(from=1900, to=2010, by=10)

# ------------------------------------------------------------------------------
# Box 27: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:926-932
# ------------------------------------------------------------------------------

  for (year in year_list10){
    df[, paste0("build_decade_", year)] <- ifelse(
      df$build_year >= year & df$build_year <= year + 9, 1, 0)
    df[, paste0("city_area_build_decade_", year)] <- (
      df$city_area * 
        df[, paste0("build_decade_", year)]) 
  }

# ------------------------------------------------------------------------------
# Box 28: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:936-943
# ------------------------------------------------------------------------------

 year_list1 <- unique(df$build_year)
 for (year in year_list1){
 df[, paste0("build_year_", year)] <- ifelse(
 df$build_year == year, 1, 0)
 df[, paste0("city_area_build_year_", year)] <- (
 df$city_area *
 df[, paste0("build_year_", year)])
 }

# ------------------------------------------------------------------------------
# Box 29: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:950-950
# ------------------------------------------------------------------------------

  room_vars <- grep("^room_size_|^city_area_room_size_", names(df), value=TRUE)

# ------------------------------------------------------------------------------
# Box 30: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:961-962
# ------------------------------------------------------------------------------

build_decade_vars <- grep("^build_decade_|^city_area_build_decade_", names(df), value=TRUE)
build_year_vars <- grep("^build_year_|^city_area_build_year_", names(df), value=TRUE)

# ------------------------------------------------------------------------------
# Box 31: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:966-972
# ------------------------------------------------------------------------------

  rest_vars <- c("living_area", "new_production",
                 "monthly_fee", "city_area", "elevator",
                 "elevator_missing", "living_area2",
                 "monthly_fee2")
  tree_vars <- c("living_area", "new_production",
                 "monthly_fee", "city_area", "elevator",
                 "number_of_rooms", "build_year")

# ------------------------------------------------------------------------------
# Box 32: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:976-977
# ------------------------------------------------------------------------------

 varlist_model1 <- c(room_vars, build_year_vars, rest_vars)
 varlist_model10 <- c(room_vars, build_decade_vars, rest_vars)

# ------------------------------------------------------------------------------
# Box 33: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:981-983
# ------------------------------------------------------------------------------

 X1 <- as.matrix(df[, varlist_model1])
 X10 <- as.matrix(df[, varlist_model10])
 Y <- df$price

# ------------------------------------------------------------------------------
# Box 34: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:987-988
# ------------------------------------------------------------------------------

 formOLS1 <- paste(varlist_model1, collapse="+")
 formOLS1 <- paste("price ~ ", formOLS1)

# ------------------------------------------------------------------------------
# Box 35: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:992-995
# ------------------------------------------------------------------------------

  formOLS10 <- paste("price ~ ",
    paste(varlist_model10, collapse="+"))
  formCART <- paste("price ~ ",
    paste(tree_vars, collapse="+"))

# ------------------------------------------------------------------------------
# Box 36: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:999-1002
# ------------------------------------------------------------------------------

 set.seed(12)
 n <- nrow(df)
 ind_train <- sample(1:n, 4/5 * n, replace=FALSE)
 ind_test <- setdiff(1:n, ind_train)

# ------------------------------------------------------------------------------
# Box 37: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:1006-1024
# ------------------------------------------------------------------------------

  ols_model1 <- lm(as.formula(formOLS1), data=df[ind_train, ])
  ridge_model1 <- cv.glmnet(
    X1[ind_train, ], Y[ind_train], alpha=0)
  lasso_model1 <- cv.glmnet(
    X1[ind_train, ], Y[ind_train], alpha=1)

  ols_model10 <- lm(as.formula(formOLS10), data=df[ind_train, ])
  ridge_model10 <- cv.glmnet(
    X10[ind_train, ], Y[ind_train], alpha=0)
  lasso_model10 <- cv.glmnet(
    X10[ind_train, ], Y[ind_train], alpha=1)

    CART_model = rpart(formCART, data=df[ind_train, ], 
                     control=rpart.control(
                      minsplit = 20, minbucket = 5, cp=0))
  c <- printcp(CART_model)
  s <- c[, "xerror"]
  alpha <- c[which.min(s), "CP"]
  pruned_tree <- prune(CART_model, cp=alpha)

# ------------------------------------------------------------------------------
# Box 38: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:1028-1038
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
# Box 39: Comparison of the different prediction models
# Source lines: CH10 Prediction.tex:1042-1052
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
