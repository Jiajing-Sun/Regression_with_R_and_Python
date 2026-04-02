# Appendix Python subsection: The Inverse c.d.f. (Inverse Transform) Method
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001
# Chapter: The Python Programming Language
# Section: Probability Distributions
# Subsection: The Inverse c.d.f. (Inverse Transform) Method
# ------------------------------------------------------------------------------

import numpy as np
import scipy.stats as st
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt

# Reproducibility
rng = np.random.default_rng(123456789)

# Standard normal CDF via numerical integration
def compute_phi(z):
    integrand = lambda t: (1.0 / np.sqrt(2.0 * np.pi)) * np.exp(-t**2 / 2.0)
    val, _ = quad(integrand, -np.inf, z)
    return val

# Test the function and compare with SciPy's built-in CDF
z_val = 1.96
print(compute_phi(z_val))
print(st.norm.cdf(z_val))

# Invert Phi numerically using a root finder
def inverse_phi(u):
    f = lambda z: compute_phi(z) - u
    return brentq(f, -10.0, 10.0)

# Step 1: draw from U(0,1) (avoid endpoints for numerical stability)
eps = 1e-12
u = rng.uniform(eps, 1.0 - eps, size=1000)

# Step 2: apply the inverse CDF
sample_norm = np.array([inverse_phi(ui) for ui in u])

# Plot histogram with an empirical (kernel) density curve
plt.figure(figsize=(7, 5))
plt.hist(sample_norm, bins=30, density=True, edgecolor="black", alpha=0.6)

kde = gaussian_kde(sample_norm)
grid = np.linspace(sample_norm.min(), sample_norm.max(), 200)
plt.plot(grid, kde(grid), linewidth=2)

plt.title("Inverse-CDF simulation of a standard normal distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.tight_layout()

# Save figure (adjust the path if needed)
plt.savefig("figures/inverse-cdf-python.png", dpi=150)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 002
# Chapter: The Python Programming Language
# Section: Probability Distributions
# Subsection: The Inverse c.d.f. (Inverse Transform) Method
# ------------------------------------------------------------------------------

# Practical shortcut when a quantile (ppf) is available:
sample_norm_fast = st.norm.ppf(u)
