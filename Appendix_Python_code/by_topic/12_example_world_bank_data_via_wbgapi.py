# Appendix Python subsection: Example: World Bank data via wbgapi
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001
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
