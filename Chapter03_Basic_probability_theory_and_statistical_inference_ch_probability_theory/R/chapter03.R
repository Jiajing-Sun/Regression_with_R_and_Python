# Extracted R code for Chapter 03: Basic probability theory and statistical inference
# Source: CH3 Basic probability.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Monte Carlo simulation in R
# Textbook context: Section: Estimators
# ------------------------------------------------------------------------------

    n <- 50
    dice_throws <- sample(1:6, n, replace=TRUE)
    ybar <- mean(dice_throws)

# ------------------------------------------------------------------------------
# Box 02: Monte Carlo simulation in R
# Textbook context: Section: Estimators
# ------------------------------------------------------------------------------

    nr_samples <- 10000
    n <- 50
    ybar_dist <- rep(NA, nr_samples)
    for (i in 1:nr_samples){
      dice_throws <- sample(1:6, n, replace=TRUE)
      ybar_dist[i] <- mean(dice_throws)
      print(i)
    }

# ------------------------------------------------------------------------------
# Box 03: Monte Carlo simulation in R
# Textbook context: Section: Estimators
# ------------------------------------------------------------------------------

 hist(ybar_dist, breaks=50)

# ------------------------------------------------------------------------------
# Box 04: Hypothesis tests and confidence intervals with R
# Textbook context: Section: Hypothesis testing and confidence intervals | Subsection: Confidence interval
# ------------------------------------------------------------------------------

    dice_throws <- c(rep(1, 13), rep(2, 7), rep(3, 8),
                     rep(4, 9), rep(5, 9), rep(6, 4))

# ------------------------------------------------------------------------------
# Box 05: Hypothesis tests and confidence intervals with R
# Textbook context: Section: Hypothesis testing and confidence intervals | Subsection: Confidence interval
# ------------------------------------------------------------------------------

    n <- length(dice_throws)
    mean_dice_throws <- mean(dice_throws)
    var_dice_throws <- 
      sum((dice_throws - mean_dice_throws)^2) / (n - 1)

# ------------------------------------------------------------------------------
# Box 06: Hypothesis tests and confidence intervals with R
# Textbook context: Section: Hypothesis testing and confidence intervals | Subsection: Confidence interval
# ------------------------------------------------------------------------------

    se_dice_throws <- sqrt(var_dice_throws / n)
    t_stat <- (mean_dice_throws - 3.5) / se_dice_throws

# ------------------------------------------------------------------------------
# Box 07: Hypothesis tests and confidence intervals with R
# Textbook context: Section: Hypothesis testing and confidence intervals | Subsection: Confidence interval
# ------------------------------------------------------------------------------

    p_value <- 2 * (1 - pt(abs(t_stat), df=n-1))

# ------------------------------------------------------------------------------
# Box 08: Hypothesis tests and confidence intervals with R
# Textbook context: Section: Hypothesis testing and confidence intervals | Subsection: Confidence interval
# ------------------------------------------------------------------------------

    alpha <- 0.05
    t_crit <- qt(1-alpha/2, n-1)
    ci_lower <- mean_dice_throws - t_crit * se_dice_throws
    ci_upper <- mean_dice_throws + t_crit * se_dice_throws

# ------------------------------------------------------------------------------
# Box 09: Hypothesis tests and confidence intervals with R
# Textbook context: Section: Hypothesis testing and confidence intervals | Subsection: Confidence interval
# ------------------------------------------------------------------------------

 t.test(dice_throws, mu=3.5)
