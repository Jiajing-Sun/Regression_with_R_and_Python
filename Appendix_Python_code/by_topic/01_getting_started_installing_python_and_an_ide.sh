# The Python Programming Language — Getting started: installing Python and an IDE
# Extracted from Appendix Python (1).tex

########################################################################
# Chunk 001 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Check that Python works.
########################################################################

python3 --version

########################################################################
# Chunk 002 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Check that Python works.
########################################################################

python --version

########################################################################
# Chunk 003 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: python: command not found on macOS.
########################################################################

python3 --version
python3 -m pip --version

########################################################################
# Chunk 004 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: python: command not found on macOS.
########################################################################

python3 -m pip install --upgrade pip

########################################################################
# Chunk 005 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: python: command not found on macOS.
########################################################################

python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip setuptools wheel

########################################################################
# Chunk 006 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: python: command not found on macOS.
########################################################################

brew --version
brew install python
python3 --version
python3 -m pip install --upgrade pip

########################################################################
# Chunk 007 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: python: command not found on macOS.
########################################################################

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

########################################################################
# Chunk 008 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Option 2: Jupyter notebooks (great for interactive learning).
########################################################################

python3 --version
python3 -m pip --version

########################################################################
# Chunk 009 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Option 2: Jupyter notebooks (great for interactive learning).
########################################################################

python3 -m venv ~/venvs/jupyter
source ~/venvs/jupyter/bin/activate
python -m pip install --upgrade pip
python -m pip install notebook

########################################################################
# Chunk 010 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Option 2: Jupyter notebooks (great for interactive learning).
########################################################################

python -m notebook

########################################################################
# Chunk 011 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Option 2: Jupyter notebooks (great for interactive learning).
########################################################################

source ~/venvs/jupyter/bin/activate
python -m notebook

########################################################################
# Chunk 012 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Installing packages with pip.
########################################################################

python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib statsmodels

########################################################################
# Chunk 013 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Installing packages with pip.
########################################################################

python3 -m pip install --upgrade pip
python3 -m pip install numpy pandas matplotlib statsmodels

########################################################################
# Chunk 014 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Recommended: use a virtual environment.
########################################################################

cd path/to/your/project
python3 -m venv .venv
source .venv/bin/activate

########################################################################
# Chunk 015 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Recommended: use a virtual environment.
########################################################################

python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib statsmodels

########################################################################
# Chunk 016 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Recommended: use a virtual environment.
########################################################################

cd path/to/your/project
source .venv/bin/activate

########################################################################
# Chunk 017 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Recommended: use a virtual environment.
########################################################################

deactivate

########################################################################
# Chunk 018 | Section: Python Programming Fundamentals | Subsection: Getting started: installing Python and an IDE | Paragraph: Alternatives.
########################################################################

brew install pipx
pipx ensurepath
pipx install <app-name>
