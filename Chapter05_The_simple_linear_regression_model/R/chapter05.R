# Extracted R code for Chapter 05: The simple linear regression model
# Source: CH5 Simple linear regression.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Inference for regression in R
# Source lines: CH5 Simple linear regression.tex:277-279
# ------------------------------------------------------------------------------

 s2_epsilon <- RSS / (n - 2)
 SSX <- sum((df$living_area - mean(df$living_area))^2)
 var_hat_beta_1_hat <- s2_epsilon / SSX

# ------------------------------------------------------------------------------
# Box 02: Inference for regression in R
# Source lines: CH5 Simple linear regression.tex:283-286
# ------------------------------------------------------------------------------

 beta_1_H0 <- 0
 se_beta_1_hat <- sqrt(var_hat_beta_1_hat)
 t_stat <- (beta_1_hat - beta_1_H0) / se_beta_1_hat
 p_val <- 2 * (1 - pt(abs(t_stat), df=n-2))

# ------------------------------------------------------------------------------
# Box 03: Inference for regression in R
# Source lines: CH5 Simple linear regression.tex:294-297
# ------------------------------------------------------------------------------

    alpha <- 0.1
    t_crit <- qt(1-alpha/2, df=n-2)
    lb <- beta_1_hat - t_crit * se_beta_1_hat
    ub <- beta_1_hat + t_crit * se_beta_1_hat

# ------------------------------------------------------------------------------
# Box 04: Inference for regression in R
# Source lines: CH5 Simple linear regression.tex:303-303
# ------------------------------------------------------------------------------

 sum_ols_model <- summary(ols_model)

# ------------------------------------------------------------------------------
# Box 05: Inference for regression in R
# Source lines: CH5 Simple linear regression.tex:307-307
# ------------------------------------------------------------------------------

 reg_table <- sum_ols_model$coefficients

# ------------------------------------------------------------------------------
# Box 06: Inference for regression in R
# Source lines: CH5 Simple linear regression.tex:311-311
# ------------------------------------------------------------------------------

 reg_table[2, 3]

# ------------------------------------------------------------------------------
# Box 07: Inference for regression in R
# Source lines: CH5 Simple linear regression.tex:315-315
# ------------------------------------------------------------------------------

 confint(ols_model, level=0.9)

# ------------------------------------------------------------------------------
# Box 08: Inference for regression in R
# Source lines: CH5 Simple linear regression.tex:321-321
# ------------------------------------------------------------------------------

 ols_model2 <- lm(price ~ new_production, data=df)

# ------------------------------------------------------------------------------
# Box 09: Inference for regression in R
# Source lines: CH5 Simple linear regression.tex:327-327
# ------------------------------------------------------------------------------

    confint(ols_model2, level=0.9)

# ------------------------------------------------------------------------------
# Box 10: Robust inference in R
# Source lines: CH5 Simple linear regression.tex:440-440
# ------------------------------------------------------------------------------

 dx2 <- (df$living_area - mean(df$living_area))^2

# ------------------------------------------------------------------------------
# Box 11: Robust inference in R
# Source lines: CH5 Simple linear regression.tex:444-444
# ------------------------------------------------------------------------------

 var_beta_1_var_r <- sum(dx2 * u_hat^2) / (sum(dx2))^2

# ------------------------------------------------------------------------------
# Box 12: Robust inference in R
# Source lines: CH5 Simple linear regression.tex:448-448
# ------------------------------------------------------------------------------

 se_beta_1_hat_r <- sqrt(var_beta_1_var_r)

# ------------------------------------------------------------------------------
# Box 13: Robust inference in R
# Source lines: CH5 Simple linear regression.tex:455-456
# ------------------------------------------------------------------------------

    library("lmtest")
    library("sandwich")

# ------------------------------------------------------------------------------
# Box 14: Robust inference in R
# Source lines: CH5 Simple linear regression.tex:460-460
# ------------------------------------------------------------------------------

 coeftest(ols_model, vcov=vcovHC(ols_model, type="HC0"))
