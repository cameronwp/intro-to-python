# External Libraries and Imports

Why did we start this lesson by creating a virtual environment? Because we want to work with libraries.

## What is a Library?

Libraries (or packages) are just collections of code written by other people. They may be in the [Python standard library](https://docs.python.org/3/library/), or they might be written by a 3rd party (like [numpy](https://numpy.org/)).

### Usage

Regardless of where the libarary is from, you'll use it in your code the same way with an `import` statement. There are generally three ways you can use an import statement:

1. Import the library as an object
2. Import 1+ specific exports from the library into the current namespace
3. Import everything from the library into the current namespace

Here are examples of all three.

```py
# 1. import the math standard library
# https://docs.python.org/3/library/math.html
import math

math.sqrt(4) # 2
math.cos(math.pi) # -1.0

# 2. import just the sqrt function
from math import sqrt

sqrt(4) # 2

# 3. import everything from math into the current namespace
from math import *

sqrt(4) # 2
ceil(3.3) # 4
floor(5.4) # 5
cos(pi) # -1.0
```

Methods 1 and 2 are used most often. Method 3 is nice when you want to use _all_ of the exports from a library, but it can be annoying otherwise because you'll be polluting your namespace with a lot of extraneous objects you aren't using.

### Installing 3rd Party Libraries

Standard libraries come with your Python installation, so you don't need to worry about installing them yourself. But you do need to install 3rd party libraries. For that, you'll use `pip`.

1. Activate your virtual environment (see the beginning of this lecture or README.md)
2. From the same shell, run `pip install libraryname`

If you run `pip install numpy`, for instance, you'll be able to use `numpy` in your code with the following import

```py
import numpy

numpy.array((1, 2))

# but more commonly, you'll see people rename the numpy import to something easier to type
import numpy as np

np.array((1, 2))
```

Try running `python part-5-imports/example.py` now. What do you see?

You're missing 3rd party packages. We can install all of them all at once! Many projects, including this one, will come with a `requirements.txt` file, which includes a list of packages and their versions that should be installed. To install all the packages from `requirements.txt`, make sure your virtual environment is active and run the following command from the root of the repo

```sh
pip install -r requirements.txt
```

You should see the packages getting installed. Once that's done, try running `python part-5-imports/example.py` again. You should see some plots show up.

Feel free to look through `example.py` and `environment.py` to see how they manage imports.

### Freezing Dependencies

If you're working on a Python project and you've added new dependencies, you should add them to your `requirements.txt` file. To do so, you can use the `pip freeze` command like so

```sh
pip freeze > requirements.txt
```

This will overwrite your old requirements.txt file with the new packages and the versions you have installed.
