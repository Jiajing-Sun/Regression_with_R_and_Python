# Chapter 11, R box 02: Nonparametric RD in R
# Source label: box:r_nonparametric_rd
# Full runnable chapter script: ../chapter11.R
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

tri <- function(u) pmax(0, 1 - abs(u))
h <- .10
df_h <- df[abs(df$rv) <= h, ]
df_h$w <- tri(df_h$rv / h)

rd_fs_np <- lm(left_coalition_last_term ~ Z + rv + Zrv,
               data = df_h, weights = w)
rd_rf_np <- lm(change_tax_rate ~ Z + rv + Zrv,
               data = df_h, weights = w)
# --- Code block 3 ---
library(sandwich); library(lmtest); library(rdrobust)
coeftest(rd_fs_np, vcov = vcovHC(rd_fs_np, type = "HC0"))
coeftest(rd_rf_np, vcov = vcovHC(rd_rf_np, type = "HC0"))
coef(rd_rf_np)["Z"] / coef(rd_fs_np)["Z"]

rdrobust(df$change_tax_rate, df$share_seats_left_last_election,
         c = .5, kernel = "triangular",
         fuzzy = df$left_coalition_last_term)
