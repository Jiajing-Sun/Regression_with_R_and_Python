# Extracted R code for Chapter 07: Nonlinear functional form
# Source: CH7 Nonlinear functional form.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:419-419
# ------------------------------------------------------------------------------

    df <- read.csv("pollution_sf.csv")

# ------------------------------------------------------------------------------
# Box 02: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:423-425
# ------------------------------------------------------------------------------

 df$wind_cat <- cut(df$wind_direction,
 breaks=seq(0, 360, by=10),
 include.lowest=TRUE)

# ------------------------------------------------------------------------------
# Box 03: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:431-434
# ------------------------------------------------------------------------------

    df_agg <- aggregate(df$pm25,
                        by=list(wind_dir_interval=df$wind_cat),
                        FUN=mean)
    df_agg$wind_direction <- seq(5, 355, 10)

# ------------------------------------------------------------------------------
# Box 04: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:438-438
# ------------------------------------------------------------------------------

    names(df_agg)[names(df_agg) == "x"] <- "pm25_mean"

# ------------------------------------------------------------------------------
# Box 05: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:442-442
# ------------------------------------------------------------------------------

    plot(df_agg$wind_direction, df_agg$pm25_mean)

# ------------------------------------------------------------------------------
# Box 06: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:446-456
# ------------------------------------------------------------------------------

    df$north_wind <- ifelse(df$wind_direction > 315 |
                            df$wind_direction <= 45, 1, 0)
    df$east_wind <- ifelse(df$wind_direction > 45 &
                            df$wind_direction <= 135, 1, 0)
    df$south_wind <- ifelse(df$wind_direction > 135 &
                            df$wind_direction <= 225, 1, 0)
    df$west_wind <- ifelse(df$wind_direction > 225 &
                            df$wind_direction <= 315, 1, 0)
    df$land_wind <- ifelse(df$wind_direction > 330 |
                           df$wind_direction <= 150, 1, 0)
    df$strong_wind <- ifelse(df$wind_speed >= 3, 1, 0)

# ------------------------------------------------------------------------------
# Box 07: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:462-464
# ------------------------------------------------------------------------------

    df$wind_direction2 <- df$wind_direction^2
    df$wind_direction3 <- df$wind_direction^3
    df$wind_direction4 <- df$wind_direction^4

# ------------------------------------------------------------------------------
# Box 08: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:468-470
# ------------------------------------------------------------------------------

    ols_model_poly <- lm(pm25 ~ wind_direction +
      wind_direction2 + wind_direction3 +
      wind_direction4, data=df)

# ------------------------------------------------------------------------------
# Box 09: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:474-475
# ------------------------------------------------------------------------------

    ols_model_poly_alt <- lm(pm25 ~ 
      poly(wind_direction, 4), data=df)

# ------------------------------------------------------------------------------
# Box 10: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:479-479
# ------------------------------------------------------------------------------

    newdata <- data.frame(wind_direction=seq(0, 360, 1))

# ------------------------------------------------------------------------------
# Box 11: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:484-484
# ------------------------------------------------------------------------------

 newdata$pred <- predict(ols_model_poly_alt, newdata)

# ------------------------------------------------------------------------------
# Box 12: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:488-492
# ------------------------------------------------------------------------------

    newdata$pred_alt <- coef(ols_model_poly)[1] +
      coef(ols_model_poly)[2] * newdata$wind_direction +
      coef(ols_model_poly)[3] * newdata$wind_direction^2 +
      coef(ols_model_poly)[4] * newdata$wind_direction^3 +
      coef(ols_model_poly)[5] * newdata$wind_direction^4

# ------------------------------------------------------------------------------
# Box 13: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:496-497
# ------------------------------------------------------------------------------

 plot(df_agg$wind_direction, df_agg$pm25_mean)
 lines(newdata$wind_direction, newdata$pred)

# ------------------------------------------------------------------------------
# Box 14: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:501-502
# ------------------------------------------------------------------------------

 df$land_wind_strong_wind <- df$land_wind * df$strong_wind
 df$land_wind_wind_speed <- df$land_wind * df$wind_speed

# ------------------------------------------------------------------------------
# Box 15: Air pollution and weather in R
# Source lines: CH7 Nonlinear functional form.tex:506-515
# ------------------------------------------------------------------------------

    library("lmtest")
    library("sandwich")
    ols_model1 <- lm(pm25 ~ land_wind, data=df)
    ols_model2 <- lm(pm25 ~ land_wind + strong_wind +
                     land_wind_strong_wind, data=df)
    ols_model3 <- lm(pm25 ~ land_wind + wind_speed +
                     land_wind_wind_speed, data=df)
    coeftest(ols_model1, vcov=vcovHC(ols_model1, type="HC0"))
    coeftest(ols_model2, vcov=vcovHC(ols_model2, type="HC0"))
    coeftest(ols_model3, vcov=vcovHC(ols_model3, type="HC0"))
