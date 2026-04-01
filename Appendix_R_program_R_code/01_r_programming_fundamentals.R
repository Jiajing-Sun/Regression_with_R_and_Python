# Appendix R section: R Programming Fundamentals
# Source: Appendix R program.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001 (Appendix R program.tex:132-143)
# Section: R Programming Fundamentals
# Subsection: Basic computations in R
# Subsubsection: Arithmetic and vectorized operations
# ------------------------------------------------------------------------------

# Basic arithmetic
5 + 9
15 - 7
8 * 9
144 / 12

# Powers and roots
3^4
sqrt(81)

# Parentheses work as expected
(5 + 9) * 2

# ------------------------------------------------------------------------------
# Chunk 002 (Appendix R program.tex:149-159)
# Section: R Programming Fundamentals
# Subsection: Basic computations in R
# Subsubsection: Arithmetic and vectorized operations
# ------------------------------------------------------------------------------

# A numeric vector
x <- c(1, 2, 3, 4)

# Add 10 to every element
x + 10

# Multiply element-by-element
x * c(2, 2, 2, 2)

# Compare values (returns a logical vector)
x > 2

# ------------------------------------------------------------------------------
# Chunk 003 (Appendix R program.tex:166-171)
# Section: R Programming Fundamentals
# Subsection: Basic computations in R
# Subsubsection: Arithmetic and vectorized operations
# Paragraph: Recycling (use with care).
# ------------------------------------------------------------------------------

# Recycling: c(1, 2) is repeated to match length 6
1:6 + c(1, 2)

# If the longer length is not a multiple of the shorter one,
# R will warn you.
1:5 + c(1, 2)

# ------------------------------------------------------------------------------
# Chunk 004 (Appendix R program.tex:179-189)
# Section: R Programming Fundamentals
# Subsection: Basic computations in R
# Subsubsection: Inspecting objects: str(), class(), and typeof()
# ------------------------------------------------------------------------------

# A single number in R is typically stored as a double (numeric)
str(2)
typeof(2)

# An integer uses the suffix L
str(2L)
typeof(2L)

# A character string
str("hello")
typeof("hello")

# ------------------------------------------------------------------------------
# Chunk 005 (Appendix R program.tex:195-204)
# Section: R Programming Fundamentals
# Subsection: Basic computations in R
# Subsubsection: Inspecting objects: str(), class(), and typeof()
# ------------------------------------------------------------------------------

# A small data frame
df <- data.frame(
  id    = 1:3,
  group = c("A", "A", "B"),
  y     = c(1.2, 0.7, 2.4)
)

head(df)
summary(df)
str(df)

# ------------------------------------------------------------------------------
# Chunk 006 (Appendix R program.tex:214-222)
# Section: R Programming Fundamentals
# Subsection: Basic computations in R
# Subsubsection: Fundamental constants and special values
# Paragraph: Mathematical constants.
# ------------------------------------------------------------------------------

# pi is built in
pi

# e can be obtained as exp(1)
exp(1)

# Natural logarithm and exponential
log(10)
exp(2)

# ------------------------------------------------------------------------------
# Chunk 007 (Appendix R program.tex:234-245)
# Section: R Programming Fundamentals
# Subsection: Basic computations in R
# Subsubsection: Fundamental constants and special values
# Paragraph: Missing values, infinities, and undefined results.
# ------------------------------------------------------------------------------

# Missing data
NA

# Undefined operations
0/0        # NaN
1/0        # Inf
-1/0       # -Inf

# Check what is what
is.na(NA)
is.nan(0/0)
is.finite(1/0)

# ------------------------------------------------------------------------------
# Chunk 008 (Appendix R program.tex:252-257)
# Section: R Programming Fundamentals
# Subsection: Basic computations in R
# Subsubsection: Fundamental constants and special values
# Paragraph: Machine precision (optional but useful).
# ------------------------------------------------------------------------------

# Smallest difference distinguishable from 1 (roughly)
.Machine$double.eps

# Approximate smallest/largest positive doubles
.Machine$double.xmin
.Machine$double.xmax

# ------------------------------------------------------------------------------
# Chunk 009 (Appendix R program.tex:285-294)
# Section: R Programming Fundamentals
# Subsection: Loops and iteration in R
# Subsubsection: The for loop
# ------------------------------------------------------------------------------

# Looping over values
for (k in 1:5) {
  print(k)
}

