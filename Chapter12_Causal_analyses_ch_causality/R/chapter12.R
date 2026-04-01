# Extracted R code for Chapter 12: Causal analyses
# Source: CH12 Causal analyses.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: RD approach in R
# Source lines: CH12 Causal analyses.tex:908-908
# ------------------------------------------------------------------------------

install.packages(c("sandwich", "lmtest", "ivreg", "rdrobust"))

# ------------------------------------------------------------------------------
# Box 02: RD approach in R
# Source lines: CH12 Causal analyses.tex:913-919
# ------------------------------------------------------------------------------

 df <- read.csv("municip_data.csv")
 df <- df[df$municip_name != "Gotland", ]
 df$rv <- df$share_seats_left_last_election - .5
 df$change_tax_rate <- df$tax_rate - df$tax_rate_4_years_back
 df <- df[!is.na(df$change_tax_rate), ]
 df$Z <- ifelse(df$rv >= 0, 1, 0)
 df$Zrv <- df$Z * df$rv

# ------------------------------------------------------------------------------
# Box 03: RD approach in R
# Source lines: CH12 Causal analyses.tex:923-935
# ------------------------------------------------------------------------------

  h <- .05
  rd_fs <- lm(left_coalition_last_term ~ Z + rv + Zrv,
              data=df[abs(df$rv) <= h, ])
  rd_rf <- lm(change_tax_rate ~ Z + rv + Zrv,
              data=df[abs(df$rv) <= h, ])
  Dhat <- predict(rd_fs)
  rd_2sls <- lm(change_tax_rate ~ Dhat + rv + Zrv,
                data=df[abs(df$rv) <= h, ])
  library(sandwich)
  library(lmtest)
  coeftest(rd_fs, vcov=vcovHC(rd_fs, type="HC0"))
  coeftest(rd_rf, vcov=vcovHC(rd_rf, type="HC0"))
  summary(rd_2sls)

# ------------------------------------------------------------------------------
# Box 04: RD approach in R
# Source lines: CH12 Causal analyses.tex:939-944
# ------------------------------------------------------------------------------

  library(ivreg)
  rd_2sls_correct <- ivreg(change_tax_rate ~ 
      left_coalition_last_term + rv + Zrv | Z + rv + Zrv,
      data=df[abs(df$rv) <= h, ])
  coeftest(rd_2sls_correct, vcov=vcovHC(rd_2sls_correct,
                                        type="HC0"))

# ------------------------------------------------------------------------------
# Box 05: RD approach in R
# Source lines: CH12 Causal analyses.tex:948-952
# ------------------------------------------------------------------------------

 install.packages("rdrobust")
 library(rdrobust)
 rd_fs_alt <- rdrobust(df$left_coalition_last_term,
 df$share_seats_left_last_election,
 c=.5, kernel="uniform", h=h)

# ------------------------------------------------------------------------------
# Box 06: RD approach in R
# Source lines: CH12 Causal analyses.tex:960-963
# ------------------------------------------------------------------------------

  rd_2sls_alt <- rdrobust(df$change_tax_rate,
    df$share_seats_left_last_election,
    c=.5, kernel="uniform", h=h,
    fuzzy=df$left_coalition_last_term)
