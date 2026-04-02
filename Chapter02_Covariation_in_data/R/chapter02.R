# Extracted R code for Chapter 02: Covariation in data
# Source: CH2 Covariation in data.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

    df <- read.csv("apartment_price_data.csv")

# ------------------------------------------------------------------------------
# Box 02: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

    xbar <- mean(df$living_area)
    ybar <- mean(df$price)

# ------------------------------------------------------------------------------
# Box 03: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

    is.na(df$price)

# ------------------------------------------------------------------------------
# Box 04: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

    !is.na(df$price) & !is.na(df$living_area)

# ------------------------------------------------------------------------------
# Box 05: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

    df <- df[!is.na(df$price) & !is.na(df$living_area), ]

# ------------------------------------------------------------------------------
# Box 06: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

    xbar <- mean(df$living_area)
    ybar <- mean(df$price)
    n <- nrow(df)

# ------------------------------------------------------------------------------
# Box 07: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

      s_xy <- 1 / (n - 1) * sum((df$living_area - xbar) *
                                (df$price - ybar))

# ------------------------------------------------------------------------------
# Box 08: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

      s_x2 <- 1 / (n - 1) * sum((df$living_area - xbar)^2)
      s_y2 <- 1 / (n - 1) * sum((df$price - ybar)^2)

# ------------------------------------------------------------------------------
# Box 09: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

      corr_xy <- s_xy / (sqrt(s_x2) * sqrt(s_y2))

# ------------------------------------------------------------------------------
# Box 10: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

      corr_xy <- cov(df$living_area, df$price) / 
                 (sd(df$living_area) * sd(df$price))

# ------------------------------------------------------------------------------
# Box 11: Calculation of correlation in R
# Textbook context: Section: Pearson's correlation
# ------------------------------------------------------------------------------

      corr_xy <- cor(df$living_area, df$price)

# ------------------------------------------------------------------------------
# Box 12: Calculation of Spearman's correlation in R
# Textbook context: Section: Spearman's rank correlation coefficient
# ------------------------------------------------------------------------------

    df$Rx <- rank(df$living_area)
    df$Ry <- rank(df$price)

# ------------------------------------------------------------------------------
# Box 13: Calculation of Spearman's correlation in R
# Textbook context: Section: Spearman's rank correlation coefficient
# ------------------------------------------------------------------------------

    mean_Rx <- (n + 1) / 2
    mean_Ry <- (n + 1) / 2

# ------------------------------------------------------------------------------
# Box 14: Calculation of Spearman's correlation in R
# Textbook context: Section: Spearman's rank correlation coefficient
# ------------------------------------------------------------------------------

    covRxRy <- sum((df$Rx - mean_Rx)*(df$Ry-mean_Ry)) / (n - 1)
   sRx <- sqrt(sum((df$Rx - mean_Rx)^2) / (n - 1))
sRy <- sqrt(sum((df$Ry - mean_Ry)^2) / (n - 1))

# ------------------------------------------------------------------------------
# Box 15: Calculation of Spearman's correlation in R
# Textbook context: Section: Spearman's rank correlation coefficient
# ------------------------------------------------------------------------------

    rS <- covRxRy / (sRx * sRy)

# ------------------------------------------------------------------------------
# Box 16: Calculation of Spearman's correlation in R
# Textbook context: Section: Spearman's rank correlation coefficient
# ------------------------------------------------------------------------------

    rS_alt <- cor(df$Rx, df$Ry, method = "spearman")

# ------------------------------------------------------------------------------
# Box 17: Regression in R
# Textbook context: Section: Simple linear regression | Subsection: Coefficient of determination
# ------------------------------------------------------------------------------

  beta_1_hat <- s_xy / s_x2
  beta_0_hat <- ybar - xbar * beta_1_hat

# ------------------------------------------------------------------------------
# Box 18: Regression in R
# Textbook context: Section: Simple linear regression | Subsection: Coefficient of determination
# ------------------------------------------------------------------------------

  y_hat <- beta_0_hat + beta_1_hat * df$living_area

# ------------------------------------------------------------------------------
# Box 19: Regression in R
# Textbook context: Section: Simple linear regression | Subsection: Coefficient of determination
# ------------------------------------------------------------------------------

 u_hat <- df$price - y_hat

# ------------------------------------------------------------------------------
# Box 20: Regression in R
# Textbook context: Section: Simple linear regression | Subsection: Coefficient of determination
# ------------------------------------------------------------------------------

  RSS <- sum(u_hat^2)
  TSS <- sum((df$price - ybar)^2)
  R2 <- 1 - RSS / TSS

# ------------------------------------------------------------------------------
# Box 21: Regression in R
# Textbook context: Section: Simple linear regression | Subsection: Coefficient of determination
# ------------------------------------------------------------------------------

 ols_model <- lm(price ~ living_area, data=df)

# ------------------------------------------------------------------------------
# Box 22: Regression in R
# Textbook context: Section: Simple linear regression | Subsection: Coefficient of determination
# ------------------------------------------------------------------------------

 summary(ols_model)
