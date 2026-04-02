# Appendix Python subsection: Importing data and accessing external sources
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001
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
# Chunk 002
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: File paths and reproducibility
# ------------------------------------------------------------------------------

csv_path.resolve()

# ------------------------------------------------------------------------------
# Chunk 003
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
# Chunk 004
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
# Chunk 005
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
# Chunk 006
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
# Chunk 007
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
# Chunk 008
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
# Chunk 009
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: APIs and web data (a first look)
# ------------------------------------------------------------------------------

import pandas as pd

df_api = pd.json_normalize(obj)
df_api.head()
