# Appendix Python subsection: Example: financial time series from Yahoo Finance
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001 (Appendix Python.tex:2125-2142)
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
