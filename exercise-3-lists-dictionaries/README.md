# Lists and Dictionaries

## Lists

Literal lists are written with square brackets, `[ element1, element2, ... ]`

```py
subjects = ["algebra", "biology", "chemistry", "differential equations"]
print(subjects) # same list as above
```

**Lists are zero-indexed**. You can access elements in a list with square bracket notation.

```py
subjects[0] # algebra
subjects[4] # IndexError: list index out of range
```

You can access multiple elements in a list using `[start:end]` notation

```py
subjects[1:3] # ['biology', 'chemistry']
```
