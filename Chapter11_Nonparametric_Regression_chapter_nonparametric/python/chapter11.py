"""Full Python script for Chapter 11: Nonparametric Regression."""

from importlib.util import find_spec
from pathlib import Path
import os
import runpy


ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

runpy.run_path(
    ROOT / "python" / "boxes" / "box01_regressogram_and_kernel_regression_in_python.py",
    run_name="__main__",
)

if find_spec("rdrobust") is not None:
    runpy.run_path(
        ROOT / "python" / "boxes" / "box02_nonparametric_rd_in_python.py",
        run_name="__main__",
    )
else:
    print("Skipping the RD box because the optional package rdrobust is not installed.")
