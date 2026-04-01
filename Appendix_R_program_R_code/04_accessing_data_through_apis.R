# Appendix R section: Accessing data through APIs
# Source: Appendix R program.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001 (Appendix R program.tex:1791-1815)
# Section: Accessing data through APIs
# Subsection: Examples
# Subsubsection: World Bank indicators via WDI
# ------------------------------------------------------------------------------

# install.packages("WDI")
library(WDI)

# Search indicator names (returns a data frame of matches)
head(WDIsearch("life expectancy"))

# Download life expectancy and GDP per capita (constant prices)
wb <- WDI(
  country   = c("SWE", "DEU", "USA"),
  indicator = c(le = "SP.DYN.LE00.IN", gdppc = "NY.GDP.PCAP.KD"),
  start     = 1995,
  end       = 2022
)

# Basic checks
head(wb)
str(wb)

# Simple base-R ordering and a quick plot for one country
wb <- wb[order(wb$country, wb$year), ]
sweden <- wb[wb$country == "SWE", ]

plot(sweden$year, sweden$gdppc, type = "l",
     xlab = "Year", ylab = "GDP per capita (constant prices)",
     main = "Sweden: GDP per capita over time")

# ------------------------------------------------------------------------------
# Chunk 002 (Appendix R program.tex:1821-1825)
# Section: Accessing data through APIs
# Subsection: Examples
# Subsubsection: World Bank indicators via WDI
# ------------------------------------------------------------------------------

dir.create("data_cache", showWarnings = FALSE)
saveRDS(wb, file = "data_cache/wb_le_gdppc.rds")

# Later:
# wb <- readRDS("data_cache/wb_le_gdppc.rds")

# ------------------------------------------------------------------------------
# Chunk 003 (Appendix R program.tex:1866-1877)
# Section: Accessing data through APIs
# Subsection: Examples
# Subsubsection: FRED via fredr (API key required)
# ------------------------------------------------------------------------------

# install.packages("fredr")
library(fredr)

fredr_set_key(Sys.getenv("FRED_API_KEY"))

# Example series: U.S. unemployment rate (UNRATE)
unrate <- fredr(
  series_id = "UNRATE",
  observation_start = as.Date("2000-01-01")
)

head(unrate)

# ------------------------------------------------------------------------------
# Chunk 004 (Appendix R program.tex:1887-1896)
# Section: Accessing data through APIs
# Subsection: Examples
# Subsubsection: Eurostat via eurostat
# ------------------------------------------------------------------------------

# install.packages("eurostat")
library(eurostat)

# Monthly unemployment rate dataset (example)
une <- get_eurostat("une_rt_m", time_format = "date")

# Keep a small slice: total, all ages, Sweden
une_se <- une[une$geo == "SE" & une$sex == "T" & une$age == "TOTAL", ]

head(une_se)

# ------------------------------------------------------------------------------
# Chunk 005 (Appendix R program.tex:1906-1912)
# Section: Accessing data through APIs
# Subsection: Examples
# Subsubsection: OECD via OECD
# ------------------------------------------------------------------------------

# install.packages("OECD")
library(OECD)

# Example: download a dataset (start_time restricts the time range)
cli <- get_dataset("MEI_CLI", start_time = 2018)

head(cli)

# ------------------------------------------------------------------------------
# Chunk 006 (Appendix R program.tex:1922-1932)
# Section: Accessing data through APIs
# Subsection: Examples
# Subsubsection: Market data via quantmod (Yahoo Finance interface)
# ------------------------------------------------------------------------------

# install.packages("quantmod")
library(quantmod)

# Example: daily prices for Microsoft from Yahoo Finance
getSymbols("MSFT", src = "yahoo")

# Inspect the first rows
head(MSFT)

# Plot adjusted close
plot(Ad(MSFT), main = "MSFT adjusted close", ylab = "Price")

# ------------------------------------------------------------------------------
# Chunk 007 (Appendix R program.tex:1942-1955)
# Section: Accessing data through APIs
# Subsection: Examples
# Subsubsection: Calling an API directly (advanced, but useful)
# ------------------------------------------------------------------------------

# install.packages(c("httr2", "jsonlite"))
library(httr2)
library(jsonlite)

# Example: World Bank API endpoint (returns JSON)
url <- "https://api.worldbank.org/v2/country/SWE/indicator/NY.GDP.PCAP.KD?format=json&per_page=20000"

resp <- request(url) |> req_perform()
txt  <- resp_body_string(resp)

obj <- fromJSON(txt)

# The data are typically in the second element
head(obj[[2]])
