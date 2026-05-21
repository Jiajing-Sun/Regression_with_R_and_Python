# Chapter 03, R box 01: Monte Carlo simulation in R
# Source label: box:sim_r
# Full runnable chapter script: ../chapter03.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
set.seed(123)
n <- 50
nr_samples <- 10000

ybar_dist <- replicate(nr_samples, {
  dice_throws <- sample(1:6, n, replace = TRUE)
  mean(dice_throws)
})

mean(ybar_dist)
var(ybar_dist)
hist(ybar_dist, breaks = 50)
