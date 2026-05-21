# Chapter 12, R box 01: Time series analysis with R
# Source label: box:time_series
# Full runnable chapter script: ../chapter12.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages("sandwich")  # run once if needed
# --- Code block 2 ---
df <- read.csv(file.path("data", "time_series_sweden.csv"))
gdp_ts <- ts(df$gdp, frequency = 4, start = c(1981, 1))

gdpL1 <- lag(gdp_ts, k = -1)
gdpL2 <- lag(gdp_ts, k = -2)
gdpF1 <- lag(gdp_ts, k = 1)
gdpF2 <- lag(gdp_ts, k = 2)
ma <- (gdpL2/2 + gdpL1 + gdp_ts + gdpF1 + gdpF2/2) / 4

autocorrelation_function <- acf(gdp_ts)
dloggdp <- (log(gdp_ts) - log(gdpL1)) * 100
dloggdpL1 <- lag(dloggdp, k = -1)

dft <- data.frame(ts.union(dloggdp, dloggdpL1))
ar1_model <- lm(dloggdp ~ dloggdpL1, data = dft)
summary(ar1_model)
# --- Code block 3 ---
library(sandwich)
cov_matrix <- NeweyWest(ar1_model, lag = 5, prewhite = FALSE)
sqrt(diag(cov_matrix))

ar_model <- ar.ols(dloggdp, order.max = 5, aic = TRUE,
                   demean = FALSE, intercept = TRUE)
ar_model$order
