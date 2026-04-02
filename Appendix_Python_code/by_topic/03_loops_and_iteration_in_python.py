# Appendix Python subsection: Loops and iteration in Python
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: The for loop
# ------------------------------------------------------------------------------

# Looping over values (range produces 1, 2, 3, 4, 5)
for k in range(1, 6):
    print(k)

# Looping over an arbitrary list
cities = ["Uppsala", "Stockholm", "Gothenburg"]
for c in cities:
    print(c)

# ------------------------------------------------------------------------------
# Chunk 002
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: The for loop
# Paragraph: Looping over indices (when you need them).
# ------------------------------------------------------------------------------

x = [10, 20, 30]

for i, value in enumerate(x):
    print(i, value)

# ------------------------------------------------------------------------------
# Chunk 003
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: The for loop
# Paragraph: Looping over multiple sequences.
# ------------------------------------------------------------------------------

names  = ["A", "B", "C"]
values = [1.2, 0.7, 2.4]

for n, v in zip(names, values):
    print(n, v)

# ------------------------------------------------------------------------------
# Chunk 004
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: The for loop
# Paragraph: Pre-allocation (when building numeric output).
# ------------------------------------------------------------------------------

import numpy as np

x = np.arange(1, 6)              # array([1, 2, 3, 4, 5])
y = np.empty_like(x, dtype=float)

for i, xi in enumerate(x):
    y[i] = xi**2

y

# ------------------------------------------------------------------------------
# Chunk 005
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: The while loop
# ------------------------------------------------------------------------------

i = 1
while i <= 5:
    print(i)
    i = i + 1

# ------------------------------------------------------------------------------
# Chunk 006
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: The while loop
# ------------------------------------------------------------------------------

# Example: stop after at most 100 iterations
iter_ = 0
value = 1.0

while value < 1000 and iter_ < 100:
    value = value * 1.2
    iter_ = iter_ + 1

{"iter": iter_, "value": value}

# ------------------------------------------------------------------------------
# Chunk 007
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: break, continue, and loop else
# ------------------------------------------------------------------------------

for k in range(1, 11):
    if k % 2 == 0:
        continue      # skip even numbers
    if k > 7:
        break         # stop the loop
    print(k)

# ------------------------------------------------------------------------------
# Chunk 008
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: break, continue, and loop else
# ------------------------------------------------------------------------------

for k in range(2, 10):
    if 10 % k == 0:
        print("10 is divisible by", k)
        break
else:
    print("no divisor found")

# ------------------------------------------------------------------------------
# Chunk 009
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: Alternatives to explicit loops
# Paragraph: Vectorization (NumPy).
# ------------------------------------------------------------------------------

import numpy as np

x = np.arange(1, 11)

# Vectorized: squares every element at once
x**2

# Vectorized: sum of squares
np.sum(x**2)

# ------------------------------------------------------------------------------
# Chunk 010
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: Alternatives to explicit loops
# Paragraph: List comprehensions.
# ------------------------------------------------------------------------------

# Add 1 to each value (builds a list)
[a + 1 for a in range(1, 6)]

# With a condition (keep only values > 2)
[a for a in range(1, 6) if a > 2]

# ------------------------------------------------------------------------------
# Chunk 011
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: Alternatives to explicit loops
# Paragraph: map() and filter() (functional style).
# ------------------------------------------------------------------------------

list(map(lambda a: a + 1, range(1, 6)))
list(filter(lambda a: a > 2, range(1, 6)))

# ------------------------------------------------------------------------------
# Chunk 012
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: Alternatives to explicit loops
# Paragraph: A modern note (optional).
# ------------------------------------------------------------------------------

sum(a*a for a in range(1, 11))   # sum of squares without building a list
