# Control Flow

Control flow is the idea of deciding when, how, what, and how many times code should run

## `if` statements

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

## `for` loops

`for` loops allow you to repeat a statement some number of times. A common usage is

```py
for i in range(5):
    print(i) # 0 1 2 3 4
```

Here, we're asking python to loop over a list of numbers from 0 to 4. In its simplest form, the `range` function produces a list of numbers from 0 to the argument, exclusive. For [0, 5), this is `0, 1, 2, 3, 4`. ([See official docs on `range`](https://docs.python.org/3.3/library/stdtypes.html?highlight=range#range)).

You can also iterate over the elements in a list

```py
us_cities = ["Anaheim", "Boston", "Chicago", "Detroit", "El Paso"]

for city in us_cities:
    print(city + " is in the United States")
```

Alternatively, you can iterate over list indices

```py
for c in range(len(cities):
    # this uses f-string syntax
    # https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
    print(f"City {i}: {cities[i]}")
```

## `while` loops

`while` loops allow you to write code that keeps running until some condition is met. For example, the two loops below are equivalent

```py
for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i = i + 1 # don't forget or you'll have an infinite loop!
```

When you need to write a loop, `for` should be your first instinct, but a `while` loop can come in handy too.

## Exercise 3.1

Dictionaries can be elements in a list. Write a function that takes the given list of dictionaries and outputs the number of universities that are more than 150 years old.

```py
university_stats = [
    {
        "name": "MIT",
        "year_founded": 1861
    },
    {
        "name": "Harvard",
        "year_founded": 1636
    },
    {
        "name": "Vanderbilt",
        "year_founded": 1873
    },
    {
        "name": "Stanford",
        "year_founded": 1885
    },
    {
        "name": "Emory",
        "year_founded": 1836
    }
]
```

## Exercise 3.2

Write a for-loop to produce the first 10 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number).

## Exercise 3.3

You can slice strings, not just lists. Given the following list of names, print only the names that _end_ with a `"y"`.

```py
names = ["amy", "becky", "cyrano", "daisy", "evelyn", "franny", "ginny", "lydia"]
```

Head over to [part-4-objects-classes](./part-4-objects-classes/) to learn how to make your own types.
