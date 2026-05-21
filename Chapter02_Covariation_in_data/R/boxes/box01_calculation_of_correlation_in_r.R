# Chapter 02, R box 01: Calculation of correlation in R
# Source label: box:korr
# Full runnable chapter script: ../chapter02.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
df <- read.csv("apartment_price_data.csv")
df <- df[complete.cases(df[, c("living_area", "price")]), ]

xbar <- mean(df$living_area)
ybar <- mean(df$price)
n <- nrow(df)

s_xy <- sum((df$living_area - xbar) * (df$price - ybar)) / (n - 1)
s_x2 <- sum((df$living_area - xbar)^2) / (n - 1)
s_y2 <- sum((df$price - ybar)^2) / (n - 1)

corr_manual <- s_xy / (sqrt(s_x2) * sqrt(s_y2))
corr_builtin <- cor(df$living_area, df$price)
