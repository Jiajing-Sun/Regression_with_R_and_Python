# Appendix Python subsection: Core data structures in Python
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001 (Appendix Python.tex:763-769)
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: Lists (and basic indexing)
# ------------------------------------------------------------------------------

x_num = [1, 3, 5, 7, 9]
x_chr = ["Emma", "Liam", "Noah"]
x_log = [True, False, True]

len(x_num)
x_num[0]       # first element (Python uses 0-based indexing)
x_num[1:4]     # a slice (elements 2 to 4)

# ------------------------------------------------------------------------------
# Chunk 002 (Appendix Python.tex:779-779)
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: Lists (and basic indexing)
# Paragraph: Type mixing.
# ------------------------------------------------------------------------------

[1, "two", 3]     # allowed: heterogeneous list

# ------------------------------------------------------------------------------
# Chunk 003 (Appendix Python.tex:788-790)
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: Tuples
# ------------------------------------------------------------------------------

t = (201, "Emma", 32)
t
t[1]          # second element

# ------------------------------------------------------------------------------
# Chunk 004 (Appendix Python.tex:799-806)
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: Dictionaries
# ------------------------------------------------------------------------------

emp = {
    "ids":   [201, 202, 203],
    "names": ["Emma", "Liam", "Noah"],
    "n":     3
}

emp
emp["names"]     # access by key

# ------------------------------------------------------------------------------
# Chunk 005 (Appendix Python.tex:815-831)
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: NumPy arrays (vectors and matrices)
# ------------------------------------------------------------------------------

import numpy as np

x = np.array([1, 3, 5, 7, 9])
x
x.shape
x[0]          # first element
x[1:4]        # slice

# A matrix
M = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

M
M.shape
M[0, 1]       # row 1, column 2 (0-based)
M[:, 0]       # first column

# ------------------------------------------------------------------------------
# Chunk 006 (Appendix Python.tex:840-852)
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: pandas DataFrames
# ------------------------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Emma", "Liam", "Noah", "Olivia"],
    "age":  [32, 19, 45, 27],
    "is_adult": [True, False, True, True]
})

df
df.shape          # (rows, columns)
df["age"]         # a column (Series)
df.loc[0:1, :]    # first two rows (label-based)
df.loc[:, ["name", "age"]]

# ------------------------------------------------------------------------------
# Chunk 007 (Appendix Python.tex:866-871)
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: Arrays beyond two dimensions
# ------------------------------------------------------------------------------

import numpy as np

A = np.arange(1, 13).reshape((2, 3, 2))
A
A.shape
A[0, :, 0]    # first "row block", all columns, first slice

# ------------------------------------------------------------------------------
# Chunk 008 (Appendix Python.tex:880-885)
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: Categorical data (similar in spirit to factors)
# ------------------------------------------------------------------------------

import pandas as pd

f = pd.Categorical(["Low", "Medium", "High", "Low", "High"])
f
f.categories
pd.value_counts(f)
