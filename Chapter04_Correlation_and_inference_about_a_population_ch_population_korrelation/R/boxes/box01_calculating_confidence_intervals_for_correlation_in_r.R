# Chapter 04, R box 01: Calculating confidence intervals for correlation in R
# Source label: box:konfidensintervall
# Full runnable chapter script: ../chapter04.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
df <- read.csv("apartment_price_data.csv")
df <- df[complete.cases(df[, c("living_area", "price")]), ]

corrXY <- cor(df$living_area, df$price)
n <- nrow(df)

Z <- 0.5 * log((1 + corrXY) / (1 - corrXY))
z_alpha_2 <- qnorm(0.975)
Z_L <- Z - z_alpha_2 * sqrt(1 / (n - 3))
Z_U <- Z + z_alpha_2 * sqrt(1 / (n - 3))
CI <- (exp(2 * c(Z_L, Z_U)) - 1) / (exp(2 * c(Z_L, Z_U)) + 1)

cor.test(df$living_area, df$price, conf.level = 0.95)
