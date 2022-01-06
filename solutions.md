# Solutions to all the exercises in this repo

DON'T CHEAT! Make sure you're satisfied with your answer or you've exhausted all your options before looking at the solutions below.


## part-6-debugging

1. Does not handle the case when you have a number divisible by 10, eg. 20, 30, 40, etc.
2. `tens_digit = math.ceil(number / 10)` should be `tens_digit = math.floor(number / 10)`
3. `tens_place = tens[tens_digit - 1]` should be `tens_place = tens[tens_digit - 2]`

## 1 Array and Matrix Operations with Numpy

### 1a

```py
import numpy as np

a = [2, 2, 2]
b = [4, 4, 4]

np.multiply(a, b)
```

### 1b

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

### 1c

```py
import numpy as np

np.linspace(10, 20, num=4)
```