# Appendix Python subsection: Basic dataset manipulation in Python
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001 (Appendix Python.tex:1059-1066)
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
# Chunk 002 (Appendix Python.tex:1075-1082)
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
# Chunk 003 (Appendix Python.tex:1091-1094)
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Filtering observations
# ------------------------------------------------------------------------------

# High unemployment (unemp >= 8)
high_unemp = df[df["unemp"] >= 8]

len(high_unemp)

# ------------------------------------------------------------------------------
# Chunk 004 (Appendix Python.tex:1103-1109)
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
# Chunk 005 (Appendix Python.tex:1118-1126)
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
# Chunk 006 (Appendix Python.tex:1135-1137)
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Aggregating and grouping
# ------------------------------------------------------------------------------

# Average unemployment by year
avg_unemp_by_year = df.groupby("year", as_index=False)["unemp"].mean()
avg_unemp_by_year.head()

# ------------------------------------------------------------------------------
# Chunk 007 (Appendix Python.tex:1143-1144)
# Section: Python Programming Fundamentals
# Subsection: Basic dataset manipulation in Python
# Subsubsection: Aggregating and grouping
# ------------------------------------------------------------------------------

avg_by_year = df.groupby("year", as_index=False)[["unemp", "tbilrate", "infl"]].mean()
avg_by_year.head()

# ------------------------------------------------------------------------------
# Chunk 008 (Appendix Python.tex:1150-1156)
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
# Chunk 009 (Appendix Python.tex:1165-1176)
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
# Chunk 010 (Appendix Python.tex:1188-1193)
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
# Chunk 011 (Appendix Python.tex:1200-1208)
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
# Chunk 012 (Appendix Python.tex:1215-1221)
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
# Chunk 013 (Appendix Python.tex:1228-1233)
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
