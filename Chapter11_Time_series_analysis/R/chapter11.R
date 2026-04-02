# Extracted R code for Chapter 11: Time series analysis
# Source: CH11 Time series analysis.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    df <- read.csv("time_series_sweden.csv")

# ------------------------------------------------------------------------------
# Box 02: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    gdp_ts <- ts(df$gdp, frequency = 4, start = c(1981, 1))

# ------------------------------------------------------------------------------
# Box 03: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    plot(gdp_ts)

# ------------------------------------------------------------------------------
# Box 04: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    gdpL1 <- lag(gdp_ts, k=-1)
    gdpL2 <- lag(gdp_ts, k=-2)
    gdpF1 <- lag(gdp_ts, k=1)
    gdpF2 <- lag(gdp_ts, k=2)

# ------------------------------------------------------------------------------
# Box 05: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    ma <- (gdpL2/2 + gdpL1 + gdp_ts +  gdpF1 + gdpF2/2)/4

# ------------------------------------------------------------------------------
# Box 06: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    plot(ma)

# ------------------------------------------------------------------------------
# Box 07: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    mean_gdp <- mean(gdp_ts)
    r_1 <- (sum((gdp_ts - mean_gdp) * (gdpL1 - mean_gdp))) / 
           sum((gdp_ts - mean_gdp)^2)

# ------------------------------------------------------------------------------
# Box 08: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

 autocorrelation_function <- acf(gdp_ts)

# ------------------------------------------------------------------------------
# Box 09: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    plot(autocorrelation_function)

# ------------------------------------------------------------------------------
# Box 10: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    dloggdp <- (log(gdp_ts) - log(gdpL1)) * 100
    maL1 <- lag(ma, k=-1)
    dlogma <- (log(ma) - log(maL1)) * 100

# ------------------------------------------------------------------------------
# Box 11: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

plot(dloggdp)
plot(dlogma)

# ------------------------------------------------------------------------------
# Box 12: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

 dloggdpL1 <- lag(dloggdp, k=-1)
 dlogmaL1 <- lag(dlogma, k=-1)

# ------------------------------------------------------------------------------
# Box 13: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    mv_ts <- ts.union(gdp_ts, gdpL1, gdpL2, gdpF1, gdpF2, 
                      ma, dloggdp, dlogma, dloggdpL1,
                      dlogmaL1)
    dft <- data.frame(mv_ts)

# ------------------------------------------------------------------------------
# Box 14: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

 ar1_model <- lm(dloggdp ~ dloggdpL1, data=dft)
 summary(ar1_model)

# ------------------------------------------------------------------------------
# Box 15: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

 library (sandwich)
 cov_matrix <- NeweyWest(ar1_model, lag=5, prewhite=FALSE)

# ------------------------------------------------------------------------------
# Box 16: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    std_errors <- sqrt(diag(cov_matrix))

# ------------------------------------------------------------------------------
# Box 17: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

 ar1_model_alt <- ar.ols(dloggdp,
 order.max = 1,
 aic=FALSE,
 demean = FALSE,
 intercept = TRUE)

# ------------------------------------------------------------------------------
# Box 18: Time series analysis with R
# Textbook context: Section: Autoregressive regression | Subsection: Deterministic or stochastic trend? | Subsubsection: Stochastic Trend
# ------------------------------------------------------------------------------

    ar5_model <- ar.ols(dloggdp, 
      order.max = 5,
      aic=TRUE,
      demean = FALSE, 
      intercept = TRUE)
