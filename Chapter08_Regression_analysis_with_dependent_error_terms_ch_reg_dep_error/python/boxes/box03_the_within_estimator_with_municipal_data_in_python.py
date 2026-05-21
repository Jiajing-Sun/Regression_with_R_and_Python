# Chapter 08, Python box 03: The within estimator with municipal data in Python
# Source label: box:pwithin_estimator
# Full runnable chapter script: ../chapter08.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# One-time install: python -m pip install pandas statsmodels linearmodels
# --- Code block 2 ---
import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

df = pd.read_csv("data/municip_data.csv")
df = df[df["municip_name"] != "Gotland"].copy()
df_panel = df.set_index(["municip_name", "year"])

y = df_panel["tax_rate"]
X = sm.add_constant(df_panel[["left_coalition_last_term"]])

within_res = PanelOLS(y, X, entity_effects=True).fit(
    cov_type="clustered", cluster_entity=True
)
twoway_res = PanelOLS(y, X, entity_effects=True, time_effects=True).fit(
    cov_type="clustered", cluster_entity=True
)
print(within_res.summary)
print(twoway_res.summary)
