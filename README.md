# Regression with R and Python

*Description, Prediction, and Causal Inference for Applied Social Science and Econometrics*

This repository is the GitHub-ready computational companion to the textbook. It is designed for advanced undergraduate and beginning master's students in applied social sciences and econometrics who want a hands-on bridge between the printed text and runnable code.

The emphasis is on how regression supports descriptive, predictive, and causal questions in applied empirical work. It is therefore distinct from a machine-learning-first or computer-science-first regression text.

## What is included

- Extracted `R/` and `python/` scripts that follow the textbook code boxes in order.
- Box-level `R/boxes/` and `python/boxes/` snippets, with one file for each printed code box.
- A chapter-by-chapter reference R Markdown workbook for each substantive chapter.
- A separate chapter-by-chapter runnable R Markdown workbook for each substantive chapter.
- Appendix code split into reusable topic files.
- Chapter-level `data/` folders containing the CSV files used by the examples.

## Layout

- Each chapter folder contains a `README.md`, an `R/` script, a `python/` script, box-level snippet folders, a reference `.Rmd` workbook, and a runnable `.Rmd` workbook when R examples are available.
- Chapter `data/` folders contain the CSV files used by the examples.
- `Appendix_R_program_R_code/` contains one aggregate file plus section-level R appendix files.
- `Appendix_Python_code/` contains one aggregate file plus subsection-level Python appendix files.
- `render_rmarkdown_workbooks.R` renders all chapter `.Rmd` workbooks in one pass.

## How to run the materials

Run chapter scripts from the chapter folder, for example:

```sh
Rscript R/chapter06.R
python python/chapter06.py
```

The chapter scripts automatically use the local `data/` folder when one exists, so the printed textbook paths such as `apartment_price_data.csv` work without copying data files into the script folders.

The `R/boxes/` and `python/boxes/` files are the QR-code targets for the printed book. They mirror the corresponding printed code box; use the full chapter scripts when you want to run an entire chapter end-to-end.

For Python, install the companion requirements once:

```sh
python -m pip install -r requirements.txt
```

For R, the examples use base R plus common applied-econometrics packages such as `sandwich`, `lmtest`, `lme4`, `plm`, `ivreg`, `rdrobust`, `glmnet`, `rpart`, `rpart.plot`, and `rmarkdown`. Install missing packages once with `install.packages("package_name")`.

## Chapter folders

- `Chapter02_Covariation_in_data/`
- `Chapter03_Basic_probability_theory_and_statistical_inference_ch_probability_theory/`
- `Chapter04_Correlation_and_inference_about_a_population_ch_population_korrelation/`
- `Chapter05_The_simple_linear_regression_model/`
- `Chapter06_Multiple_Linear_Regression/`
- `Chapter07_Nonlinear_functional_form/`
- `Chapter08_Regression_analysis_with_dependent_error_terms_ch_reg_dep_error/`
- `Chapter09_Binary_dependent_variable_ch_logit/`
- `Chapter10_Prediction_ch_prediction/`
- `Chapter11_Nonparametric_Regression_chapter_nonparametric/`
- `Chapter12_Time_series_analysis/`
- `Chapter13_Causal_analyses_ch_causality/`

## Notes

- The generated scripts keep the textbook code content and ordering rather than rewriting examples.
- Shell-only installation commands from the Python appendix are omitted from `.py` files.
- Some appendix examples access external APIs or online data sources. Those examples may require an internet connection or an API key.
