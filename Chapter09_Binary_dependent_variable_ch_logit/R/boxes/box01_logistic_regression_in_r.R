# Chapter 09, R box 01: Logistic regression in R
# Source label: box:logit
# Full runnable chapter script: ../chapter09.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
df <- read.csv(file.path("data", "municip_data.csv"))
df <- df[df$year == 2022, ]

highest_quartile_limit <- quantile(df$tax_base, .75)
df$high_income <- ifelse(df$tax_base > highest_quartile_limit, 1, 0)
df$lnpop <- log(df$pop)

logit_model <- glm(high_income ~ share_tertiary_school,
                   family = binomial(link = "logit"), data = df)
logit_model2 <- glm(high_income ~ share_tertiary_school + lnpop,
                    family = binomial(link = "logit"), data = df)
summary(logit_model2)

beta1hat <- coef(logit_model2)["share_tertiary_school"]
exp(beta1hat * .01)
