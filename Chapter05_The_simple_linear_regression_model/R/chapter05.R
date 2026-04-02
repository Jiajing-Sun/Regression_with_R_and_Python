# Extracted R code for Chapter 05: The simple linear regression model
# Source: CH5 Simple linear regression.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Inference for regression in R
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

 s2_epsilon <- RSS / (n - 2)
 SSX <- sum((df$living_area - mean(df$living_area))^2)
 var_hat_beta_1_hat <- s2_epsilon / SSX

# ------------------------------------------------------------------------------
# Box 02: Inference for regression in R
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

 beta_1_H0 <- 0
 se_beta_1_hat <- sqrt(var_hat_beta_1_hat)
 t_stat <- (beta_1_hat - beta_1_H0) / se_beta_1_hat
 p_val <- 2 * (1 - pt(abs(t_stat), df=n-2))

# ------------------------------------------------------------------------------
# Box 03: Inference for regression in R
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

    alpha <- 0.1
    t_crit <- qt(1-alpha/2, df=n-2)
    lb <- beta_1_hat - t_crit * se_beta_1_hat
    ub <- beta_1_hat + t_crit * se_beta_1_hat

# ------------------------------------------------------------------------------
# Box 04: Inference for regression in R
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

 sum_ols_model <- summary(ols_model)

# ------------------------------------------------------------------------------
# Box 05: Inference for regression in R
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

 reg_table <- sum_ols_model$coefficients

# ------------------------------------------------------------------------------
# Box 06: Inference for regression in R
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

 reg_table[2, 3]

# ------------------------------------------------------------------------------
# Box 07: Inference for regression in R
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

 confint(ols_model, level=0.9)

# ------------------------------------------------------------------------------
# Box 08: Inference for regression in R
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

 ols_model2 <- lm(price ~ new_production, data=df)

# ------------------------------------------------------------------------------
# Box 09: Inference for regression in R
# Textbook context: Section: Inference to the population with spherical error terms
# ------------------------------------------------------------------------------

    confint(ols_model2, level=0.9)

# ------------------------------------------------------------------------------
# Box 10: Robust inference in R
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

 dx2 <- (df$living_area - mean(df$living_area))^2

# ------------------------------------------------------------------------------
# Box 11: Robust inference in R
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

 var_beta_1_var_r <- sum(dx2 * u_hat^2) / (sum(dx2))^2

# ------------------------------------------------------------------------------
# Box 12: Robust inference in R
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

 se_beta_1_hat_r <- sqrt(var_beta_1_var_r)

# ------------------------------------------------------------------------------
# Box 13: Robust inference in R
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

    library("lmtest")
    library("sandwich")

# ------------------------------------------------------------------------------
# Box 14: Robust inference in R
# Textbook context: Section: Asymptotic inference to the population
# ------------------------------------------------------------------------------

 coeftest(ols_model, vcov=vcovHC(ols_model, type="HC0"))
