# Appendix Python subsection: Functions in Python
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Functions in Python
# Subsubsection: Defining and calling functions
# ------------------------------------------------------------------------------

def add_numbers(a, b):
    return a + b

add_numbers(5, 3)

# ------------------------------------------------------------------------------
# Chunk 002
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Functions in Python
# Subsubsection: Defining and calling functions
# Paragraph: Defaults and named arguments.
# ------------------------------------------------------------------------------

def power(x, p=2):
    return x**p

power(3)            # uses p = 2
power(3, p=4)       # explicit
power(x=3, p=4)

# ------------------------------------------------------------------------------
# Chunk 003
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Functions in Python
# Subsubsection: Defining and calling functions
# Paragraph: A small numerical example: approximating $e$.
# ------------------------------------------------------------------------------

import math
import numpy as np

# (1) Compound-interest limit: (1 + 1/n)^n
def approx_e_limit(n=1000):
    return (1 + 1/n)**n

# (2) Series expansion with a loop: sum_{k=0}^n 1/k!
def approx_e_series_loop(n=10):
    out = 0.0
    for k in range(0, n + 1):
        out = out + 1 / math.factorial(k)
    return out

# (3) Series expansion, vectorized (NumPy)
def approx_e_series_vec(n=10):
    ks = np.arange(0, n + 1)
    return np.sum(1 / np.vectorize(math.factorial)(ks))

approx_e_limit(10)
approx_e_series_loop(10)
approx_e_series_vec(10)
math.exp(1)   # reference value
