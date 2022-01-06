"""
There are 3 bugs/problems in here. Use your debugger to find them!

This Python file should be executed with `python path/to/dir/part-6-debugging/main.py 10`. If you leave out the number at the end, an integer will be randomly generated
"""

import math
import random
import sys

# Capitalized function (and class and variable) names are automatically exported. see test_main.py to see how we import this function to use it in tests
def Stringify(number):
    """
    Takes an integer between 0 and 99 and returns an English string of it. Eg. 10 -> "ten", 99 -> "ninety-nine". The bugs live in this function!

    Params:
        number int
    Returns:
        string
    """
    low_numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    if number < 19:
        return low_numbers[number]

    tens_digit = math.ceil(number / 10)
    tens_place = tens[tens_digit - 1]
    ones_place = low_numbers[number % 10]
    return f"{tens_place}-{ones_place}"


def main(number):
    print(f"The number as an integer is: {number}")
    stringified = Stringify(number)
    print(f"The number as an English string is: {stringified}")


# See here for an in-depth explanation of how this block of code works:
# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # this block of code will run when you call this Python file by itself. it's a useful trick for writing scripts!
    # if you were writing a module or a library that isn't meant to be used by itself, you wouldn't need to add this block

    # sys.argv is a list of the arguments passed to python from the command line
    # try printing them!
    if len(sys.argv) > 1:
        user_value = int(sys.argv[1])
    else:
        user_value = random.randint(0, 99)
    main(user_value)
