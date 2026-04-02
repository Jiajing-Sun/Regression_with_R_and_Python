# Extracted R code for Chapter 06: Multiple Linear Regression
# Source: CH6 Multiple linear regression.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Multiple regression in R
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

 df <- read.csv("apartment_price_data.csv")

# ------------------------------------------------------------------------------
# Box 02: Multiple regression in R
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

 ols_model <- lm(price ~ living_area + monthly_fee +
 new_production, data=df)

# ------------------------------------------------------------------------------
# Box 03: Multiple regression in R
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

    library("lmtest")
    library("sandwich")
    rob_inf <- coeftest(ols_model,
      vcov = vcovHC(ols_model, type = "HC0"))

# ------------------------------------------------------------------------------
# Box 04: Multiple regression in R
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

      lmtest::coefci(ols_model,
  vcov. = vcovHC(ols_model, type = "HC0"),
  level = 0.95)

# ------------------------------------------------------------------------------
# Box 05: Multiple regression in R
# Textbook context: Section: The general multiple linear regression model
# ------------------------------------------------------------------------------

 b1 <- rob_inf["living_area", "Estimate"]
 se1 <- rob_inf["living_area", "Std. Error"]
 t_stat <- (b1 - 0.04) / se1
 df_model <- ols_model$df.residual
 p_value <- (1 - pt(abs(t_stat), df_model)) * 2

# ------------------------------------------------------------------------------
# Box 06: $F$-test in R
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

 ols_model_l <- lm(price ~ living_area + monthly_fee +
  new_production + build_year, data=df)
 summary(ols_model_l)

# ------------------------------------------------------------------------------
# Box 07: $F$-test in R
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

    n <- nobs(ols_model_l)

# ------------------------------------------------------------------------------
# Box 08: $F$-test in R
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

    b <- !is.na(df$new_production) & !is.na(df$build_year)

# ------------------------------------------------------------------------------
# Box 09: $F$-test in R
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

    ols_model_s <- lm(price ~ living_area + monthly_fee,
                              data=df[b, ])

# ------------------------------------------------------------------------------
# Box 10: $F$-test in R
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

    residuals_l <- residuals(ols_model_l)
    residuals_s <- residuals(ols_model_s)
    RSS_l <- sum(residuals_l^2)
    RSS_s <- sum(residuals_s^2)

# ------------------------------------------------------------------------------
# Box 11: $F$-test in R
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

    K <- 4
    G <- 2

# ------------------------------------------------------------------------------
# Box 12: $F$-test in R
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

    F_obs <- ((RSS_s - RSS_l) / (K - G)) / 
             (RSS_l / (n - (K + 1)))

# ------------------------------------------------------------------------------
# Box 13: $F$-test in R
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

 p <- 1 - pf(F_obs, df1=K-G, df2=n-(K+1))

# ------------------------------------------------------------------------------
# Box 14: $F$-test in R
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

    anova(ols_model_s, ols_model_l)

# ------------------------------------------------------------------------------
# Box 15: $F$-test in R
# Textbook context: Section: $F$-test
# ------------------------------------------------------------------------------

 summary(ols_model_l)

# ------------------------------------------------------------------------------
# Box 16: Robust $F$-test in R
# Textbook context: Section: $F$-test | Subsection: Robust $F$-test
# ------------------------------------------------------------------------------

    library("lmtest")
    library("sandwich")

# ------------------------------------------------------------------------------
# Box 17: Robust $F$-test in R
# Textbook context: Section: $F$-test | Subsection: Robust $F$-test
# ------------------------------------------------------------------------------

    waldtest(ols_model_s, ols_model_l,
             vcov = vcovHC(ols_model_l, type = "HC0"))

# ------------------------------------------------------------------------------
# Box 18: Confidence intervals for expected value and prediction intervals in R
# Textbook context: Section: Uncertainty of the conditional expectation | Subsection: Prediction interval
# ------------------------------------------------------------------------------

 ols_model <- lm(price ~ living_area, data=df)
 x0 <-80
 yhat_x80 <- predict(ols_model,
 newdata=data.frame(living_area=x0))

# ------------------------------------------------------------------------------
# Box 19: Confidence intervals for expected value and prediction intervals in R
# Textbook context: Section: Uncertainty of the conditional expectation | Subsection: Prediction interval
# ------------------------------------------------------------------------------

  n <- nobs(ols_model)
  RSS <- sum(residuals(ols_model)^2)
  s2_epsilon <- RSS / (n - 2)
  xbar <- mean(df$living_area)
  SSX <- sum((df$living_area - xbar)^2)
  var_eY_x0 <- s2_epsilon * (1 / n + (x0 - xbar)^2 / SSX)

# ------------------------------------------------------------------------------
# Box 20: Confidence intervals for expected value and prediction intervals in R
# Textbook context: Section: Uncertainty of the conditional expectation | Subsection: Prediction interval
# ------------------------------------------------------------------------------

 alpha <- 0.05
 t_crit <- qt(1-alpha/2, df=n-2)
 lb_ci_eY_x0 <- yhat_x80 - t_crit * sqrt(var_eY_x0)
 ub_ci_eY_x0 <- yhat_x80 + t_crit * sqrt(var_eY_x0)

# ------------------------------------------------------------------------------
# Box 21: Confidence intervals for expected value and prediction intervals in R
# Textbook context: Section: Uncertainty of the conditional expectation | Subsection: Prediction interval
# ------------------------------------------------------------------------------

 var_tildeepsilon_x0 <- var_eY_x0 + s2_epsilon
 lb_pi_x0 <- yhat_x80 - t_crit * sqrt(var_tildeepsilon_x0)
 ub_pi_x0 <- yhat_x80 + t_crit * sqrt(var_tildeepsilon_x0)

# ------------------------------------------------------------------------------
# Box 22: Confidence intervals for expected value and prediction intervals in R
# Textbook context: Section: Uncertainty of the conditional expectation | Subsection: Prediction interval
# ------------------------------------------------------------------------------

 ols_model2 <- lm(price ~ living_area + monthly_fee +
 new_production, data=df)

# ------------------------------------------------------------------------------
# Box 23: Confidence intervals for expected value and prediction intervals in R
# Textbook context: Section: Uncertainty of the conditional expectation | Subsection: Prediction interval
# ------------------------------------------------------------------------------

 eval_df <- data.frame(living_area=80,
 monthly_fee=3000, new_production=1)
 predict(ols_model2, newdata = eval_df,
 interval = "confidence",
 level=.95)
 predict(ols_model2, newdata = eval_df,
 interval = "prediction",
 level=.95)
