# Chapter 08, R box 03: The within estimator with municipal data in R
# Source label: box:within_estimator
# Full runnable chapter script: ../chapter08.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages(c("plm", "lmtest", "sandwich"))  # run once if needed
# --- Code block 2 ---
library(plm)
library(lmtest)
library(sandwich)

df <- read.csv(file.path("data", "municip_data.csv"))
df <- df[df$municip_name != "Gotland", ]

within_model <- plm(tax_rate ~ left_coalition_last_term,
                    data = df, index = c("municip_name", "year"),
                    effect = "individual")
coeftest(within_model,
         vcov = vcovHC(within_model, type = "HC0", cluster = "group"))

twoway_model <- plm(tax_rate ~ left_coalition_last_term,
                    data = df, index = c("municip_name", "year"),
                    effect = "twoways")
coeftest(twoway_model,
         vcov = vcovHC(twoway_model, type = "HC0", cluster = "group"))
