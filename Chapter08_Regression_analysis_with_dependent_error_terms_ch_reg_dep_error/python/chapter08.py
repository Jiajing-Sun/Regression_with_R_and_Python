# Extracted Python code for Chapter 08: Regression analysis with dependent error terms
# Source: CH8 Regression with dependent errors.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Project Star and clustering in Python
# Source lines: CH8 Regression with dependent errors.tex:153-224
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# Load data
df = pd.read_csv("data/star.csv")

# NOTE (updated data schema):
# class_type  : class assignment (e.g. "SMALL", "REGULAR", "AIDE")
# class_id    : class/teacher identifier (cluster id)
# read_score  : grade 3 reading score (outcome)
# school_id   : school identifier (optional for multilevel models)

# Create treatment indicator: small_class
df["small_class"] = np.where(df["class_type"] == "SMALL", 1.0, np.nan)
df.loc[df["class_type"].isin(["AIDE", "REGULAR"]), "small_class"] = 0.0

# Keep complete cases for outcome, regressor, and cluster id
df = df.dropna(subset=["class_id", "read_score", "small_class"]).copy()

# Baseline regression
ols_model = smf.ols("read_score ~ small_class", data=df).fit()

beta_small = float(ols_model.params["small_class"])
sd_y = float(df["read_score"].std(ddof=1))
beta_small_std = beta_small / sd_y

# Robust (HC0) and clustered SE
ols_model_hc0 = ols_model.get_robustcov_results(cov_type="HC0", use_t=True)
ols_model_cl = ols_model.get_robustcov_results(
    cov_type="cluster",
    groups=df["class_id"],
    use_t=True
)

def coef_table(res):
    names = res.model.exog_names
    return pd.DataFrame(
        {"Estimate": np.asarray(res.params),
         "Std. Error": np.asarray(res.bse),
         "t": np.asarray(res.tvalues),
         "p-value": np.asarray(res.pvalues)},
        index=names,
    )

print(coef_table(ols_model))
print(coef_table(ols_model_hc0))
print(coef_table(ols_model_cl))

# Birth month example
ols_model2 = smf.ols("read_score ~ birth_month", data=df).fit()
ols_model2_hc0 = ols_model2.get_robustcov_results(cov_type="HC0", use_t=True)
ols_model2_cl = ols_model2.get_robustcov_results(
    cov_type="cluster",
    groups=df["class_id"],
    use_t=True
)

print(coef_table(ols_model2))
print(coef_table(ols_model2_hc0))
print(coef_table(ols_model2_cl))

# Combined model
ols_model3 = smf.ols("read_score ~ small_class + birth_month", data=df).fit()
ols_model3_cl = ols_model3.get_robustcov_results(
    cov_type="cluster",
    groups=df["class_id"],
    use_t=True
)

print(coef_table(ols_model3))
print(coef_table(ols_model3_cl))

# ------------------------------------------------------------------------------
# Box 02: Project Star and multilevel models in Python
# Source lines: CH8 Regression with dependent errors.tex:304-348
# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("data/star.csv")

# Create treatment indicator
df["small_class"] = np.where(df["class_type"] == "SMALL", 1.0, np.nan)
df.loc[df["class_type"].isin(["AIDE", "REGULAR"]), "small_class"] = 0.0

# Keep complete cases for class-level model
df = df.dropna(subset=["class_id", "read_score", "small_class"]).copy()

# Random intercept by class_id
multi_model1 = smf.mixedlm(
    "read_score ~ small_class",
    data=df,
    groups=df["class_id"]
).fit(reml=True)

print(multi_model1.summary())

sigma2_class = float(multi_model1.cov_re.iloc[0, 0])  # class-level variance
sigma2_u = float(multi_model1.scale)                  # residual variance
share_class = sigma2_class / (sigma2_class + sigma2_u)

# Add school random intercept via variance component (if school_id is available)
if "school_id" in df.columns and df["school_id"].notna().any():
    df2 = df.dropna(subset=["school_id"]).copy()

    multi_model2 = smf.mixedlm(
        "read_score ~ small_class",
        data=df2,
        groups=df2["class_id"],
        vc_formula={"school": "0 + C(school_id)"}
    ).fit(reml=True)

    print(multi_model2.summary())

    sigma2_class2 = float(multi_model2.cov_re.iloc[0, 0])
    sigma2_school2 = float(multi_model2.vcomp[0])
    sigma2_u2 = float(multi_model2.scale)

    share_class2 = sigma2_class2 / (sigma2_class2 + sigma2_school2 + sigma2_u2)
    share_school2 = sigma2_school2 / (sigma2_class2 + sigma2_school2 + sigma2_u2)

# ------------------------------------------------------------------------------
# Box 03: The within estimator with municipal data in Python
# Source lines: CH8 Regression with dependent errors.tex:520-543
# ------------------------------------------------------------------------------

import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

df = pd.read_csv("data/municip_data.csv")
df = df[df["municip_name"] != "Gotland"].copy()

# Create a (municipality, year) index
df_panel = df.set_index(["municip_name", "year"])

y = df_panel["tax_rate"]
X = sm.add_constant(df_panel[["left_coalition_last_term"]])

# Entity (municipality) FE with clustered SE by municipality
within_model = PanelOLS(y, X, entity_effects=True)
within_res = within_model.fit(cov_type="clustered", cluster_entity=True)

print(within_res.summary)

# Two-way FE (municipality + year)
twoway_model = PanelOLS(y, X, entity_effects=True, time_effects=True)
twoway_res = twoway_model.fit(cov_type="clustered", cluster_entity=True)

print(twoway_res.summary)
