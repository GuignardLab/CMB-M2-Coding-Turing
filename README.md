# CMB-M2-Coding-Turing <!-- omit in toc -->

- [1. Roadmap](#1-roadmap)
- [2. Goal of this course](#2-goal-of-this-course)
- [3. Technical pre-requisits](#3-technical-pre-requisits)
- [4. Back to basics of coding](#4-back-to-basics-of-coding)
  - [4.1. Variables](#41-variables)
  - [4.2. Data structures](#42-data-structures)
  - [4.3. Conditional statements \& loops](#43-conditional-statements--loops)
  - [4.4. Functions](#44-functions)
- [5. Classes](#5-classes)

## 1. Roadmap

- Recaps
  - Functions
  - Scripts
- What is a class?
- Why might we need classes?
- How to write a class in Python
- A class for the implementation of Turing patterns
- Bonus: Packaging your code

## 2. Goal of this course

This course aims at teaching the basics of classes using reaction diffusion simulations as a support, more specifically Turing like patterns. Understanding the mathematics or the biology behind Turing patterns is not necessary but it might help to understand better what is happening under the hood.

At the end of the course, I would like you to be able to write classes to do data analysis. Beginer to medium coding knowledge is required though I will do my best to not loose the least experienced ones on our way.

## 3. Technical pre-requisits

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
pip install numpy scipy matplotlib notebook # installing numpy, scipy matplotlib and jupyter notebook with pip
```

You should also download this repository via [GitHub](https://github.com/):

```shell
git clone https://github.com/GuignardLab/CMB-M2-Coding-Turing.git
```

Finally, if these steps are successful, you should be able to run the notebooks by first starting jupyter from the `CMB-M2-Coding-Turing` folder:

```shell
cd CMB-M2-Coding-Turing
jupyter notebook
```

and open the notebooks directly from the `notebook` folder.

## 4. Back to basics of coding

### 4.1. Variables

- What is a variable?
- What are the different types of variables?
  - `Integer`
  - `Float`
  - `String`
- Difference between compiled and interpreted?

### 4.2. Data structures

- What are data structures?
- What are they good for?
- Common data structures in Python:
  - `List`
  - `Tuple`
  - `Dictionary`
  - `Set`
  - `np.ndarray`
  - [...]

### 4.3. Conditional statements & loops

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

### 4.4. Functions

- What is a function?
  - name
  - arguments
  - return value
- What is it good for?

## 5. Classes

[Let's open a notebook now](notebooks/1.Classes.ipynb)
