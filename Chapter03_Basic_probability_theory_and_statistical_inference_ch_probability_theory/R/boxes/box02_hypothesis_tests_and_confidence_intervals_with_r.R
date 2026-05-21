# Chapter 03, R box 02: Hypothesis tests and confidence intervals  with R
# Source label: box:inference_r
# Full runnable chapter script: ../chapter03.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
dice_throws <- c(rep(1, 13), rep(2, 7), rep(3, 8),
                 rep(4, 9), rep(5, 9), rep(6, 4))

n <- length(dice_throws)
ybar <- mean(dice_throws)
se <- sd(dice_throws) / sqrt(n)

t_stat <- (ybar - 3.5) / se
p_value <- 2 * (1 - pt(abs(t_stat), df = n - 1))

alpha <- 0.05
t_crit <- qt(1 - alpha / 2, df = n - 1)
ci <- ybar + c(-1, 1) * t_crit * se

# Same test and interval in one command:
t.test(dice_throws, mu = 3.5)
