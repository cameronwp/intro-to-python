# Hello, world!

## Basic Types and Operations

### Printing

`print(anything)`

`print("hello, world!")` prints `hello, world!`

### Comments

Comments are useful for explaining the reasoning behind your code

```py
print("this string is printed")

# this a comment. it won't run any code

# print("this won't be printed because it's commented out")
```

It's never a bad idea to leave a comment, but try to write comments that add information that someone might not be able to learn just by reading your code. For example, this isn't useful

```py
# checks if root is greater than 0
if root > 0:
    print("positive")
```

On the other hand, this might be more useful

```py
# the path is feasible because the first root of the quadratic is positive
if root > 0:
    print("positive")
```

### Strings

[Official intro to strings](https://docs.python.org/3/tutorial/introduction.html#strings)

Strings are `'single'` or `"double"` quoted sequences of characters. `""` is referred to as an empty string.

```py
print("This is a string")
```

Strings can be concatenated together

```py
print("M" + "I" + "T") # MIT
```

### Numbers

[Official intro to numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)

Integers do not have a decimal. Floating point numbers do. Generally, you want to use floating point numbers when you're doing actual math

`1` is the integer 1. `1.0` is the floating point number for 1

Normal mathematical operations work as expected:

```py
1 + 1 # 2
10 - 1 # 9
2.0 * 3.0 # 6.0
100 / 5 # 20
2**3 # 8
```

Python will change integers to floating point as necessary:

`10 / 3 # 3.333...`

As will be useful later when we do control flow, comparisons are also available:

```py
print(3 == 3) # True
print(3 < 3) # False
print(3 > 1) # True
print(3 >= 3) # True
print(3 != 3) # False
```

### Booleans + Boolean Logic

The two booleans are: `True` and `False` (note the capital letters)

You can use `and` and `or` to perform logical operations

```py
print(True and True) # True
print(True and False) # False
print(True or False) # True

if True and True:
    print("this is true")
```

### Variables

Variables are containers that hold values

```py
x = 2
y = 3
x**y # 8

name = "cameron"
print(name) # "cameron"
```

Variables can change values

```py
x = 1
print(x) # 1
x = 2
print(x) # 2
```

Variables are not strongly typed, but for your own sanity's sake, you should treat them as such. The following is legal Python, but a bad idea

```py
x = 1
print(x) # 1

x = "cameron"
print(x) # cameron
```

## Functions

Functions are useful for encapsulating related instructions into reasonable chunks that can be composed together. Imagine that you wanted to use the quadratic formula to get the roots of multiple quadratic equations. You could do it manually, like so

```py
import math

positive_root1 = (-b1 + math.sqrt(b1**2 - 4*a1*c1)) / (2 * a1)
negative_root1 = (-b1 - math.sqrt(b1**2 - 4*a1*c1)) / (2 * a1)

positive_root2 = (-b2 + math.sqrt(b2**2 - 4*a2*c2)) / (2 * a2)
negative_root2 = (-b2 - math.sqrt(b2**2 - 4*a2*c2)) / (2 * a2)

positive_root3 = (-b3 + math.sqrt(b3**2 - 4*a3*c3)) / (2 * a3)
negative_root3 = (-b3 - math.sqrt(b3**2 - 4*a3*c3)) / (2 * a3)

positive_root4 = (-b4 + math.sqrt(b4**2 - 4*a4*c4)) / (2 * a4)
negative_root4 = (-b4 - math.sqrt(b4**2 - 4*a4*c4)) / (2 * a4)
```

Or you could encapsulate the math into a reusable function to make your code simpler and easier to understand

```py
def quadatric_formula(a, b, c):
    """
    Returns a tuple of the [positive, negative] roots of a quadratic equation
    """
    positive_root = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    negative_root = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
    return positive_root, negative_root

roots1 = quadratic_eqn(a1, b1, c1)
roots2 = quadratic_eqn(a2, b2, c2)
roots3 = quadratic_eqn(a3, b3, c3)
roots4 = quadratic_eqn(a4, b4, c4)
```

The basic syntax of defining a function is:

```py
def function_name(argument1, argument2, ...):
    """
    Description of what this function is supposed to do
    """
    # do whatever you want
    value = "a value"
    return value
```

`return` indicates that the function will output (not print) a value, which you can use after you call the function. For example:

```py
def square(x):
    """
    Return the square of the input
    """
    return x**2

input_value = 4.0
# call the function and set a variable to the output of the function
output_value = square(input_value)
print(output_value) # 16.0
```

The basic syntax of calling a function is:

```py
value = function_name(parameter1, parameter2, ...) # if a function returns a value
function_name(parameter1, parameter2, ...) # if a function does not return a value
```

## Exercise 1.1

Write a function that takes someone's `name` as a string and prints `"Hello, {name}!"`

## Exercise 1.2

Write a function called `sine` that takes the length of the side opposite of an angle and hypoteneuse of a right triangle as arguments and returns the sine. You should be able to use it like so

```py
opposite = 3
hypoteneuse = 5
value = sine(opposite, hypoteneuse)
print(value) # 0.6
```

Next, you'll learn about collections of data in [part-2-lists-dictionaries](./part-2-lists-dictionaries.md).
