# Chapter 07, R box 01: Air pollution and weather in R
# Source label: box:pollution_weather
# Full runnable chapter script: ../chapter07.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages(c("lmtest", "sandwich"))  # run once if needed
# --- Code block 2 ---
df <- read.csv("pollution_sf.csv")

# Aggregate PM2.5 by 10-degree wind-direction intervals.
df$wind_cat <- cut(df$wind_direction, breaks = seq(0, 360, by = 10),
                   include.lowest = TRUE)
df_agg <- aggregate(pm25 ~ wind_cat, data = df, FUN = mean)
df_agg$wind_direction <- seq(5, 355, 10)

# Direction and strength indicators.
df$land_wind <- ifelse(df$wind_direction > 330 | df$wind_direction <= 150, 1, 0)
df$strong_wind <- ifelse(df$wind_speed >= 3, 1, 0)
df$land_wind_strong_wind <- df$land_wind * df$strong_wind
df$land_wind_wind_speed <- df$land_wind * df$wind_speed

# Polynomial and interaction models.
ols_model_poly <- lm(pm25 ~ poly(wind_direction, 4), data = df)
ols_model1 <- lm(pm25 ~ land_wind, data = df)
ols_model2 <- lm(pm25 ~ land_wind + strong_wind + land_wind_strong_wind, data = df)
ols_model3 <- lm(pm25 ~ land_wind + wind_speed + land_wind_wind_speed, data = df)
# --- Code block 3 ---
library(lmtest)
library(sandwich)
coeftest(ols_model2, vcov = vcovHC(ols_model2, type = "HC0"))
