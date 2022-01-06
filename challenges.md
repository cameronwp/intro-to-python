# Challenges

Here's a series of problems to practice perfecting your practical Python skills with the libraries you'll be using in the Momentum challenge.

Make sure you run `pip install -r requirements.txt` in your venv.

You are expected to use library documentation to solve these problems.

## 1 Array and Matrix Operations with Numpy

`numpy` ([official documentation](https://numpy.org/), [official tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html)) is the _de facto_ standard library for performing fast math in Python.

For the following problems, you'll be asked to perform the mathematical operations with Numpy. I'll give you starter code.

### 1a

Element-wise multiply two lists. Eg. `[2, 2, 2] * [4, 4, 4] == [8, 8, 8]` (this won't work with plain Python, FYI)

```py
import numpy as np

a = [2, 2, 2]
b = [4, 4, 4]

# your code here
```

### 1b

Create a 3x2 `np.array` made only of `1`s.

```py
import numpy as np

# your code here
```

### 1c

Use `np.linspace` to create an array of 4 evenly-spaced numbers between 10 and 20 inclusive.

```py
import numpy as np

# your code here

# result should be: [10., 13.33333333, 16.66666667, 20.]
```

## 2