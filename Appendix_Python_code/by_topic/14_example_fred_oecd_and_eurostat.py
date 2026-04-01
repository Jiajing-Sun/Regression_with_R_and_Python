# Appendix Python subsection: Example: FRED, OECD, and Eurostat
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001 (Appendix Python.tex:2153-2170)
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
# Chunk 002 (Appendix Python.tex:2177-2193)
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
# Chunk 003 (Appendix Python.tex:2200-2216)
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
