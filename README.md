# An Advanced, Practical Intro to Python - Momentum Lecture IAP 2022

## Introduction

### Additional Resources

* https://docs.python.org/3/tutorial/

### Development Environment - Installation

1. Install Visual Studio Code aka VS Code aka VSCode aka Code: [](https://code.visualstudio.com/)
2. Make sure you have Python 3 installed:
  a. MacOS/Linux: `which python` (you probably already have it installed). If you get Python 2, try `which python3` and then use `python3` for the rest of this lecture
  b. Windows: TODO

### Development Environment - virtual env

A Python virtual environment (venv) makes it easy to manage dependencies across projects. Dependencies will be installed within the project directory, instead of globally, allowing different projects to independently track different versions of dependencies

1. Go to your project directory: `cd your/project/directory`
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `./.venv/bin/activate`
4. If you want to leave your virtual environment: `deactivate`

For the future, any time you want to use your venv, just use steps 1 and 3.

### venv in a little more detail

You'll notice a new directory, `.venv`, that includes symlinks to `python` and `pip`

Calling `.venv/bin/activate` modifies your Python environment in your current shell session. `deactivate` undoes the modifications

When you `pip install package`, the package is installed to the `.venv` directory

When you `import package`, it will first check your `.venv` directory

## How to Run Python

1. Call `python` against a Python file: `python path/to/python/file.py`
  * Runs your code all in one shot
2. Use the Python interpreter by itself: `python`
  * Runs your code line-by-line as you press enter
3. Jupyter notebook. This is out of scope for this lecture, but it's a great way to tell a story with Python

I will be using VS Code with its integrated terminal from now on.

To get started, head over to [part-1-hello-world.md](./part-1-hello-world.md).

## More Practice

Want to keep practicing Python? Here's an incomplete list of some great resources.

### Challenges

1. [Advent of Code](https://adventofcode.com) - a coding competition every December (but available year round) with holiday themed challenges
2. [Code Kata](http://codekata.com/)
3. [Project Euler](https://projecteuler.net/)
4. [Codewars](https://www.codewars.com/)

### Books and Courses

1. [Think Python](https://greenteapress.com/wp/think-python-2e/)
2. [6.001 on MIT OCW](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)