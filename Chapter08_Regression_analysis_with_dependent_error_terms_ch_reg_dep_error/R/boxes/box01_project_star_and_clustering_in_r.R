# Chapter 08, R box 01: Project Star and clustering in R
# Source label: box:klustring
# Full runnable chapter script: ../chapter08.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages(c("lmtest", "sandwich"))  # run once if needed
# --- Code block 2 ---
df <- read.csv(file.path("data", "star.csv"))
df$small_class <- ifelse(df$class_type == "SMALL", 1, NA)
df$small_class <- ifelse(df$class_type %in% c("AIDE", "REGULAR"),
                         0, df$small_class)
df <- df[complete.cases(df[, c("read_score", "small_class", "class_id")]), ]

ols_model <- lm(read_score ~ small_class, data = df)

library(lmtest)
library(sandwich)
coeftest(ols_model)
coeftest(ols_model, vcov = vcovHC(ols_model, type = "HC0"))
coeftest(ols_model, vcov = vcovCL(ols_model, cluster = df$class_id,
                                  type = "HC0"))
