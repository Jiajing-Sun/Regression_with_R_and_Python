# Appendix R section: Probability Distributions
# Source: Appendix R program.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001 (Appendix R program.tex:1301-1305)
# Section: Probability Distributions
# Subsection: Reproducibility: setting the seed
# ------------------------------------------------------------------------------

set.seed(1234)
rnorm(5)

set.seed(1234)
rnorm(5)   # identical output

# ------------------------------------------------------------------------------
# Chunk 002 (Appendix R program.tex:1340-1350)
# Section: Probability Distributions
# Subsection: The inverse c.d.f. (quantile) method
# Subsubsection: Example 1: inverse c.d.f. for the exponential distribution
# ------------------------------------------------------------------------------

set.seed(1)

n <- 10000
rate <- 2

u <- runif(n)
x_icdf <- -log(u) / rate         # inverse cdf method
x_rexp <- rexp(n, rate = rate)   # built-in generator

c(mean_icdf = mean(x_icdf), mean_rexp = mean(x_rexp))
c(var_icdf  = var(x_icdf),  var_rexp  = var(x_rexp))

# ------------------------------------------------------------------------------
# Chunk 003 (Appendix R program.tex:1371-1388)
# Section: Probability Distributions
# Subsection: The inverse c.d.f. (quantile) method
# Subsubsection: The generalized inverse (discrete case)
# ------------------------------------------------------------------------------

set.seed(2)

vals  <- c(0, 1, 2, 5)
probs <- c(0.10, 0.30, 0.50, 0.10)
cdf   <- cumsum(probs)

n <- 20
u <- runif(n)

# Map u to vals via the generalized inverse
idx <- findInterval(u, vec = c(0, cdf), rightmost.closed = TRUE)
x_icdf_discrete <- vals[idx]

x_icdf_discrete

# Compare with R's built-in sampler for discrete distributions
x_sample <- sample(vals, size = n, replace = TRUE, prob = probs)
x_sample

# ------------------------------------------------------------------------------
# Chunk 004 (Appendix R program.tex:1404-1412)
# Section: Probability Distributions
# Subsection: The inverse c.d.f. (quantile) method
# Subsubsection: Example 2: numerical inversion when no closed-form quantile exists
# ------------------------------------------------------------------------------

qnorm_uniroot <- function(u, lower = -10, upper = 10) {
  stopifnot(u > 0, u < 1)
  f <- function(x) pnorm(x) - u
  uniroot(f, interval = c(lower, upper))$root
}

set.seed(3)
u <- runif(5)
sapply(u, qnorm_uniroot)
