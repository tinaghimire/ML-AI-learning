# Python Packages

## Anaconda

- Anaconda is a program to manage (install, upgrade, or uninstall) packages and environments to use with Python. It's simple to install packages with Anaconda and create virtual environments to work on multiple projects conveniently.

conda create -n tea_facts python=3 -- tea_facts is a name of project
conda create -n my_env python=3.7 numpy Keras
conda env create -f environment.yaml

source activate tea_facts
conda list
conda env list
conda env remove -n env_name
conda info --envs

conda install numpy pandas matplotlib
conda install jupyter notebook
conda --version
conda install numpy scipy pandas
conda remove PACKAGE_NAME
conda update package_name
conda search *SEARCH_TERM*
conda env export > environment.yaml

**Share the list of dependencies**
pip freeze > requirements.txt
pip install -r requirements.txt

[](https://conda.io/projects/conda/en/latest/commands/index.html)

## Jupyter Notebook

- pip install nbconvert
- jupyter nbconvert --to FORMAT mynotebook.ipynb
The currently supported output FORMAT could be either of the following (ignore case):

HTML,
LaTeX,
PDF,
WebPDF,
Reveal.js HTML slideshow,
Markdown,
Ascii,
reStructuredText,
executable script,
notebook.
