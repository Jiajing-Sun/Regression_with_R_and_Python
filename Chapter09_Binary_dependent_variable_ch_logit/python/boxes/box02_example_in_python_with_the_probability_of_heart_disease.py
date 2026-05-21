# Chapter 09, Python box 02: Example in Python with the probability of heart disease
# Source label: box:plogit_heart_disease
# Full runnable chapter script: ../chapter09.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install numpy pandas statsmodels scipy
# --- Code block 2 ---
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv("data/heart_disease.csv")
logit_model = smf.glm("heart_disease ~ blood_pressure", data=df,
    family=sm.families.Binomial(link=sm.families.links.logit())).fit()
std_bp = df["blood_pressure"].std(ddof=1)
print(np.exp(logit_model.conf_int().loc["blood_pressure"] * std_bp))

logit_model2 = smf.glm("heart_disease ~ blood_pressure + male + age", data=df,
    family=sm.families.Binomial(link=sm.families.links.logit())).fit()
increases = np.array([std_bp, 1.0, df["age"].std(ddof=1)])
print(np.exp(logit_model2.params[["blood_pressure", "male", "age"]] * increases))
case = pd.DataFrame({"blood_pressure": [140], "male": [1], "age": [50]})
print(logit_model2.predict(case).iloc[0])
# --- Code block 3 ---
p0 = logit_model2.predict(df)
def risk_change(var, delta):
    df1 = df.copy(); df1[var] = df1[var] + delta
    p1 = logit_model2.predict(df1)
    return {"GRR": float((p1 / p0).mean()), "GRD": float((p1 - p0).mean())}
print(risk_change("blood_pressure", std_bp))
print(risk_change("age", df["age"].std(ddof=1)))

df_female = df.copy(); df_female["male"] = 0
df_male = df.copy(); df_male["male"] = 1
p_female = logit_model2.predict(df_female)
p_male = logit_model2.predict(df_male)
print({"GRR_male": float((p_male / p_female).mean()),
       "GRD_male": float((p_male - p_female).mean())})
