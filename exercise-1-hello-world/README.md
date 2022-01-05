# Hello, world!

## Basic Types and Operations

### Printing

`print(anything)`

`print("hello, world!")` prints `hello, world!`

### Comments

`# this a comment. it won't run any code`

### Strings

`'Single'` or `"double"` quoted

### Numbers

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

## Exercise

Write a function that takes someone name as a string and prints `"Hello, {name}!"`
