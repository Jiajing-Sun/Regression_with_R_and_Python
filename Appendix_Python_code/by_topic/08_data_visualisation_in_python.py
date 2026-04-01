# Appendix Python subsection: Data Visualisation in Python
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001 (Appendix Python.tex:1254-1257)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

from pathlib import Path

FIG_DIR = Path("Your_Folder")
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------------------
# Chunk 002 (Appendix Python.tex:1263-1269)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import statsmodels.api as sm

co2_raw = sm.datasets.co2.load_pandas().data
co2_raw.head()
co2_raw.info()

co2_raw.index.min(), co2_raw.index.max()

# ------------------------------------------------------------------------------
# Chunk 003 (Appendix Python.tex:1275-1278)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import pandas as pd

co2 = co2_raw["co2"].resample("M").mean().dropna()
co2.head()

# ------------------------------------------------------------------------------
# Chunk 004 (Appendix Python.tex:1284-1287)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt

ax = co2.plot()
plt.show()

# ------------------------------------------------------------------------------
# Chunk 005 (Appendix Python.tex:1293-1301)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4))
plt.plot(co2.index, co2.values, linewidth=2)
plt.xlabel("Year")
plt.ylabel("CO2 concentration (ppm)")
plt.title("Atmospheric CO2 at Mauna Loa (monthly averages)")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Chunk 006 (Appendix Python.tex:1307-1315)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

plt.figure(figsize=(10, 4))
plt.plot(co2.index, co2.values, linewidth=2)
plt.xlabel("Year")
plt.ylabel("CO2 concentration (ppm)")
plt.title("Atmospheric CO2 at Mauna Loa (monthly averages)")
plt.tight_layout()

plt.savefig(FIG_DIR / "co2_timeseries_py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 007 (Appendix Python.tex:1334-1352)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame.copy()

# Make the data frame resemble the familiar R-style naming
df = df.rename(columns={
    "sepal length (cm)": "Sepal.Length",
    "sepal width (cm)":  "Sepal.Width",
    "petal length (cm)": "Petal.Length",
    "petal width (cm)":  "Petal.Width",
})

df["Species"] = df["target"].map(dict(enumerate(iris.target_names)))
df = df.drop(columns=["target"])

df.head()
df.describe()

# ------------------------------------------------------------------------------
# Chunk 008 (Appendix Python.tex:1360-1370)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.figure(figsize=(6.5, 4.8))
plt.hist(df["Sepal.Length"], bins=15, edgecolor="black")
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(FIG_DIR / "hist-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 009 (Appendix Python.tex:1376-1384)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

plt.figure(figsize=(6.5, 4.8))
plt.scatter(df["Sepal.Width"], df["Sepal.Length"], s=25)
plt.title("Sepal Width vs Sepal Length")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Sepal Length (cm)")
plt.tight_layout()

plt.savefig(FIG_DIR / "scatter-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 010 (Appendix Python.tex:1390-1401)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

species_order = sorted(df["Species"].unique())
data_by_species = [df.loc[df["Species"] == s, "Sepal.Length"] for s in species_order]

plt.figure(figsize=(6.5, 4.8))
plt.boxplot(data_by_species, labels=species_order)
plt.title("Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.tight_layout()

plt.savefig(FIG_DIR / "box-plot-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 011 (Appendix Python.tex:1407-1416)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

from pandas.plotting import scatter_matrix

cols = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]

axes = scatter_matrix(df[cols], figsize=(8, 8), diagonal="hist")
plt.suptitle("Scatterplot Matrix for Iris Measurements", y=1.02)
plt.tight_layout()

plt.savefig(FIG_DIR / "pair-plot-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 012 (Appendix Python.tex:1422-1435)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

import numpy as np

corr = df[cols].corr()

plt.figure(figsize=(6.5, 4.8))
plt.imshow(corr.values)
plt.xticks(range(len(cols)), cols, rotation=45, ha="right")
plt.yticks(range(len(cols)), cols)
plt.colorbar()
plt.title("Correlation Heatmap (Iris)")
plt.tight_layout()

plt.savefig(FIG_DIR / "correlation-iris-py.png", dpi=120)
plt.close()

# ------------------------------------------------------------------------------
# Chunk 013 (Appendix Python.tex:1441-1455)
# Section: Python Programming Fundamentals
# Subsection: Data Visualisation in Python
# Subsubsection: Saving figures to a fixed folder.
# ------------------------------------------------------------------------------

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D projection)

fig = plt.figure(figsize=(6.5, 4.8))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(df["Sepal.Length"], df["Sepal.Width"], df["Petal.Length"], s=20)

ax.set_title("3D Scatterplot: Sepal Length, Sepal Width, Petal Length")
ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Sepal Width (cm)")
ax.set_zlabel("Petal Length (cm)")

plt.tight_layout()
plt.savefig(FIG_DIR / "3d-iris-py.png", dpi=120)
plt.close()
