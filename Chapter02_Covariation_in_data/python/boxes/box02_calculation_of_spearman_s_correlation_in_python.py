# Chapter 02, Python box 02: Calculation of Spearman's correlation in Python
# Source label: box:pspearman
# Full runnable chapter script: ../chapter02.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
df["Rx"] = df["living_area"].rank(method="average")
df["Ry"] = df["price"].rank(method="average")

rS_manual = df["Rx"].corr(df["Ry"], method="pearson")
rS_builtin = df["living_area"].corr(df["price"], method="spearman")
