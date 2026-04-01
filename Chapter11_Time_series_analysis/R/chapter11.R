# Extracted R code for Chapter 11: Time series analysis
# Source: CH11 Time series analysis.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:328-328
# ------------------------------------------------------------------------------

    df <- read.csv("time_series_sweden.csv")

# ------------------------------------------------------------------------------
# Box 02: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:332-332
# ------------------------------------------------------------------------------

    gdp_ts <- ts(df$gdp, frequency = 4, start = c(1981, 1))

# ------------------------------------------------------------------------------
# Box 03: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:336-336
# ------------------------------------------------------------------------------

    plot(gdp_ts)

# ------------------------------------------------------------------------------
# Box 04: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:340-343
# ------------------------------------------------------------------------------

    gdpL1 <- lag(gdp_ts, k=-1)
    gdpL2 <- lag(gdp_ts, k=-2)
    gdpF1 <- lag(gdp_ts, k=1)
    gdpF2 <- lag(gdp_ts, k=2)

# ------------------------------------------------------------------------------
# Box 05: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:347-347
# ------------------------------------------------------------------------------

    ma <- (gdpL2/2 + gdpL1 + gdp_ts +  gdpF1 + gdpF2/2)/4

# ------------------------------------------------------------------------------
# Box 06: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:351-351
# ------------------------------------------------------------------------------

    plot(ma)

# ------------------------------------------------------------------------------
# Box 07: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:355-357
# ------------------------------------------------------------------------------

    mean_gdp <- mean(gdp_ts)
    r_1 <- (sum((gdp_ts - mean_gdp) * (gdpL1 - mean_gdp))) / 
           sum((gdp_ts - mean_gdp)^2)

# ------------------------------------------------------------------------------
# Box 08: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:361-361
# ------------------------------------------------------------------------------

 autocorrelation_function <- acf(gdp_ts)

# ------------------------------------------------------------------------------
# Box 09: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:365-365
# ------------------------------------------------------------------------------

    plot(autocorrelation_function)

# ------------------------------------------------------------------------------
# Box 10: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:371-373
# ------------------------------------------------------------------------------

    dloggdp <- (log(gdp_ts) - log(gdpL1)) * 100
    maL1 <- lag(ma, k=-1)
    dlogma <- (log(ma) - log(maL1)) * 100

# ------------------------------------------------------------------------------
# Box 11: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:377-378
# ------------------------------------------------------------------------------

plot(dloggdp)
plot(dlogma)

# ------------------------------------------------------------------------------
# Box 12: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:382-383
# ------------------------------------------------------------------------------

 dloggdpL1 <- lag(dloggdp, k=-1)
 dlogmaL1 <- lag(dlogma, k=-1)

# ------------------------------------------------------------------------------
# Box 13: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:387-390
# ------------------------------------------------------------------------------

    mv_ts <- ts.union(gdp_ts, gdpL1, gdpL2, gdpF1, gdpF2, 
                      ma, dloggdp, dlogma, dloggdpL1,
                      dlogmaL1)
    dft <- data.frame(mv_ts)

# ------------------------------------------------------------------------------
# Box 14: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:394-395
# ------------------------------------------------------------------------------

 ar1_model <- lm(dloggdp ~ dloggdpL1, data=dft)
 summary(ar1_model)

# ------------------------------------------------------------------------------
# Box 15: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:399-400
# ------------------------------------------------------------------------------

 library (sandwich)
 cov_matrix <- NeweyWest(ar1_model, lag=5, prewhite=FALSE)

# ------------------------------------------------------------------------------
# Box 16: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:404-404
# ------------------------------------------------------------------------------

    std_errors <- sqrt(diag(cov_matrix))

# ------------------------------------------------------------------------------
# Box 17: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:408-412
# ------------------------------------------------------------------------------

 ar1_model_alt <- ar.ols(dloggdp,
 order.max = 1,
 aic=FALSE,
 demean = FALSE,
 intercept = TRUE)

# ------------------------------------------------------------------------------
# Box 18: Time series analysis with R
# Source lines: CH11 Time series analysis.tex:416-420
# ------------------------------------------------------------------------------

    ar5_model <- ar.ols(dloggdp, 
      order.max = 5,
      aic=TRUE,
      demean = FALSE, 
      intercept = TRUE)
