# Lists and Dictionaries

## Lists

[Official intro to lists](https://docs.python.org/3/tutorial/introduction.html#lists)

Lists hold collections of items.

Literal lists are written with square brackets, `[ element0, element1, ... ]` with comma-separated elements. Elements can be of any type.

```py
subjects = ["algebra", "biology", "chemistry", "differential equations"]
print(subjects) # same list as above
```

**Lists are zero-indexed**. The first index in a list is 0. You can access elements in a list with square bracket notation.

```py
subjects[0] # algebra
subjects[4] # IndexError: list index out of range
```

You can access elements in a list going backwards using negative numbers, eg.

```py
subjects[-1] # "differential equations"
```

You can access a range of elements in a list using `[start:end]` notation to **slice** it. You will be returned a list

```py
subjects[1:3] # ['biology', 'chemistry']
```

You can have an implicit start or end by leaving it out but keeping the `:` when slicing a list. For instance, to get all elements _except_ the first one

```py
subjects[1:] # ['biology', 'chemistry', 'differential equations']
```

To get all elements except the last one

```py
subjects[:-1] # ['algebra', 'biology', 'chemistry']
```

You can even nest lists

```py
matrix = [[0, 1],
          [2, 3]]

matrix[0][1] # 1
matrix[1][0] # 2
```

You can change elements in a list

```py
subjects[1] = "botany"
subjects # ["algebra", "botany", "chemistry", "differential equations"]

matrix[1][1] = 4
matrix # [[0, 1], [2, 4]]
```

You can find out how many elements are in a list

```py
len(subjects) # 4
len(matrix) # 2
```

**Question for you**: why does `matrix` only have a length of 2?

### Looping over a List

We'll see more on this later. For now, try running

```py
for subject in subjects:
    print("I'm taking " + subject)

for row in matrix:
    # sum() is a built-in function that sums all the numbers passed to it
    print(sum(row))
```

## Exercise 1

Write a function that takes a list of elements and returns the median (middle) element. If the length of the list is even, return the median element with a lower index.

## Exercise 2

A tuple is basically a lighter-weight verion of a list, mainly used in function returns. You can write them with parenthesis, like `(element0, element1). Write a function that takes the following list of numbers and returns the mean and median in a tuple.

```py
list_of_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### Bonus

Now calculate the mode of the list in the same function.

## Dictionaries

Like lists, dictionaries hold collections of elements. Unlike lists, you can decide how to access each element using `{key: value}` syntax. A `key` represents the accessor of an element in a dictonary. The `value` is the information that is accessible through the `key`. This is a lookup operation, much like looking up a phone number in your contacts list. The name of your contact is the `key`, their phone number is the `value`.

Use curly bracket notation to build dictonaries.

```py
university = {"name": "MIT"}
print(university) # {'name': 'MIT'}
print(university["name"]) # 'MIT'
```

To enter multiple key-value pairs in a dictonary, separate them with commas.

```py
university = {"name": "MIT", "location": "Cambridge, MA", "year_founded": 1861, "enrollment": 11934}
university["location"] # "Cambridge, MA"
```

Note that you can mix and match any type of value. Use square bracket notation with keys to access elements in a dictionary

```py
university["enrollment"] # 11934
university["year_founded"] # 1861
university["mascot"] # KeyError: 'mascot'
```

You can add new key-value pairs after creating the dictionary.

```py
university["mascot"] = "Tim the Beaver"
print(university["mascot"]) # Tim the Beaver
```

You can change values after creating the dictonary.

```py
university["name"] = "Massachusetts Institute of Technology"
print(university["name"]) # 'Massachusetts Institute of Technology'
```

## Exercise 3

Values can also be dictionaries. Let's make the value held by the `"enrollment"` another dictionary that gives the undergrad and grad student enrollments separately. If your code is right, you should see the following:

```py
print(university["enrollment"]["undergrad"]) # 4638
print(university["enrollment"]["grad"]) # 7296

if university["enrollment"]["grad"] > 5000:
    print("there are more than 5,000 grad students")
```

(According to Wikipedia, MIT has 4,638 undergrads and 7,296 grad students.)

