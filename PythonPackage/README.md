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

## NumPy

### Benefits of using NumPy

Even though Python lists are great on their own, NumPy has a number of key features that give it great advantages over Python lists. Below are a few convincingly strong features:

One such feature is speed. When performing operations on large arrays NumPy can often perform several orders of magnitude faster than Python lists. This speed comes from the nature of NumPy arrays being memory-efficient and from optimized algorithms used by NumPy for doing arithmetic, statistical, and linear algebra operations.

Another great feature of NumPy is that it has multidimensional array data structures that can represent vectors and matrices. You will learn all about vectors and matrices in the Linear Algebra section of this course later on, and as you will soon see, a lot of machine learning algorithms rely on matrix operations. For example, when training a Neural Network, you often have to carry out many matrix multiplications. NumPy is optimized for matrix operations and it allows us to do Linear Algebra operations effectively and efficiently, making it very suitable for solving machine learning problems.

Another great advantage of NumPy over Python lists is that NumPy has a large number of optimized built-in mathematical functions. These functions allow you to do a variety of complex mathematical computations very fast and with very little code (avoiding the use of complicated loops) making your programs more readable and easier to understand.

These are just some of the key features that have made NumPy an essential package for scientific computing in Python. In fact, NumPy has become so popular that a lot of Python packages, such as Pandas, are built on top of NumPy.
