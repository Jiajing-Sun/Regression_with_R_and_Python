# Extracted R code for Chapter 02: Covariation in data
# Source: CH2 Covariation in data.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:62-62
# ------------------------------------------------------------------------------

    df <- read.csv("apartment_price_data.csv")

# ------------------------------------------------------------------------------
# Box 02: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:70-71
# ------------------------------------------------------------------------------

    xbar <- mean(df$living_area)
    ybar <- mean(df$price)

# ------------------------------------------------------------------------------
# Box 03: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:75-75
# ------------------------------------------------------------------------------

    is.na(df$price)

# ------------------------------------------------------------------------------
# Box 04: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:79-79
# ------------------------------------------------------------------------------

    !is.na(df$price) & !is.na(df$living_area)

# ------------------------------------------------------------------------------
# Box 05: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:83-83
# ------------------------------------------------------------------------------

    df <- df[!is.na(df$price) & !is.na(df$living_area), ]

# ------------------------------------------------------------------------------
# Box 06: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:87-89
# ------------------------------------------------------------------------------

    xbar <- mean(df$living_area)
    ybar <- mean(df$price)
    n <- nrow(df)

# ------------------------------------------------------------------------------
# Box 07: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:93-94
# ------------------------------------------------------------------------------

      s_xy <- 1 / (n - 1) * sum((df$living_area - xbar) *
                                (df$price - ybar))

# ------------------------------------------------------------------------------
# Box 08: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:102-103
# ------------------------------------------------------------------------------

      s_x2 <- 1 / (n - 1) * sum((df$living_area - xbar)^2)
      s_y2 <- 1 / (n - 1) * sum((df$price - ybar)^2)

# ------------------------------------------------------------------------------
# Box 09: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:111-111
# ------------------------------------------------------------------------------

      corr_xy <- s_xy / (sqrt(s_x2) * sqrt(s_y2))

# ------------------------------------------------------------------------------
# Box 10: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:115-116
# ------------------------------------------------------------------------------

      corr_xy <- cov(df$living_area, df$price) / 
                 (sd(df$living_area) * sd(df$price))

# ------------------------------------------------------------------------------
# Box 11: Calculation of correlation in R
# Source lines: CH2 Covariation in data.tex:120-120
# ------------------------------------------------------------------------------

      corr_xy <- cor(df$living_area, df$price)

# ------------------------------------------------------------------------------
# Box 12: Calculation of Spearman's correlation in R
# Source lines: CH2 Covariation in data.tex:210-211
# ------------------------------------------------------------------------------

    df$Rx <- rank(df$living_area)
    df$Ry <- rank(df$price)

# ------------------------------------------------------------------------------
# Box 13: Calculation of Spearman's correlation in R
# Source lines: CH2 Covariation in data.tex:215-216
# ------------------------------------------------------------------------------

    mean_Rx <- (n + 1) / 2
    mean_Ry <- (n + 1) / 2

# ------------------------------------------------------------------------------
# Box 14: Calculation of Spearman's correlation in R
# Source lines: CH2 Covariation in data.tex:220-222
# ------------------------------------------------------------------------------

    covRxRy <- sum((df$Rx - mean_Rx)*(df$Ry-mean_Ry)) / (n - 1)
   sRx <- sqrt(sum((df$Rx - mean_Rx)^2) / (n - 1))
sRy <- sqrt(sum((df$Ry - mean_Ry)^2) / (n - 1))

# ------------------------------------------------------------------------------
# Box 15: Calculation of Spearman's correlation in R
# Source lines: CH2 Covariation in data.tex:226-226
# ------------------------------------------------------------------------------

    rS <- covRxRy / (sRx * sRy)

# ------------------------------------------------------------------------------
# Box 16: Calculation of Spearman's correlation in R
# Source lines: CH2 Covariation in data.tex:230-230
# ------------------------------------------------------------------------------

    rS_alt <- cor(df$Rx, df$Ry, method = "spearman")

# ------------------------------------------------------------------------------
# Box 17: Regression in R
# Source lines: CH2 Covariation in data.tex:449-450
# ------------------------------------------------------------------------------

  beta_1_hat <- s_xy / s_x2
  beta_0_hat <- ybar - xbar * beta_1_hat

# ------------------------------------------------------------------------------
# Box 18: Regression in R
# Source lines: CH2 Covariation in data.tex:454-454
# ------------------------------------------------------------------------------

  y_hat <- beta_0_hat + beta_1_hat * df$living_area

# ------------------------------------------------------------------------------
# Box 19: Regression in R
# Source lines: CH2 Covariation in data.tex:458-458
# ------------------------------------------------------------------------------

 u_hat <- df$price - y_hat

# ------------------------------------------------------------------------------
# Box 20: Regression in R
# Source lines: CH2 Covariation in data.tex:462-464
# ------------------------------------------------------------------------------

  RSS <- sum(u_hat^2)
  TSS <- sum((df$price - ybar)^2)
  R2 <- 1 - RSS / TSS

# ------------------------------------------------------------------------------
# Box 21: Regression in R
# Source lines: CH2 Covariation in data.tex:468-468
# ------------------------------------------------------------------------------

 ols_model <- lm(price ~ living_area, data=df)

# ------------------------------------------------------------------------------
# Box 22: Regression in R
# Source lines: CH2 Covariation in data.tex:472-472
# ------------------------------------------------------------------------------

 summary(ols_model)
