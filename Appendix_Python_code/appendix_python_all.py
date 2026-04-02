# Appendix: The Python Programming Language
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

# ------------------------------------------------------------------------------
# Chunk 010
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
# Chunk 011
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
# Chunk 012
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
# Chunk 013
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
# Chunk 014
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
# Chunk 015
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
# Chunk 016
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
# Chunk 017
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
# Chunk 018
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
# Chunk 019
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
# Chunk 020
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: Alternatives to explicit loops
# Paragraph: map() and filter() (functional style).
# ------------------------------------------------------------------------------

list(map(lambda a: a + 1, range(1, 6)))
list(filter(lambda a: a > 2, range(1, 6)))

# ------------------------------------------------------------------------------
# Chunk 021
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Loops and iteration in Python
# Subsubsection: Alternatives to explicit loops
# Paragraph: A modern note (optional).
# ------------------------------------------------------------------------------

sum(a*a for a in range(1, 11))   # sum of squares without building a list

# ------------------------------------------------------------------------------
# Chunk 022
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Functions in Python
# Subsubsection: Defining and calling functions
# ------------------------------------------------------------------------------

def add_numbers(a, b):
    return a + b

add_numbers(5, 3)

# ------------------------------------------------------------------------------
# Chunk 023
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
# Chunk 024
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

# ------------------------------------------------------------------------------
# Chunk 025
# Chapter: The Python Programming Language
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
# Chunk 026
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: Lists (and basic indexing)
# Paragraph: Type mixing.
# ------------------------------------------------------------------------------

[1, "two", 3]     # allowed: heterogeneous list

# ------------------------------------------------------------------------------
# Chunk 027
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: Tuples
# ------------------------------------------------------------------------------

t = (201, "Emma", 32)
t
t[1]          # second element

# ------------------------------------------------------------------------------
# Chunk 028
# Chapter: The Python Programming Language
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
# Chunk 029
# Chapter: The Python Programming Language
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
# Chunk 030
# Chapter: The Python Programming Language
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
# Chunk 031
# Chapter: The Python Programming Language
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
# Chunk 032
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Core data structures in Python
# Subsubsection: Categorical data (similar in spirit to factors)
# ------------------------------------------------------------------------------

import pandas as pd

f = pd.Categorical(["Low", "Medium", "High", "Low", "High"])
f
f.categories
pd.value_counts(f)

# ------------------------------------------------------------------------------
# Chunk 033
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: File paths and reproducibility
# ------------------------------------------------------------------------------

from pathlib import Path

# Project root (adjust to your project folder if needed)
project = Path(".")   # current directory

# A relative path to a data file
csv_path = project / "data" / "macro_panel.csv"
csv_path

# ------------------------------------------------------------------------------
# Chunk 034
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: File paths and reproducibility
# ------------------------------------------------------------------------------

csv_path.resolve()

# ------------------------------------------------------------------------------
# Chunk 035
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Delimited text files: CSV and friends
# ------------------------------------------------------------------------------

import pandas as pd
from pathlib import Path

csv_path = Path("data") / "macro_panel.csv"

# Basic import
df = pd.read_csv(csv_path)

# Quick checks
df.head()
df.info()
df.describe()

# ------------------------------------------------------------------------------
# Chunk 036
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Delimited text files: CSV and friends
# ------------------------------------------------------------------------------

# Example: tell pandas which strings should be treated as missing
df2 = pd.read_csv(csv_path, na_values=["", "NA", ".", "-999"])

# Example: semicolon-separated file
df3 = pd.read_csv(Path("data") / "macro_panel_semicolon.csv", sep=";")

# ------------------------------------------------------------------------------
# Chunk 037
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Excel workbooks (.xls and .xlsx)
# ------------------------------------------------------------------------------

import pandas as pd
from pathlib import Path

xlsx_path = Path("data") / "household_survey.xlsx"

survey = pd.read_excel(xlsx_path)
survey_wave1 = pd.read_excel(xlsx_path, sheet_name="Wave1")

survey_wave1.head()