# Looping over an arbitrary vector
cities <- c("Uppsala", "Stockholm", "Gothenburg")
for (c in cities) {
  print(c)
}

# ------------------------------------------------------------------------------
# Chunk 010 (Appendix R program.tex:301-305)
# Section: R Programming Fundamentals
# Subsection: Loops and iteration in R
# Subsubsection: The for loop
# Paragraph: Looping over indices (safely).
# ------------------------------------------------------------------------------

x <- c(10, 20, 30)

for (i in seq_along(x)) {
  print(x[i])
}

# ------------------------------------------------------------------------------
# Chunk 011 (Appendix R program.tex:312-321)
# Section: R Programming Fundamentals
# Subsection: Loops and iteration in R
# Subsubsection: The for loop
# Paragraph: Pre-allocation.
# ------------------------------------------------------------------------------

x <- 1:5

# Pre-allocate a numeric vector
y <- numeric(length(x))

for (i in seq_along(x)) {
  y[i] <- x[i]^2
}

y

# ------------------------------------------------------------------------------
# Chunk 012 (Appendix R program.tex:330-334)
# Section: R Programming Fundamentals
# Subsection: Loops and iteration in R
# Subsubsection: The while loop
# ------------------------------------------------------------------------------

i <- 1
while (i <= 5) {
  print(i)
  i <- i + 1
}

# ------------------------------------------------------------------------------
# Chunk 013 (Appendix R program.tex:343-352)
# Section: R Programming Fundamentals
# Subsection: Loops and iteration in R
# Subsubsection: The while loop
# ------------------------------------------------------------------------------

# Example: stop after at most 100 iterations
iter <- 0
value <- 1

while (value < 1000 && iter < 100) {
  value <- value * 1.2
  iter  <- iter + 1
}

c(iter = iter, value = value)

# ------------------------------------------------------------------------------
# Chunk 014 (Appendix R program.tex:361-369)
# Section: R Programming Fundamentals
# Subsection: Loops and iteration in R
# Subsubsection: The repeat loop
# ------------------------------------------------------------------------------

i <- 0
repeat {
  i <- i + 1
  print(i)

  if (i >= 5) {
    break
  }
}

# ------------------------------------------------------------------------------
# Chunk 015 (Appendix R program.tex:385-391)
# Section: R Programming Fundamentals
# Subsection: Loops and iteration in R
# Subsubsection: Alternatives to explicit loops
# Paragraph: Vectorization.
# ------------------------------------------------------------------------------

x <- 1:10

# Vectorized: squares every element at once
x^2

# Vectorized: sum of squares
sum(x^2)

# ------------------------------------------------------------------------------
# Chunk 016 (Appendix R program.tex:404-408)
# Section: R Programming Fundamentals
# Subsection: Loops and iteration in R
# Subsubsection: Alternatives to explicit loops
# Paragraph: The apply family.
# ------------------------------------------------------------------------------

# lapply returns a list
lapply(1:5, function(a) a + 1)

# sapply tries to simplify to a vector
sapply(1:5, function(a) a + 1)

# ------------------------------------------------------------------------------
# Chunk 017 (Appendix R program.tex:416-417)
# Section: R Programming Fundamentals
# Subsection: Loops and iteration in R
# Subsubsection: Alternatives to explicit loops
# Paragraph: A modern note (optional).
# ------------------------------------------------------------------------------

# Anonymous function (compact syntax)
sapply(1:5, \(a) a + 1)

# ------------------------------------------------------------------------------
# Chunk 018 (Appendix R program.tex:435-439)
# Section: R Programming Fundamentals
# Subsection: Functions in R
# Subsubsection: Defining and calling functions
# ------------------------------------------------------------------------------

add_numbers <- function(a, b) {
  a + b
}

add_numbers(5, 3)

# ------------------------------------------------------------------------------
# Chunk 019 (Appendix R program.tex:446-452)
# Section: R Programming Fundamentals
# Subsection: Functions in R
# Subsubsection: Defining and calling functions
# Paragraph: Defaults and named arguments.
# ------------------------------------------------------------------------------

power <- function(x, p = 2) {
  x^p
}

power(3)          # uses p = 2
power(3, p = 4)   # explicit
power(x = 3, p = 4)

