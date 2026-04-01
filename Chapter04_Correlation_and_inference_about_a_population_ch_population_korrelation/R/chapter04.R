# Extracted R code for Chapter 04: Correlation and inference about a population
# Source: CH4 Correlation and inference.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Calculating confidence intervals for correlation in R
# Source lines: CH4 Correlation and inference.tex:82-90
# ------------------------------------------------------------------------------

  df <- read.csv("apartment_price_data.csv")
  corrXY <- cor(df$living_area, df$price)
  Z <- 1/2 * log((1+corrXY)/(1-corrXY))
  alpha <- 0.05
  z_alpha_2 <- qnorm(1-alpha/2)
  Z_L <- Z - z_alpha_2 * sqrt(1/(1000-3))
  Z_U <- Z + z_alpha_2 * sqrt(1/(1000-3))
  CI_L <- (exp(2*Z_L) - 1)/(exp(2*Z_L) + 1)
  CI_U <- (exp(2*Z_U) - 1)/(exp(2*Z_U) + 1)

# ------------------------------------------------------------------------------
# Box 02: Calculating confidence intervals for correlation in R
# Source lines: CH4 Correlation and inference.tex:98-98
# ------------------------------------------------------------------------------

  cor.test(df$living_area, df$price, conf.level=0.95)
