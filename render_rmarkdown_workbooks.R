# Render all chapter R Markdown workbooks in place.
if (!requireNamespace("rmarkdown", quietly = TRUE)) {
  stop("Please install the rmarkdown package before rendering the workbooks.")
}

workbooks <- c(
  "Chapter02_Covariation_in_data/chapter02_workbook.Rmd",
  "Chapter03_Basic_probability_theory_and_statistical_inference_ch_probability_theory/chapter03_workbook.Rmd",
  "Chapter04_Correlation_and_inference_about_a_population_ch_population_korrelation/chapter04_workbook.Rmd",
  "Chapter05_The_simple_linear_regression_model/chapter05_workbook.Rmd",
  "Chapter06_Multiple_Linear_Regression/chapter06_workbook.Rmd",
  "Chapter07_Nonlinear_functional_form/chapter07_workbook.Rmd",
  "Chapter08_Regression_analysis_with_dependent_error_terms_ch_reg_dep_error/chapter08_workbook.Rmd",
  "Chapter09_Binary_dependent_variable_ch_logit/chapter09_workbook.Rmd",
  "Chapter10_Prediction_ch_prediction/chapter10_workbook.Rmd",
  "Chapter11_Time_series_analysis/chapter11_workbook.Rmd",
  "Chapter12_Causal_analyses_ch_causality/chapter12_workbook.Rmd",
  "Chapter13_Nonparametric_Regression_chapter_nonparametric/chapter13_workbook.Rmd"
)

for (workbook in workbooks) {
  rmarkdown::render(
    workbook,
    output_dir = dirname(workbook),
    envir = new.env(parent = globalenv())
  )
}
