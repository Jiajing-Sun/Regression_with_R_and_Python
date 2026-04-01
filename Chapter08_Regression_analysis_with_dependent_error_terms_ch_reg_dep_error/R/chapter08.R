# Extracted R code for Chapter 08: Regression analysis with dependent error terms
# Source: CH8 Regression with dependent errors.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Project Star and clustering in R
# Source lines: CH8 Regression with dependent errors.tex:95-139
# ------------------------------------------------------------------------------

# Load data
df <- read.csv(file.path("data", "star.csv"))

# NOTE (updated data schema):
# class_type  : class assignment (e.g. "SMALL", "REGULAR", "AIDE")
# class_id    : class/teacher identifier (cluster id)
# read_score  : grade 3 reading score (outcome)
# school_id   : school identifier (optional for multilevel models)

# Create treatment indicator: small_class
# 1 if SMALL, 0 if REGULAR/AIDE, NA otherwise
df$small_class <- ifelse(df$class_type == "SMALL", 1, NA)
df$small_class <- ifelse(df$class_type %in% c("AIDE", "REGULAR"), 0, df$small_class)

# Keep complete cases for outcome, regressor, and cluster id
df <- df[!is.na(df$class_id) & !is.na(df$read_score) & !is.na(df$small_class), ]

# Baseline regression
ols_model <- lm(read_score ~ small_class, data=df)

# Standard deviation of outcome (for standardized effect if desired)
sd(df$read_score, na.rm=TRUE)

# Robust and cluster-robust inference
library(lmtest)
library(sandwich)

# HC0 robust standard errors
coeftest(ols_model, vcov = vcovHC(ols_model, type="HC0"))

# Cluster-robust standard errors (clustered by class_id)
V_cl <- vcovCL(ols_model, cluster = df$class_id, type="HC0")
coeftest(ols_model, vcov = V_cl)

# Birth month example
ols_model2 <- lm(read_score ~ birth_month, data=df)
coeftest(ols_model2, vcov = vcovHC(ols_model2, type="HC0"))

V_cl2 <- vcovCL(ols_model2, cluster = df$class_id, type="HC0")
coeftest(ols_model2, vcov = V_cl2)

# Combined model
ols_model3 <- lm(read_score ~ small_class + birth_month, data=df)
V_cl3 <- vcovCL(ols_model3, cluster = df$class_id, type="HC0")
coeftest(ols_model3, vcov = V_cl3)

# ------------------------------------------------------------------------------
# Box 02: Project Star and multilevel models in R
# Source lines: CH8 Regression with dependent errors.tex:265-265
# ------------------------------------------------------------------------------

    install.packages(c("lme4"))

# ------------------------------------------------------------------------------
# Box 03: Project Star and multilevel models in R
# Source lines: CH8 Regression with dependent errors.tex:270-289
# ------------------------------------------------------------------------------

df <- read.csv(file.path("data", "star.csv"))

# Create treatment indicator
df$small_class <- ifelse(df$class_type == "SMALL", 1, NA)
df$small_class <- ifelse(df$class_type %in% c("AIDE", "REGULAR"), 0, df$small_class)

# Keep complete cases
df <- df[!is.na(df$class_id) & !is.na(df$read_score) & !is.na(df$small_class), ]

library(lme4)

# Random intercept by class (class_id)
multi_model1 <- lmer(read_score ~ small_class + (1 | class_id), data = df)
summary(multi_model1)

# Random intercept by class and school (if school_id exists / is non-missing)
# (If school_id has missing values, consider dropping them before fitting.)
df2 <- df[!is.na(df$school_id), ]
multi_model2 <- lmer(read_score ~ small_class + (1 | class_id) + (1 | school_id), data = df2)
summary(multi_model2)

# ------------------------------------------------------------------------------
# Box 04: The within estimator with municipal data in R
# Source lines: CH8 Regression with dependent errors.tex:483-506
# ------------------------------------------------------------------------------

df <- read.csv(file.path("data", "municip_data.csv"))
df <- df[df$municip_name != "Gotland", ]

library(plm)
library(lmtest)
library(sandwich)

within_model <- plm(
  tax_rate ~ left_coalition_last_term,
  effect = "individual",
  index = c("municip_name", "year"),
  data = df
)

coeftest(within_model, vcov = vcovHC(within_model, type="HC0", cluster="group"))

# Two-way FE (municipality + year)
twoway_model <- plm(
  tax_rate ~ left_coalition_last_term,
  effect = "twoways",
  index = c("municip_name", "year"),
  data = df
)
coeftest(twoway_model, vcov = vcovHC(twoway_model, type="HC0", cluster="group"))
