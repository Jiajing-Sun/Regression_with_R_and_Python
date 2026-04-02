# Regression with R and Python

## Subtitle

Description, Prediction, and Causal Analysis for Applied Social Science and Econometrics

This repository is the GitHub-ready computational companion to the textbook. It is designed for advanced undergraduate and beginning master's students in applied social sciences and econometrics who want a hands-on bridge between the printed text and runnable code.

The emphasis is on how regression supports descriptive, predictive, and causal questions in applied empirical work. It is therefore distinct from a machine-learning-first or computer-science-first regression text.

## What is included

- Extracted `R/` and `python/` scripts that follow the textbook code boxes in order.
- A chapter-by-chapter reference R Markdown workbook for each substantive chapter.
- A separate chapter-by-chapter runnable R Markdown workbook for each substantive chapter.
- Appendix code split into reusable topic files.

## Layout

- Each chapter folder contains a `README.md`, an `R/` script, a `python/` script, a reference `.Rmd` workbook, and a runnable `.Rmd` workbook when R examples are available.
- `Appendix_R_program_R_code/` contains one aggregate file plus section-level R appendix files.
- `Appendix_Python_code/` contains one aggregate file plus subsection-level Python appendix files.
- `render_rmarkdown_workbooks.R` renders all chapter `.Rmd` workbooks in one pass.

## Notes

- The generated scripts keep the textbook code content and ordering rather than rewriting examples.
- Shell-only installation commands from the Python appendix are omitted from `.py` files.
- Relative file paths and working-directory assumptions follow the textbook examples.