# ------------------------------------------------------------------------------
# Chunk 020 (Appendix R program.tex:459-481)
# Section: R Programming Fundamentals
# Subsection: Functions in R
# Subsubsection: Defining and calling functions
# Paragraph: A small numerical example: approximating $e$.
# ------------------------------------------------------------------------------

# (1) Compound-interest limit: (1 + 1/n)^n
approx_e_limit <- function(n = 1000) {
  (1 + 1/n)^n
}

# (2) Series expansion with a loop: sum_{k=0}^n 1/k!
approx_e_series_loop <- function(n = 10) {
  out <- 0
  for (k in 0:n) {
    out <- out + 1 / factorial(k)
  }
  out
}

# (3) Series expansion, vectorized
approx_e_series_vec <- function(n = 10) {
  sum(1 / factorial(0:n))
}

approx_e_limit(10)
approx_e_series_loop(10)
approx_e_series_vec(10)
exp(1)  # reference value

# ------------------------------------------------------------------------------
# Chunk 021 (Appendix R program.tex:502-508)
# Section: R Programming Fundamentals
# Subsection: Core data structures in R
# Subsubsection: Vectors (atomic vectors)
# ------------------------------------------------------------------------------

x_num <- c(1, 3, 5, 7, 9)
x_chr <- c("Emma", "Liam", "Noah")
x_log <- c(TRUE, FALSE, TRUE)

length(x_num)
x_num[1]      # first element
x_num[2:4]    # a slice

# ------------------------------------------------------------------------------
# Chunk 022 (Appendix R program.tex:515-515)
# Section: R Programming Fundamentals
# Subsection: Core data structures in R
# Subsubsection: Vectors (atomic vectors)
# Paragraph: Coercion.
# ------------------------------------------------------------------------------

c(1, "two", 3)    # coerces to character

# ------------------------------------------------------------------------------
# Chunk 023 (Appendix R program.tex:524-535)
# Section: R Programming Fundamentals
# Subsection: Core data structures in R
# Subsubsection: Lists
# ------------------------------------------------------------------------------

emp_ids   <- c(201, 202, 203)
emp_names <- c("Emma", "Liam", "Noah")

employee_list <- list(
  ids   = emp_ids,
  names = emp_names,
  n     = length(emp_ids)
)

employee_list
employee_list$names   # access by name
employee_list[[1]]    # access by position

# ------------------------------------------------------------------------------
# Chunk 024 (Appendix R program.tex:544-556)
# Section: R Programming Fundamentals
# Subsection: Core data structures in R
# Subsubsection: Data frames
# ------------------------------------------------------------------------------

df <- data.frame(
  name    = c("Emma", "Liam", "Noah", "Olivia"),
  age     = c(32, 19, 45, 27),
  is_adult = c(TRUE, FALSE, TRUE, TRUE)
)

df
nrow(df)
ncol(df)

df$age
df[1:2, ]        # first two rows
df[, c("name", "age")]

# ------------------------------------------------------------------------------
# Chunk 025 (Appendix R program.tex:570-579)
# Section: R Programming Fundamentals
# Subsection: Core data structures in R
# Subsubsection: Matrices
# ------------------------------------------------------------------------------

M <- matrix(
  c(10, 20, 30,
    40, 50, 60,
    70, 80, 90),
  nrow = 3, byrow = TRUE
)

M
M[1, 2]      # row 1, column 2
M[, 1]       # first column

# ------------------------------------------------------------------------------
# Chunk 026 (Appendix R program.tex:588-591)
# Section: R Programming Fundamentals
# Subsection: Core data structures in R
# Subsubsection: Arrays
# ------------------------------------------------------------------------------

A <- array(1:12, dim = c(2, 3, 2))
A
dim(A)
A[1, , 1]    # first row, all columns, first "slice"

# ------------------------------------------------------------------------------
# Chunk 027 (Appendix R program.tex:600-603)
# Section: R Programming Fundamentals
# Subsection: Core data structures in R
# Subsubsection: Factors
# ------------------------------------------------------------------------------

f <- factor(c("Low", "Medium", "High", "Low", "High"))
f
levels(f)
table(f)

# ------------------------------------------------------------------------------
# Chunk 028 (Appendix R program.tex:628-637)
# Section: R Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: File paths and reproducibility
# ------------------------------------------------------------------------------

# Where am I?
getwd()

# If you must change working directory, do it once at the top of the script:
# setwd("/path/to/your/project")

# A common alternative is the {here} package for project-relative paths:
# install.packages("here")
# library(here)
# here("data", "my_file.csv")

