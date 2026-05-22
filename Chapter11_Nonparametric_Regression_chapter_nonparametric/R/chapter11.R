# Full R script for Chapter 11: Nonparametric Regression
# Run from the chapter folder, or run this file directly with Rscript.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_file <- normalizePath(sub("^--file=", "", file_arg[1]))
  setwd(normalizePath(file.path(dirname(script_file), "..")))
}

source(file.path("R", "boxes", "box01_regressogram_and_kernel_regression_in_r.R"))

rd_packages <- c("sandwich", "lmtest", "rdrobust")
have_rd_packages <- all(vapply(rd_packages, requireNamespace,
                               quietly = TRUE, FUN.VALUE = logical(1)))

if (have_rd_packages) {
  source(file.path("R", "boxes", "box02_nonparametric_rd_in_r.R"))
} else {
  message(
    "Skipping the RD box because one or more optional packages are missing: ",
    paste(rd_packages, collapse = ", ")
  )
}
