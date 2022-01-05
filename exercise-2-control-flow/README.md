# Control Flow

Control flow is the idea of deciding when, how, what, and how many times code should run

## Deciding When

### `if` statements

Syntax: a set of `if`, `elif` (else if), and `else` blocks. The first condition that matches is run. `elif` can be repeated multiple times. If `else` is used, it must be the last block.

```py
# eg 1
if something is True:
    do_something()
elif something else is True:
    do_something_else()
elif some other thing is True:
    ...
else:
    print("none of the above blocks must have been True")

# eg 2
if True:
    do_something()

# eg 3
x = 4
if x < 3:
    print("x is less than 3")
elif x == 3:
    print("x equals 3")
else:
    print("x is greater than 3)

# eg 4
x = "momentum"
# if the first character is "a"
if x[0] == "a":
    print("starts with a")
elif x[0] == "b":
    print("starts with b")
elif x[0] == "c":
    print("starts with c")
else:
    print("it doesn't start with a, b, or c")
```

### `for` loops

`for` loops allow you to repeat a statement some number of times. A common usage is

```py
for i in range(5):
    print(i) # 0 1 2 3 4
```

The `range` function produces a list of numbers from 0 to the argument, exclusive. For [0, 5), this is 0, 1, 2, 3, 4