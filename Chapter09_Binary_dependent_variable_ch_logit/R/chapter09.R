# Extracted R code for Chapter 09: Binary dependent variable
# Source: CH9 Binary dependent variable.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Logistic regression in R
# Source lines: CH9 Binary dependent variable.tex:316-317
# ------------------------------------------------------------------------------

 df <- read.csv("municip_data.csv")
 df <- df[df$year == 2022, ]

# ------------------------------------------------------------------------------
# Box 02: Logistic regression in R
# Source lines: CH9 Binary dependent variable.tex:321-321
# ------------------------------------------------------------------------------

    highest_quartile_limit <- quantile(df$tax_base, .75)

# ------------------------------------------------------------------------------
# Box 03: Logistic regression in R
# Source lines: CH9 Binary dependent variable.tex:325-326
# ------------------------------------------------------------------------------

 df$high_income <- ifelse(
 df$tax_base > highest_quartile_limit, 1, 0)

# ------------------------------------------------------------------------------
# Box 04: Logistic regression in R
# Source lines: CH9 Binary dependent variable.tex:330-332
# ------------------------------------------------------------------------------

    logit_model <- glm(df$high_income ~ share_tertiary_school,
                       family = binomial(link = "logit"),
                       data=df)

# ------------------------------------------------------------------------------
# Box 05: Logistic regression in R
# Source lines: CH9 Binary dependent variable.tex:336-336
# ------------------------------------------------------------------------------

 summary(logit_model)

# ------------------------------------------------------------------------------
# Box 06: Logistic regression in R
# Source lines: CH9 Binary dependent variable.tex:340-343
# ------------------------------------------------------------------------------

    df$lnpop <- log(df$pop)
    logit_model2 <- glm(df$high_income ~ 
      share_tertiary_school + lnpop,
      family = binomial(link = "logit"), data=df)

# ------------------------------------------------------------------------------
# Box 07: Logistic regression in R
# Source lines: CH9 Binary dependent variable.tex:349-350
# ------------------------------------------------------------------------------

    beta1hat <- logit_model2$coefficients[2]
    beta2hat <- logit_model2$coefficients[3]

# ------------------------------------------------------------------------------
# Box 08: Logistic regression in R
# Source lines: CH9 Binary dependent variable.tex:358-358
# ------------------------------------------------------------------------------

 exp(beta1hat * .01)

# ------------------------------------------------------------------------------
# Box 09: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:488-492
# ------------------------------------------------------------------------------

    df <- read.csv("heart_disease.csv")
    logit_model <- glm(df$heart_disease ~ blood_pressure,
                       family = binomial(link = "logit"),
                       data=df)
    summary(logit_model)

# ------------------------------------------------------------------------------
# Box 10: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:496-507
# ------------------------------------------------------------------------------

    sum_logit_model <- summary(logit_model)$coefficients
    beta_1_hat <- sum_logit_model["blood_pressure", "Estimate"]
    se_beta_1_hat <- sum_logit_model[
      "blood_pressure", "Std. Error"]
    std_dev_blood_pressure <- sd(df$blood_pressure)
    alpha <- .05
    zstat <- qnorm(1-alpha/2)
    lb_beta_1_hat <- beta_1_hat - zstat * se_beta_1_hat
    ub_beta_1_hat <- beta_1_hat + zstat * se_beta_1_hat
    lb_odds_ratio <- exp(lb_beta_1_hat * std_dev_blood_pressure)
    ub_odds_ratio <- exp(ub_beta_1_hat * std_dev_blood_pressure)
    print(c(lb_odds_ratio, ub_odds_ratio))

# ------------------------------------------------------------------------------
# Box 11: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:521-523
# ------------------------------------------------------------------------------

    logit_model2 <- glm(df$heart_disease ~ blood_pressure +
      male + age, family = binomial(link = "logit"), data=df)
    summary(logit_model2)

# ------------------------------------------------------------------------------
# Box 12: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:526-535
# ------------------------------------------------------------------------------

    sum_logit_model2 <- summary(logit_model2)$coefficients
    beta_1_hat_b <- sum_logit_model2[
      "blood_pressure", "Estimate"]
    beta_2_hat_b <- sum_logit_model2["male", "Estimate"]
    beta_3_hat_b <- sum_logit_model2["age", "Estimate"]
    std_dev_age <- sd(df$age)
    odds_ratio_blood_pressure <- exp(beta_1_hat_b *
                                     std_dev_blood_pressure)
    odds_ratio_male <- exp(beta_2_hat_b * 1)
    odds_ratio_age <- exp(beta_3_hat_b * std_dev_age)

# ------------------------------------------------------------------------------
# Box 13: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:539-541
# ------------------------------------------------------------------------------

    beta_hat_b <- sum_logit_model2[, "Estimate"][2:4]
    increases <- c(std_dev_blood_pressure, 1, std_dev_age)
    odds_ratios <- exp(beta_hat_b * increases)

# ------------------------------------------------------------------------------
# Box 14: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:546-549
# ------------------------------------------------------------------------------

    beta_0_hat_b <- sum_logit_model2["(Intercept)", "Estimate"]
    pred_heart_disease <- 1 / (1 + exp(-(
      beta_0_hat_b + beta_1_hat_b * 140 + beta_2_hat_b * 1 +
      beta_3_hat_b * 50)))

# ------------------------------------------------------------------------------
# Box 15: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:553-555
# ------------------------------------------------------------------------------

 pred_heart_disease_alt <- predict(logit_model2,
 data.frame(blood_pressure=140, male=1, age=50),
 type="response")

# ------------------------------------------------------------------------------
# Box 16: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:561-561
# ------------------------------------------------------------------------------

    df$pred <- predict(logit_model2, type="response")

# ------------------------------------------------------------------------------
# Box 17: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:565-570
# ------------------------------------------------------------------------------

    df_incr_blood_pressure <- df
    df_incr_blood_pressure$blood_pressure <- 
      df_incr_blood_pressure$blood_pressure + 
      std_dev_blood_pressure
    df_incr_blood_pressure$pred <- predict(logit_model2,
      newdata=df_incr_blood_pressure, type="response")

# ------------------------------------------------------------------------------
# Box 18: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:574-577
# ------------------------------------------------------------------------------

 df$risk_ratio_blood_pressure <-
 df_incr_blood_pressure$pred / df$pred
 df$risk_diff_blood_pressure <-
 df_incr_blood_pressure$pred - df$pred

# ------------------------------------------------------------------------------
# Box 19: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:581-582
# ------------------------------------------------------------------------------

 GRR_blood_pressure <- mean(df$risk_ratio_blood_pressure)
 GRD_blood_pressure <- mean(df$risk_diff_blood_pressure)

# ------------------------------------------------------------------------------
# Box 20: Example in R with the probability of heart disease
# Source lines: CH9 Binary dependent variable.tex:586-597
# ------------------------------------------------------------------------------

    df_female <- df
    df_female$male <- 0
    df_male <- df
    df_male$male <- 1
    df_female$pred <- predict(logit_model2, newdata=df_female,
                              type="response")
    df_male$pred <- predict(logit_model2, newdata=df_male,
                            type="response")
    df$risk_ratio_male <- df_male$pred / df_female$pred
    df$risk_diff_male <- df_male$pred - df_female$pred
    GRR_male <- mean(df$risk_ratio_male)
    GRD_male <- mean(df$risk_diff_male)
