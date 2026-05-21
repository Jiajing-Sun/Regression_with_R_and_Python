# Chapter 09, R box 02: Example in R with the probability of heart disease
# Source label: box:logit_heart_disease
# Full runnable chapter script: ../chapter09.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
df <- read.csv(file.path("data", "heart_disease.csv"))
logit_model <- glm(heart_disease ~ blood_pressure,
                   family = binomial(link = "logit"), data = df)
std_bp <- sd(df$blood_pressure)
exp(confint.default(logit_model)["blood_pressure", ] * std_bp)

logit_model2 <- glm(heart_disease ~ blood_pressure + male + age,
                    family = binomial(link = "logit"), data = df)
beta <- coef(logit_model2)[c("blood_pressure", "male", "age")]
exp(beta * c(std_bp, 1, sd(df$age)))
predict(logit_model2,
        data.frame(blood_pressure = 140, male = 1, age = 50),
        type = "response")
# --- Code block 2 ---
p0 <- predict(logit_model2, type = "response")
risk_change <- function(var, delta) {
  df1 <- df; df1[[var]] <- df1[[var]] + delta
  p1 <- predict(logit_model2, newdata = df1, type = "response")
  c(GRR = mean(p1 / p0), GRD = mean(p1 - p0))
}
risk_change("blood_pressure", std_bp)
risk_change("age", sd(df$age))

df_female <- df; df_female$male <- 0
df_male <- df; df_male$male <- 1
p_female <- predict(logit_model2, newdata = df_female, type = "response")
p_male <- predict(logit_model2, newdata = df_male, type = "response")
c(GRR_male = mean(p_male / p_female), GRD_male = mean(p_male - p_female))
