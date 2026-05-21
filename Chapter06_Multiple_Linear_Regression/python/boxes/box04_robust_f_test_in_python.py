# Chapter 06, Python box 04: Robust $F$-test in Python
# Source label: box:pf_test_robust
# Full runnable chapter script: ../chapter06.py
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
ols_model_l_hc0 = ols_model_l.get_robustcov_results(cov_type="HC0", use_t=True)
ftest_rob = ols_model_l_hc0.f_test("new_production = 0, build_year = 0")

F_rob = float(ftest_rob.fvalue)
p_rob = float(ftest_rob.pvalue)
