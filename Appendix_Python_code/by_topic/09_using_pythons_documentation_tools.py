# Appendix Python subsection: Using Python's documentation tools
# Source: Appendix Python.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Using Python's documentation tools
# ------------------------------------------------------------------------------

import numpy as np

help(np.random.Generator.uniform)

# ------------------------------------------------------------------------------
# Chunk 002
# Chapter: The Python Programming Language
# Section: Python Programming Fundamentals
# Subsection: Using Python's documentation tools
# ------------------------------------------------------------------------------

import inspect
import textwrap
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

FIG_DIR = Path("Your_Folder")
FIG_DIR.mkdir(parents=True, exist_ok=True)

doc = inspect.getdoc(np.random.Generator.uniform)
doc_lines = doc.splitlines()
excerpt = "\n".join(doc_lines[:40])   # keep it short for a figure

# Wrap long lines for readability
excerpt = "\n".join(textwrap.fill(line, width=95) for line in excerpt.splitlines())

fig = plt.figure(figsize=(10, 6))
fig.text(0.01, 0.99, excerpt, va="top", ha="left", family="monospace", fontsize=8)
plt.axis("off")

plt.savefig(FIG_DIR / "help-uniform-python.png", dpi=150, bbox_inches="tight")
plt.close()