# ------------------------------------------------------------------------------
# Chunk 029 (Appendix R program.tex:646-651)
# Section: R Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Delimited text files: CSV and friends
# ------------------------------------------------------------------------------

# Base R import
df_base <- read.csv("data/macro_panel.csv")

# Quick checks
head(df_base)
str(df_base)

# ------------------------------------------------------------------------------
# Chunk 030 (Appendix R program.tex:655-662)
# Section: R Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Delimited text files: CSV and friends
# ------------------------------------------------------------------------------

# Fast and friendly import (tidyverse style)
# install.packages("readr")
library(readr)

# returns a tibble (a modern data frame)
df <- read_csv("data/macro_panel.csv")  
# compact overview (from dplyr)
glimpse(df)

# ------------------------------------------------------------------------------
# Chunk 031 (Appendix R program.tex:672-674)
# Section: R Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Delimited text files: CSV and friends
# ------------------------------------------------------------------------------

# Example: tell R which strings should be treated as missing
df2 <- read.csv("data/macro_panel.csv", na.strings = c("", "NA", ".",
        "-999"))

# ------------------------------------------------------------------------------
# Chunk 032 (Appendix R program.tex:683-690)
# Section: R Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Excel workbooks (.xls and .xlsx)
# ------------------------------------------------------------------------------

# install.packages("readxl")
library(readxl)

survey <- read_excel("data/household_survey.xlsx")
survey_wave1 <- read_excel("data/household_survey.xlsx", 
                sheet = "Wave1")

head(survey_wave1)

# ------------------------------------------------------------------------------
# Chunk 033 (Appendix R program.tex:700-706)
# Section: R Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Stata, SPSS, and SAS files
# ------------------------------------------------------------------------------

# install.packages("haven")
library(haven)

firm_panel <- read_dta("data/firm_panel.dta")
experiment <- read_sav("data/experiment_data.sav")

str(firm_panel)

# ------------------------------------------------------------------------------
# Chunk 034 (Appendix R program.tex:716-723)
# Section: R Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: Modern columnar formats: Parquet/Arrow
# ------------------------------------------------------------------------------

# install.packages("arrow")
library(arrow)

df_parquet <- read_parquet("data/large_panel.parquet")

# Select a subset of columns (helps when files are big)
df_small <- read_parquet("data/large_panel.parquet",
                         col_select = c("id", "year", "outcome"))

# ------------------------------------------------------------------------------
# Chunk 035 (Appendix R program.tex:731-745)
# Section: R Programming Fundamentals
# Subsection: Importing data and accessing external sources
# Subsubsection: APIs and web data (a first look)
# ------------------------------------------------------------------------------

# install.packages(c("httr2", "jsonlite"))
library(httr2)
library(jsonlite)

# Example pattern (URL is just an illustration; APIs differ)
req <- request("https://api.example.com/data") |>
  req_url_query(country = "SE", year = 2020)

resp <- req_perform(req)

# Parse JSON into an R object (often a list/data frame)
content_txt <- resp_body_string(resp)
obj <- fromJSON(content_txt)

str(obj)

# ------------------------------------------------------------------------------
# Chunk 036 (Appendix R program.tex:758-760)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# ------------------------------------------------------------------------------

data(airquality)
head(airquality)
str(airquality)

# ------------------------------------------------------------------------------
# Chunk 037 (Appendix R program.tex:769-776)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Subsetting rows and columns
# ------------------------------------------------------------------------------

# Select columns by name
aq_small <- airquality[, c("Ozone", "Solar.R", "Wind", "Temp")]

# Select the first 10 rows
aq_first10 <- airquality[1:10, ]

# Select one column (returns a vector)
temp <- airquality$Temp

# ------------------------------------------------------------------------------
# Chunk 038 (Appendix R program.tex:786-793)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Filtering observations
# ------------------------------------------------------------------------------

# Hot days (Temp >= 90)
hot_days <- airquality[airquality$Temp >= 90, ]

# Days with high ozone (and not missing)
high_ozone <- airquality[!is.na(airquality$Ozone) 
              & airquality$Ozone > 80, ]

nrow(high_ozone)

# ------------------------------------------------------------------------------
# Chunk 039 (Appendix R program.tex:801-809)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Creating new variables
# ------------------------------------------------------------------------------

aq <- airquality

# A simple transformation (Celsius)
aq$TempC <- (aq$Temp - 32) * 5/9

