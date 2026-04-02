# Appendix Python subsection: Basic computations in Python
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic computations in Python
# Subsubsection: Arithmetic and vectorized operations
# ------------------------------------------------------------------------------

# Basic arithmetic
5 + 9
15 - 7
8 * 9
144 / 12

# Integer division and remainder
144 // 12
145 % 12

# Powers and roots
3**4
import math
math.sqrt(81)

# Parentheses work as expected
(5 + 9) * 2

# ------------------------------------------------------------------------------
# Chunk 002
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic computations in Python
# Subsubsection: Note (why you see ... in the Python prompt).
# ------------------------------------------------------------------------------

import numpy as np

# A numeric array
x = np.array([1, 2, 3, 4])

# Add 10 to every element
x + 10

# Multiply element-by-element
x * np.array([2, 2, 2, 2])

# Compare values (returns a boolean array)
x > 2

# ------------------------------------------------------------------------------
# Chunk 003
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic computations in Python
# Subsubsection: Note (why you see ... in the Python prompt).
# Paragraph: Broadcasting (use with care).
# ------------------------------------------------------------------------------

import numpy as np

x = np.arange(1, 7)          # array([1, 2, 3, 4, 5, 6])

# Broadcasting: the length-2 array is repeated to match length 6
x + np.array([1, 2])

# If shapes are incompatible, NumPy raises an error (this is good!)
np.arange(1, 6) + np.array([1, 2, 3])

# ------------------------------------------------------------------------------
# Chunk 004
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic computations in Python
# Subsubsection: Note (why you see ... in the Python prompt).
# Paragraph: Broadcasting (use with care).
# ------------------------------------------------------------------------------

x.shape

# ------------------------------------------------------------------------------
# Chunk 005
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic computations in Python
# Subsubsection: Inspecting objects: type(), dir(), and help()
# ------------------------------------------------------------------------------

# A number (int)
type(2)

# A floating-point number (float)
type(2.0)

# A string
type("hello")

# Explore available attributes and methods (often too long to read fully)
dir("hello")

# Built-in help for functions and objects
help(len)

# ------------------------------------------------------------------------------
# Chunk 006
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic computations in Python
# Subsubsection: Inspecting objects: type(), dir(), and help()
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

x = np.array([1, 2, 3, 4])
x.dtype
x.shape

df = pd.DataFrame({
  "id": [1, 2, 3],
  "group": ["A", "A", "B"],
  "y": [1.2, 0.7, 2.4]
})

df.head()
df.describe()
df.info()

# ------------------------------------------------------------------------------
# Chunk 007
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic computations in Python
# Subsubsection: Fundamental constants and special values
# Paragraph: Mathematical constants.
# ------------------------------------------------------------------------------

import math
import numpy as np

# pi is built in
math.pi

# e is built in
math.e

# Natural logarithm and exponential
math.log(10)
math.exp(2)

# NumPy versions (operate element-wise on arrays)
np.log(np.array([1, 10, 100]))
np.exp(np.array([0, 1, 2]))

# ------------------------------------------------------------------------------
# Chunk 008
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic computations in Python
# Subsubsection: Fundamental constants and special values
# Paragraph: Missing values, infinities, and undefined results.
# ------------------------------------------------------------------------------

import math
import numpy as np

# A general "missing" object in Python
None

# Undefined or missing numeric values
float("nan")     # NaN
float("inf")     # Inf
float("-inf")    # -Inf

# Undefined operations (in floating point)
0.0/0.0          # ZeroDivisionError in Python (unlike R)
np.nan           # commonly used NaN in NumPy/pandas

# Check what is what
math.isnan(float("nan"))
math.isfinite(float("inf"))

np.isnan(np.nan)
np.isfinite(np.array([1.0, np.nan, np.inf]))

# ------------------------------------------------------------------------------
# Chunk 009
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic computations in Python
# Subsubsection: Fundamental constants and special values
# Paragraph: Machine precision (optional but useful).
# ------------------------------------------------------------------------------

import sys
import numpy as np

# Floating-point information for Python's float (IEEE 754 double)
sys.float_info.epsilon
sys.float_info.min
sys.float_info.max

# NumPy float64 information (typically the same as Python float)
np.finfo(np.float64).eps
np.finfo(np.float64).tiny
np.finfo(np.float64).max
