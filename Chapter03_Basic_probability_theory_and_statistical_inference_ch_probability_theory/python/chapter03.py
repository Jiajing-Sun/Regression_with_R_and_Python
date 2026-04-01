# Extracted Python code for Chapter 03: Basic probability theory and statistical inference
# Source: CH3 Basic probability.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Monte Carlo simulation in Python
# Source lines: CH3 Basic probability.tex:331-334
# ------------------------------------------------------------------------------

import numpy as np

rng = np.random.default_rng()     # optional: np.random.default_rng(123) for a fixed seed
dice_throw = rng.integers(1, 7)   # 1,2,3,4,5,6 with equal probability

# ------------------------------------------------------------------------------
# Box 02: Monte Carlo simulation in Python
# Source lines: CH3 Basic probability.tex:338-340
# ------------------------------------------------------------------------------

n = 50
dice_throws = rng.integers(1, 7, size=n)
ybar = dice_throws.mean()

# ------------------------------------------------------------------------------
# Box 03: Monte Carlo simulation in Python
# Source lines: CH3 Basic probability.tex:344-354
# ------------------------------------------------------------------------------

nr_samples = 10000
n = 50
ybar_dist = np.empty(nr_samples)

for i in range(nr_samples):
    dice_throws = rng.integers(1, 7, size=n)
    ybar_dist[i] = dice_throws.mean()

    # optional: simple progress indicator
    # if (i + 1) % 1000 == 0:
    #     print(i + 1)

# ------------------------------------------------------------------------------
# Box 04: Monte Carlo simulation in Python
# Source lines: CH3 Basic probability.tex:358-359
# ------------------------------------------------------------------------------

mean_ybar = ybar_dist.mean()
var_ybar = ybar_dist.var(ddof=1)   # ddof=1 gives the sample variance

# ------------------------------------------------------------------------------
# Box 05: Monte Carlo simulation in Python
# Source lines: CH3 Basic probability.tex:365-367
# ------------------------------------------------------------------------------

nr_samples = 10000
n = 50
ybar_dist = rng.integers(1, 7, size=(nr_samples, n)).mean(axis=1)

# ------------------------------------------------------------------------------
# Box 06: Monte Carlo simulation in Python
# Source lines: CH3 Basic probability.tex:371-374
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.hist(ybar_dist, bins=50)
plt.show()

# ------------------------------------------------------------------------------
# Box 07: Hypothesis tests and confidence intervals with Python
# Source lines: CH3 Basic probability.tex:701-710
# ------------------------------------------------------------------------------

import numpy as np

dice_throws = np.concatenate([
    np.repeat(1, 13),
    np.repeat(2,  7),
    np.repeat(3,  8),
    np.repeat(4,  9),
    np.repeat(5,  9),
    np.repeat(6,  4),
])

# ------------------------------------------------------------------------------
# Box 08: Hypothesis tests and confidence intervals with Python
# Source lines: CH3 Basic probability.tex:714-716
# ------------------------------------------------------------------------------

n = dice_throws.size
mean_dice_throws = dice_throws.mean()
var_dice_throws = dice_throws.var(ddof=1)   # sample variance (n-1)

# ------------------------------------------------------------------------------
# Box 09: Hypothesis tests and confidence intervals with Python
# Source lines: CH3 Basic probability.tex:720-721
# ------------------------------------------------------------------------------

se_dice_throws = np.sqrt(var_dice_throws / n)
t_stat = (mean_dice_throws - 3.5) / se_dice_throws

# ------------------------------------------------------------------------------
# Box 10: Hypothesis tests and confidence intervals with Python
# Source lines: CH3 Basic probability.tex:725-727
# ------------------------------------------------------------------------------

from scipy import stats

p_value = 2 * stats.t.sf(np.abs(t_stat), df=n-1)   # sf = 1 - cdf

# ------------------------------------------------------------------------------
# Box 11: Hypothesis tests and confidence intervals with Python
# Source lines: CH3 Basic probability.tex:731-735
# ------------------------------------------------------------------------------

alpha = 0.05
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)

ci_lower = mean_dice_throws - t_crit * se_dice_throws
ci_upper = mean_dice_throws + t_crit * se_dice_throws

# ------------------------------------------------------------------------------
# Box 12: Hypothesis tests and confidence intervals with Python
# Source lines: CH3 Basic probability.tex:739-741
# ------------------------------------------------------------------------------

ttest_res = stats.ttest_1samp(dice_throws, popmean=3.5)  # default is two-sided
t_stat_builtin = ttest_res.statistic
p_value_builtin = ttest_res.pvalue

# ------------------------------------------------------------------------------
# Box 13: Hypothesis tests and confidence intervals with Python
# Source lines: CH3 Basic probability.tex:745-747
# ------------------------------------------------------------------------------

ci_lower_alt, ci_upper_alt = stats.t.interval(
    1 - alpha, df=n-1, loc=mean_dice_throws, scale=se_dice_throws
)