# ------------------------------------------------------------------------------
# Chunk 038
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Stata, SPSS, and SAS files
# ------------------------------------------------------------------------------

import pandas as pd
from pathlib import Path

stata_path = Path("data") / "firm_panel.dta"
firm_panel = pd.read_stata(stata_path)

firm_panel.info()

# ------------------------------------------------------------------------------
# Chunk 039
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Modern columnar formats: Parquet/Arrow
# ------------------------------------------------------------------------------

import pandas as pd
from pathlib import Path

parquet_path = Path("data") / "large_panel.parquet"

df_parquet = pd.read_parquet(parquet_path)

# Select a subset of columns (helps when files are big)
df_small = pd.read_parquet(parquet_path, columns=["id", "year", "outcome"])

# ------------------------------------------------------------------------------
# Chunk 040
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: APIs and web data (a first look)
# ------------------------------------------------------------------------------

import requests

# Example pattern (URL is just an illustration; APIs differ)
url = "https://api.example.com/data"
params = {"country": "SE", "year": 2020}

resp = requests.get(url, params=params)
resp.raise_for_status()   # raises an error if the request failed

# Parse JSON into Python objects (often dicts/lists)
obj = resp.json()

type(obj)

# ------------------------------------------------------------------------------
# Chunk 041
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: APIs and web data (a first look)
# ------------------------------------------------------------------------------

import pandas as pd

df_api = pd.json_normalize(obj)
df_api.head()

# ------------------------------------------------------------------------------
# Chunk 042
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import statsmodels.api as sm

df = sm.datasets.macrodata.load_pandas().data

df.head()
df.info()

# ------------------------------------------------------------------------------
# Chunk 043
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Subsetting rows and columns
# ------------------------------------------------------------------------------

# Select columns by name
df_small = df[["realgdp", "realcons", "tbilrate", "unemp"]]

# Select the first 10 rows (position-based)
df_first10 = df.iloc[:10, :]

# Select one column (returns a Series)
unemp = df["unemp"]

# ------------------------------------------------------------------------------
# Chunk 044
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Filtering observations
# ------------------------------------------------------------------------------

# High unemployment (unemp >= 8)
high_unemp = df[df["unemp"] >= 8]

len(high_unemp)

# ------------------------------------------------------------------------------
# Chunk 045
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Filtering observations
# ------------------------------------------------------------------------------

# For illustration: create a few artificial missing values
df2 = df.copy()
df2.loc[df2.sample(5, random_state=1).index, "unemp"] = np.nan

# Filter while explicitly excluding missing values
high_unemp2 = df2[df2["unemp"].notna() & (df2["unemp"] >= 8)]
high_unemp2[["year", "quarter", "unemp"]].head()

# ------------------------------------------------------------------------------
# Chunk 046
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Creating new variables
# ------------------------------------------------------------------------------

df3 = df.copy()

# A simple transformation (log real GDP)
df3["log_realgdp"] = np.log(df3["realgdp"])

# A logical indicator (high unemployment)
df3["high_unemp"] = df3["unemp"] >= 8

df3[["realgdp", "log_realgdp", "unemp", "high_unemp"]].head()

# ------------------------------------------------------------------------------
# Chunk 047
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Aggregating and grouping
# ------------------------------------------------------------------------------

# Average unemployment by year
avg_unemp_by_year = df.groupby("year", as_index=False)["unemp"].mean()
avg_unemp_by_year.head()

# ------------------------------------------------------------------------------
# Chunk 048
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Aggregating and grouping
# ------------------------------------------------------------------------------

avg_by_year = df.groupby("year", as_index=False)[["unemp", "tbilrate", "infl"]].mean()
avg_by_year.head()

# ------------------------------------------------------------------------------
# Chunk 049
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Aggregating and grouping
# ------------------------------------------------------------------------------

summary_by_year = df.groupby("year").agg(
    mean_unemp=("unemp", "mean"),
    sd_unemp=("unemp", "std"),
    mean_infl=("infl", "mean")
).reset_index()

