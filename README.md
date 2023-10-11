# CMB-M2-Coding-Turing <!-- omit in toc -->

- [1. Goal of this course](#1-goal-of-this-course)
- [2. Technical pre-requisits](#2-technical-pre-requisits)
- [3. Back to basics of coding](#3-back-to-basics-of-coding)
  - [3.1. Variables](#31-variables)
  - [3.2. Data structures](#32-data-structures)
  - [3.3. Conditional statements \& loops](#33-conditional-statements--loops)
  - [3.4. Functions](#34-functions)
- [4. Classes](#4-classes)

## 1. Goal of this course

This course aims at teaching the basics of classes using reaction diffusion simulations as a support, more specifically Turing like patterns. Understanding the mathematics or the biology behind Turing patterns is not necessary but it might help to understand better what is happening under the hood.

At the end of the course, I would like you to be able to write classes to do data analysis. Beginer to medium coding knowledge is required though I will do my best to not loose the least experienced ones on our way.

## 2. Technical pre-requisits

To follow this course, on top of having an idea of what is coding and what are Turing patterns, the following softwares and libraries are necessary:

- Python
- A virtual environment manager such as [miniconda](https://docs.conda.io/projects/miniconda/en/latest/index.html) (Please avoid using Anaconda!)
- Few Python libraries:
  - [numpy](https://www.numpy.org)
  - [scipy](https://www.scipy.org)
  - [matplotlib](https://www.matplotlib.org)
- And one way to run jupyter notebooks, for example [Jupyter notebooks](https://jupyter.org/)

Probably the better way to run this course is by creating an environment dedicated to it, installing the pre-requisits within that dedicated environment and run the course from there.

This succession of commands could lead you to the correct install if you are with Linux or MacOs distributions (assuming [miniconda](https://docs.conda.io/projects/miniconda/en/latest/index.html) installed):

```shell
conda create -n M2-CT python=3.10 # Creating an environment with Python 3.10
                                  # named M2-CT
conda activate M2-CT # activate the environment
conda install pip # install pip in the environment (it should already be the case but one never knows ...)
```

You should also download this repository via [GitHub](https://github.com/GuignardLab/CMB-M2-Coding-Turing):

```shell
git clone https://github.com/GuignardLab/CMB-M2-Coding-Turing.git
```

Then, you can install the required libraries from the freshly downloaded folder:

```shell
cd CMB-M2-Coding-Turing
pip install .
```

The last command should install numpy, scipy, matplotlib and the jupyter notebook.

Finally, if these steps are successful, you should be able to run the notebooks by first starting jupyter from the `CMB-M2-Coding-Turing` folder:

```shell
jupyter notebook
```

and open the notebooks directly from the `notebook` folder.

## 3. Back to basics of coding

### 3.1. Variables

- What is a variable?
- What are the different types of variables?
  - `Integer`
  - `Float`
  - `String`
- Difference between compiled and interpreted?

### 3.2. Data structures

- What are data structures?
- What are they good for?
- Common data structures in Python:
  - `List`
  - `Tuple`
  - `Dictionary`
  - `Set`
  - `np.ndarray`
  - [...]

### 3.3. Conditional statements & loops

- What are conditional statements?
- Bread and butter of coding
- Common conditional statements:
  - `if`
  - `else`
  - `elif`
- What are loops?
- Common loops:
  - `for`
  - `while`

### 3.4. Functions

- What is a function?
  - name
  - arguments
  - return value
- What is it good for?

## 4. Classes

[Let's open a notebook now](notebooks/0.Functions.ipynb)
