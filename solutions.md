# Solutions to all the exercises in this repo

DON'T CHEAT! Make sure you're satisfied with your answer or you've exhausted all your options before looking at the solutions below.

## 1.1

```py
def hell_name(name):
    """
    Print "Hello, name!"
    """
    print(f"Hello, {name}!")
```

## 1.2

```py
def sine(opposite, hypoteneuse):
    """
    Calculate sine using the sides of a right triangle
    """
    return opposite / hypoteneuse
```

## 2.1

```py
def median(elements):
    """
    Returns the middle element. If the list has an even length, returns the lower index
    """
    half = len(elements) / 2
    if half % 1 != 0:
        half = half - 0.5
    return elements[int(half) - 1]
```

You could also use `math.floor`

```py
def median(elements):
    """
    Returns the middle element. If the list has an even length, returns the lower index
    """
    half = math.floor(len(elements) / 2)
    return elements[half - 1]
```

## 2.2

```py
def mean_and_median(numbers):
    """
    Get the mean and median of a list of numbers

    Params:
        numbers list of numbers
    Returns:
        mean float, median float tuple
    """
    mean = sum(numbers) / len(numbers)
    half = math.floor(len(numbers) / 2)
    median = numbers[half - 1]

    return mean, median
```

## 2.3

A numbered-key dictionary is useful when the number keys actually mean something. In the case of months, January is usually written as `1`, so it makes sense using `1` as a key for it. It could simplify operations like converting a date string such as `1/1/2022` into an English string like `January 1st, 2022`.

## 2.4

```py
university = {
    "name": "MIT",
    "location": "Cambridge, MA",
    "year_founded": 1861,
    "enrollment": {
        "undergrad": 4638,
        "grad": 7296
    }
}
```

## 3.1

Simple solution

```py
def old_school(universities):
    """
    Given a list of universities, return the number that are more than 150 years old

    Params:
        universities list of university objects with a "year_founded" property
    """
    num_old = 0
    for uni in universities:
        if 2022 - uni["year_founded"] > 150:
            # shorthand for num_old = num_old + 1
            num_old += 1
    return num_old
```

Advanced (with [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions))

```py
def old_school(universities):
    """
    Given a list of universities, return the number that are more than 150 years old

    Params:
        universities list of university objects with a "year_founded" property
    """
    # get the length of a new list that is filtered for old universities
    return len([
        uni for uni in universities
        # filters for old universities
        if 2022 - uni["year_founded"] > 150
    ])
```

## 3.2

```py
def fibo(n):
    """
    Produce the first n numbers of the Fibonacci sequence

    Params:
        n integer
    """
    result = []
    for i in range(n):
        if len(result) <= 1:
            result.append(1)
        else:
            prev1 = result[-1]
            prev2 = result[-2]
            result.append(prev1 + prev2)
    return result
```

## 3.3

```py
def ends_in_y(names):
    """
    Print names that end in 'y'

    Params
        names list of strings
    """
    for name in names:
        if name[-1] == "y":
            print(name)
```

## 3.4

```py
def mode(numbers):
    """
    Get the mode of a list of numbers

    Params:
        numbers list of numbers
    Returns:
        number
    """
    # create a dictionary of the number of times I've seen each number
    seen = {}
    for number in numbers:
        # defaults the number of times we've seen a number to 0, or gets the number of times we've seen it before
        curr = seen.setdefault(number, 0)
        # increment the number of times by 1
        seen[number] = curr + 1

    # the `max` function will give the biggest value in a collection. when we provide the `key` argument, we tell `max` what value to use when comparing to see what's biggest
    # try removing the `key=seen.get` to see what happens
    return max(seen, key=seen.get)
```

## 4

```py
class Dog:
    """
    An actual dog
    """

    def __init__(self, name, breed, is_female):
        """
        Set the properties of this dog
        """
        self.name = name
        self.breed = breed
        self.female = is_female
        self.location = None

    # ... same code as example

    def __str__(self):
        return f"{self.name}, {self.breed}"
```

## 5.1a

```py
import numpy as np

a = [2, 2, 2]
b = [4, 4, 4]

np.multiply(a, b)
```

## 5.1b

The easy way

```py
import numpy as np

np.ones((3, 2))
```

The hard way

```py
import numpy as np

np.array([[1, 1],
          [1, 1],
          [1, 1]])
```

## 5.1c

```py
import numpy as np

np.linspace(10, 20, num=4)
```

## 6

1. Does not handle the case when you have a number divisible by 10, eg. 20, 30, 40, etc.
2. `tens_digit = math.ceil(number / 10)` should be `tens_digit = math.floor(number / 10)`
3. `tens_place = tens[tens_digit - 1]` should be `tens_place = tens[tens_digit - 2]`