summary_by_year.head()

# ------------------------------------------------------------------------------
# Chunk 050
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Preliminary analysis: quick summaries
# ------------------------------------------------------------------------------

# Summary of all numeric columns
df.describe()

# Mean and variance of unemployment
df["unemp"].mean()
df["unemp"].var()

# Quantiles
df["unemp"].quantile([0.1, 0.5, 0.9])

# Frequency table for quarter
df["quarter"].value_counts().sort_index()

# ------------------------------------------------------------------------------
# Chunk 051
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Saving results and outputs
# Paragraph: Python/pandas-native formats.
# ------------------------------------------------------------------------------

from pathlib import Path

Path("output").mkdir(exist_ok=True)

df3.to_pickle("output/macrodata_clean.pkl")
df3_loaded = pd.read_pickle("output/macrodata_clean.pkl")

# ------------------------------------------------------------------------------
# Chunk 052
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Saving results and outputs
# Paragraph: Saving model results (illustration).
# ------------------------------------------------------------------------------

# Simple regression: real GDP on consumption, investment, interest rate, unemployment
y = df["realgdp"]
X = df[["realcons", "realinv", "tbilrate", "unemp"]]
X = sm.add_constant(X)

fit = sm.OLS(y, X).fit()

fit.save("output/fit_gdp_model.pickle")
fit_loaded = sm.load("output/fit_gdp_model.pickle")

# ------------------------------------------------------------------------------
# Chunk 053
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Saving results and outputs
# Paragraph: Tabular formats.
# ------------------------------------------------------------------------------

coef_table = pd.DataFrame({
    "term": fit.params.index,
    "estimate": fit.params.values
})

coef_table.to_csv("output/coef_table.csv", index=False)
coef_table.to_excel("output/coef_table.xlsx", index=False)

# ------------------------------------------------------------------------------
# Chunk 054
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Saving results and outputs
# Paragraph: Systematic file names.
# ------------------------------------------------------------------------------

spec = "baseline"
start_year = int(df["year"].min())
end_year   = int(df["year"].max())

fname = Path("output") / f"gdp_model_{spec}_years_{start_year}_{end_year}.pickle"
fit.save(fname)

# ------------------------------------------------------------------------------
# Chunk 055
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

from pathlib import Path

FIG_DIR = Path("Your_Folder")
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------------------
# Chunk 056
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import statsmodels.api as sm

co2_raw = sm.datasets.co2.load_pandas().data
co2_raw.head()
co2_raw.info()

co2_raw.index.min(), co2_raw.index.max()

# ------------------------------------------------------------------------------
# Chunk 057
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import pandas as pd

co2 = co2_raw["co2"].resample("M").mean().dropna()
co2.head()

# ------------------------------------------------------------------------------
# Chunk 058
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt

ax = co2.plot()
plt.show()

# ------------------------------------------------------------------------------
# Chunk 059
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4))
plt.plot(co2.index, co2.values, linewidth=2)
plt.xlabel("Year")
plt.ylabel("CO2 concentration (ppm)")
plt.title("Atmospheric CO2 at Mauna Loa (monthly averages)")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Chunk 060
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

plt.figure(figsize=(10, 4))
plt.plot(co2.index, co2.values, linewidth=2)
plt.xlabel("Year")
plt.ylabel("CO2 concentration (ppm)")
plt.title("Atmospheric CO2 at Mauna Loa (monthly averages)")
plt.tight_layout()

