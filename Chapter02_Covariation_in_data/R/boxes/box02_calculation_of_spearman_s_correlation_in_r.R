# Chapter 02, R box 02: Calculation of Spearman's correlation in R
# Source label: box:spearman
# Full runnable chapter script: ../chapter02.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
df$Rx <- rank(df$living_area)
df$Ry <- rank(df$price)

rS_manual <- cor(df$Rx, df$Ry)
rS_builtin <- cor(df$living_area, df$price, method = "spearman")
