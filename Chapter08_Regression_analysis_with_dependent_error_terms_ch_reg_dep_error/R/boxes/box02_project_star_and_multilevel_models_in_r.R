# Chapter 08, R box 02: Project Star and multilevel models in R
# Source label: box:multilevel
# Full runnable chapter script: ../chapter08.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages("lme4")  # run once if needed
# --- Code block 2 ---
library(lme4)

df <- read.csv(file.path("data", "star.csv"))
df$small_class <- ifelse(df$class_type == "SMALL", 1, NA)
df$small_class <- ifelse(df$class_type %in% c("AIDE", "REGULAR"),
                         0, df$small_class)
df <- df[complete.cases(df[, c("read_score", "small_class", "class_id")]), ]

multi_model <- lmer(read_score ~ small_class + (1 | class_id), data = df)
summary(multi_model)