# A logical indicator (very windy day)
aq$HighWind <- aq$Wind > 15

head(aq)

# ------------------------------------------------------------------------------
# Chunk 040 (Appendix R program.tex:818-827)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Aggregating and grouping
# ------------------------------------------------------------------------------

# Average temperature by month (base R)
avg_temp_by_month <- aggregate(Temp ~ Month, data = airquality, 
                    FUN = mean)
avg_temp_by_month

# Average ozone by month (remove missing values)
avg_ozone_by_month <- aggregate(Ozone ~ Month, data = airquality,
                               FUN = function(x) 
                               mean(x, na.rm = TRUE))
avg_ozone_by_month

# ------------------------------------------------------------------------------
# Chunk 041 (Appendix R program.tex:833-836)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Aggregating and grouping
# ------------------------------------------------------------------------------

avg_by_month <- aggregate(cbind(Temp, Wind) ~ Month,
                          data = airquality, FUN = mean, 
                          na.rm = TRUE)
avg_by_month

# ------------------------------------------------------------------------------
# Chunk 042 (Appendix R program.tex:845-856)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Preliminary analysis: quick summaries
# ------------------------------------------------------------------------------

# Summary of the whole dataset
summary(airquality)

# Mean and variance of temperature
mean(airquality$Temp)
var(airquality$Temp)

# Quantiles
quantile(airquality$Temp, probs = c(0.1, 0.5, 0.9), na.rm = TRUE)

# Frequency table for Month
table(airquality$Month)

# ------------------------------------------------------------------------------
# Chunk 043 (Appendix R program.tex:870-873)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Saving results and outputs
# Paragraph: R-native formats.
# ------------------------------------------------------------------------------

fit <- lm(Ozone ~ Temp + Wind, data = airquality)

saveRDS(fit, file = "output/fit_ozone_model.rds")
fit_loaded <- readRDS("output/fit_ozone_model.rds")

# ------------------------------------------------------------------------------
# Chunk 044 (Appendix R program.tex:877-882)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Saving results and outputs
# Paragraph: R-native formats.
# ------------------------------------------------------------------------------

dir.create("output", showWarnings = FALSE)

coef_fit <- coef(fit)
res_fit  <- resid(fit)

save(fit, coef_fit, res_fit, file = "output/model_objects.RData")

# ------------------------------------------------------------------------------
# Chunk 045 (Appendix R program.tex:889-894)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Saving results and outputs
# Paragraph: Tabular formats.
# ------------------------------------------------------------------------------

summary_df <- data.frame(
  term = names(coef_fit),
  estimate = as.numeric(coef_fit)
)

write.csv(summary_df, file = "output/coef_table.csv", row.names = FALSE)

# ------------------------------------------------------------------------------
# Chunk 046 (Appendix R program.tex:898-900)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Saving results and outputs
# Paragraph: Tabular formats.
# ------------------------------------------------------------------------------

# install.packages("writexl")
library(writexl)
write_xlsx(summary_df, path = "output/coef_table.xlsx")

# ------------------------------------------------------------------------------
# Chunk 047 (Appendix R program.tex:907-911)
# Section: R Programming Fundamentals
# Subsection: Basic dataset manipulation in R
# Subsubsection: Saving results and outputs
# Paragraph: Systematic file names.
# ------------------------------------------------------------------------------

spec <- "baseline"
year <- 1973

fname <- paste0("output/ozone_model_", spec, "_year_", year, ".rds")
saveRDS(fit, file = fname)

# ------------------------------------------------------------------------------
# Chunk 048 (Appendix R program.tex:932-946)
# Section: R Programming Fundamentals
# Subsection: Data visualization in R
# Subsubsection: Base graphics: common plot types
# ------------------------------------------------------------------------------

# Scatter plot: Ozone vs Temperature
plot(airquality$Temp, airquality$Ozone,
     xlab = "Temperature (F)",
     ylab = "Ozone",
     main = "Ozone and temperature (airquality)")

# Histogram of Wind
hist(airquality$Wind,
     xlab = "Wind",
     main = "Histogram of wind speed")

# Boxplot of temperature by month
boxplot(Temp ~ factor(Month), data = airquality,
        xlab = "Month", ylab = "Temperature (F)",
        main = "Temperature by month")

