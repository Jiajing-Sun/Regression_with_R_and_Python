# Chapter 13, R box 01: RD approach in R
# Source label: box:rd
# Full runnable chapter script: ../chapter13.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages(c("sandwich", "lmtest", "ivreg", "rdrobust"))  # run once if needed
# --- Code block 2 ---
df <- read.csv(file.path("data", "municip_data.csv"))
df <- df[df$municip_name != "Gotland", ]
df$rv <- df$share_seats_left_last_election - .5
df$change_tax_rate <- df$tax_rate - df$tax_rate_4_years_back
df <- df[!is.na(df$change_tax_rate), ]
df$Z <- ifelse(df$rv >= 0, 1, 0)
df$Zrv <- df$Z * df$rv

h <- .05
df_h <- df[abs(df$rv) <= h, ]
rd_fs <- lm(left_coalition_last_term ~ Z + rv + Zrv, data = df_h)
rd_rf <- lm(change_tax_rate ~ Z + rv + Zrv, data = df_h)
# --- Code block 3 ---
library(sandwich)
library(lmtest)
library(ivreg)
coeftest(rd_fs, vcov = vcovHC(rd_fs, type = "HC0"))
coeftest(rd_rf, vcov = vcovHC(rd_rf, type = "HC0"))

rd_2sls <- ivreg(change_tax_rate ~ left_coalition_last_term + rv + Zrv |
                   Z + rv + Zrv, data = df_h)
coeftest(rd_2sls, vcov = vcovHC(rd_2sls, type = "HC0"))

library(rdrobust)
rdrobust(df$change_tax_rate, df$share_seats_left_last_election,
         c = .5, kernel = "uniform", h = h,
         fuzzy = df$left_coalition_last_term)