plt.savefig(FIG_DIR / "co2_timeseries_py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 061
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame.copy()

# Make the data frame resemble the familiar R-style naming
df = df.rename(columns={
    "sepal length (cm)": "Sepal.Length",
    "sepal width (cm)":  "Sepal.Width",
    "petal length (cm)": "Petal.Length",
    "petal width (cm)":  "Petal.Width",
})

df["Species"] = df["target"].map(dict(enumerate(iris.target_names)))
df = df.drop(columns=["target"])

df.head()
df.describe()

# ------------------------------------------------------------------------------
# Chunk 062
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.figure(figsize=(6.5, 4.8))
plt.hist(df["Sepal.Length"], bins=15, edgecolor="black")
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(FIG_DIR / "hist-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 063
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

plt.figure(figsize=(6.5, 4.8))
plt.scatter(df["Sepal.Width"], df["Sepal.Length"], s=25)
plt.title("Sepal Width vs Sepal Length")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Sepal Length (cm)")
plt.tight_layout()

plt.savefig(FIG_DIR / "scatter-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 064
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

species_order = sorted(df["Species"].unique())
data_by_species = [df.loc[df["Species"] == s, "Sepal.Length"] for s in species_order]

plt.figure(figsize=(6.5, 4.8))
plt.boxplot(data_by_species, labels=species_order)
plt.title("Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.tight_layout()

plt.savefig(FIG_DIR / "box-plot-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 065
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

from pandas.plotting import scatter_matrix

cols = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]

axes = scatter_matrix(df[cols], figsize=(8, 8), diagonal="hist")
plt.suptitle("Scatterplot Matrix for Iris Measurements", y=1.02)
plt.tight_layout()

plt.savefig(FIG_DIR / "pair-plot-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 066
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import numpy as np

corr = df[cols].corr()

plt.figure(figsize=(6.5, 4.8))
plt.imshow(corr.values)
plt.xticks(range(len(cols)), cols, rotation=45, ha="right")
plt.yticks(range(len(cols)), cols)
plt.colorbar()
plt.title("Correlation Heatmap (Iris)")
plt.tight_layout()

plt.savefig(FIG_DIR / "correlation-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 067
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D projection)

fig = plt.figure(figsize=(6.5, 4.8))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(df["Sepal.Length"], df["Sepal.Width"], df["Petal.Length"], s=20)

ax.set_title("3D Scatterplot: Sepal Length, Sepal Width, Petal Length")
ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Sepal Width (cm)")
ax.set_zlabel("Petal Length (cm)")

plt.tight_layout()
plt.savefig(FIG_DIR / "3d-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 068
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Using Python's documentation tools
# ------------------------------------------------------------------------------

import numpy as np

help(np.random.Generator.uniform)

# ------------------------------------------------------------------------------
# Chunk 069
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Using Python's documentation tools
# ------------------------------------------------------------------------------

import inspect
import textwrap
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

FIG_DIR = Path("Your_Folder")
FIG_DIR.mkdir(parents=True, exist_ok=True)

doc = inspect.getdoc(np.random.Generator.uniform)
doc_lines = doc.splitlines()
excerpt = "\n".join(doc_lines[:40])   # keep it short for a figure

# Wrap long lines for readability
excerpt = "\n".join(textwrap.fill(line, width=95) for line in excerpt.splitlines())

fig = plt.figure(figsize=(10, 6))
fig.text(0.01, 0.99, excerpt, va="top", ha="left", family="monospace", fontsize=8)
plt.axis("off")

plt.savefig(FIG_DIR / "help-uniform-python.png", dpi=150, bbox_inches="tight")
plt.close()

# ------------------------------------------------------------------------------
# Chunk 070
# Chapter: The Python Programming Language
# Section: Probability Distributions
# Subsection: Discrete and Continuous Probability Distributions
# ------------------------------------------------------------------------------

import numpy as np
import scipy.stats as st

rng = np.random.default_rng(123456789) # reproducible random numbers

# ------------------------------------------------------------------------------
# Chunk 071
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
# Chunk 072
# Chapter: The Python Programming Language
# Section: Probability Distributions
# Subsection: The Inverse c.d.f. (Inverse Transform) Method
# ------------------------------------------------------------------------------

# Practical shortcut when a quantile (ppf) is available:
sample_norm_fast = st.norm.ppf(u)

# ------------------------------------------------------------------------------
# Chunk 073
# Chapter: The Python Programming Language
# Section: Accessing Data via APIs (Python)
# Subsection: Example: World Bank data via wbgapi
# ------------------------------------------------------------------------------

# If needed (in your virtual environment):
# python -m pip install wbgapi pandas matplotlib

import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt

# Search for indicators (interactive listing)
wb.series.info(q="gdp per capita")

# Download GDP per capita (constant 2015 USD) for selected countries, 1990--2022
gdppc = wb.data.DataFrame(
    "NY.GDP.PCAP.KD",
    ["CHN", "GBR", "USA"],
    time=range(1990, 2023),
    labels=True
).reset_index()

# Clean up year labels like "YR1990" -> 1990 and rename the value column
gdppc["year"] = gdppc["time"].str.replace("YR", "", regex=False).astype(int)
gdppc = gdppc.rename(columns={"NY.GDP.PCAP.KD": "gdppc"})

# Plot GDP per capita over time
plt.figure(figsize=(8, 4))
for name, g in gdppc.groupby("Country"):
    plt.plot(g["year"], g["gdppc"], label=name)

plt.title("GDP per Capita (constant 2015 USD)")
plt.xlabel("Year")
plt.ylabel("GDP per capita")
plt.legend()
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Chunk 074
# Chapter: The Python Programming Language
# Section: Accessing Data via APIs (Python)
# Subsection: Example: financial time series from Yahoo Finance
# ------------------------------------------------------------------------------

# If needed:
# python -m pip install yfinance pandas matplotlib

import yfinance as yf
import matplotlib.pyplot as plt

# Download daily prices for Apple Inc.
aapl = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
print(aapl.head())

# Plot adjusted close
plt.figure(figsize=(8, 4))
aapl["Adj Close"].plot()
plt.title("AAPL adjusted close price")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Chunk 075
# Chapter: The Python Programming Language
# Section: Accessing Data via APIs (Python)
# Subsection: Example: FRED, OECD, and Eurostat
# Subsubsection: FRED (requires an API key).
# ------------------------------------------------------------------------------

# If needed:
# python -m pip install fredapi pandas matplotlib

import os
from fredapi import Fred
import matplotlib.pyplot as plt

fred = Fred(api_key=os.getenv("FRED_API_KEY"))

# U.S. CPI (all urban consumers), monthly
cpi = fred.get_series("CPIAUCSL", observation_start="2000-01-01")
print(cpi.tail())

cpi.plot(figsize=(8, 4), title="CPI (CPIAUCSL), FRED")
plt.xlabel("Date")
plt.ylabel("Index")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Chunk 076
# Chapter: The Python Programming Language
# Section: Accessing Data via APIs (Python)
# Subsection: Example: FRED, OECD, and Eurostat
# Subsubsection: OECD via SDMX (no key).
# ------------------------------------------------------------------------------

# If needed:
# python -m pip install pandasdmx pandas

import pandas as pd
import pandasdmx as pdmx

# Tell pandaSDMX we want OECD data
oecd = pdmx.Request("OECD")

# Example query (dataset-specific codes; see OECD SDMX documentation)
data = oecd.data(
    resource_id="PDB_LV",
    key="GBR+FRA+CAN+ITA+DEU+JPN+USA.T_GDPEMP.CPC/all?startTime=2010",
).to_pandas()

df_oecd = pd.DataFrame(data).reset_index()
print(df_oecd.head())

# ------------------------------------------------------------------------------
# Chunk 077
# Chapter: The Python Programming Language
# Section: Accessing Data via APIs (Python)
# Subsection: Example: FRED, OECD, and Eurostat
# Subsubsection: Eurostat (no key).
# ------------------------------------------------------------------------------

# If needed:
# python -m pip install eurostatapiclient pandas

from eurostatapiclient import EurostatAPIClient

client = EurostatAPIClient("1.0", "json", "en")

# Retrieve a dataset and convert to a DataFrame
dataset = client.get_dataset("tps00001")
df_eurostat = dataset.to_dataframe()
print(df_eurostat.head())

# Filtered request (example: Germany only)
params = {"geo": "DE"}
dataset_de = client.get_dataset("tps00001", params=params)
df_de = dataset_de.to_dataframe()
print(df_de.head())