# ------------------------------------------------------------------------------
# Chunk 049 (Appendix R program.tex:954-961)
# Section: R Programming Fundamentals
# Subsection: Data visualization in R
# Subsubsection: Saving plots without embedding figures
# ------------------------------------------------------------------------------

dir.create("output/figures", recursive = TRUE, showWarnings = FALSE)

png("output/figures/R/ozone_vs_temp.png", width = 900, height = 650, 
     res = 120)
plot(airquality$Temp, airquality$Ozone,
     xlab = "Temperature (F)", ylab = "Ozone",
     main = "Ozone vs Temperature")
dev.off()

# ------------------------------------------------------------------------------
# Chunk 050 (Appendix R program.tex:969-977)
# Section: R Programming Fundamentals
# Subsection: Data visualization in R
# Subsubsection: ggplot2: a quick example
# ------------------------------------------------------------------------------

# install.packages("ggplot2")
library(ggplot2)

p <- ggplot(airquality, aes(x = Temp, y = Ozone)) +
  geom_point(na.rm = TRUE) +
  labs(x = "Temperature (F)", y = "Ozone",
       title = "Ozone vs Temperature (airquality)")

p

# ------------------------------------------------------------------------------
# Chunk 051 (Appendix R program.tex:983-984)
# Section: R Programming Fundamentals
# Subsection: Data visualization in R
# Subsubsection: ggplot2: a quick example
# ------------------------------------------------------------------------------

ggsave("output/figures/R/ozone_vs_temp_ggplot.png", plot = p,
       width = 7.5, height = 5.5, dpi = 150)

# ------------------------------------------------------------------------------
# Chunk 052 (Appendix R program.tex:1000-1000)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Help pages: your first stop
# ------------------------------------------------------------------------------

?runif

# ------------------------------------------------------------------------------
# Chunk 053 (Appendix R program.tex:1006-1006)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Help pages: your first stop
# ------------------------------------------------------------------------------

help(runif)

# ------------------------------------------------------------------------------
# Chunk 054 (Appendix R program.tex:1035-1035)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Running the examples directly
# ------------------------------------------------------------------------------

example(runif)

# ------------------------------------------------------------------------------
# Chunk 055 (Appendix R program.tex:1045-1046)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Quick checks: args(), formals(), and namespaces
# ------------------------------------------------------------------------------

args(runif)
formals(runif)

# ------------------------------------------------------------------------------
# Chunk 056 (Appendix R program.tex:1052-1052)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Quick checks: args(), formals(), and namespaces
# ------------------------------------------------------------------------------

stats::runif(5)

# ------------------------------------------------------------------------------
# Chunk 057 (Appendix R program.tex:1064-1065)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Searching for help when you do not know the function name
# Paragraph: Search by keyword in installed documentation.
# ------------------------------------------------------------------------------

??uniform
help.search("uniform")

# ------------------------------------------------------------------------------
# Chunk 058 (Appendix R program.tex:1072-1072)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Searching for help when you do not know the function name
# Paragraph: Search by partial name.
# ------------------------------------------------------------------------------

apropos("unif")

# ------------------------------------------------------------------------------
# Chunk 059 (Appendix R program.tex:1079-1080)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Searching for help when you do not know the function name
# Paragraph: Search in online documentation.
# ------------------------------------------------------------------------------

RSiteSearch("uniform distribution")
RSiteSearch("random effects")

# ------------------------------------------------------------------------------
# Chunk 060 (Appendix R program.tex:1090-1090)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Vignettes: longer, tutorial-style documentation
# ------------------------------------------------------------------------------

browseVignettes()

# ------------------------------------------------------------------------------
# Chunk 061 (Appendix R program.tex:1096-1096)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Vignettes: longer, tutorial-style documentation
# ------------------------------------------------------------------------------

browseVignettes(package = "ggplot2")

# ------------------------------------------------------------------------------
# Chunk 062 (Appendix R program.tex:1102-1102)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Vignettes: longer, tutorial-style documentation
# ------------------------------------------------------------------------------

vignette(package = "survival")

# ------------------------------------------------------------------------------
# Chunk 063 (Appendix R program.tex:1121-1125)
# Section: R Programming Fundamentals
# Subsection: Getting help in R (and in RStudio)
# Subsubsection: Online help pages and HTML vs. text help
# ------------------------------------------------------------------------------

# Open HTML help (if available)
help(runif, help_type = "html")

# Check how help is currently configured
getOption("help_type")
