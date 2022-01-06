import unittest

# this is how we import a function from another Python file
from .main import Stringify


class StringificationTests(unittest.TestCase):
    def test_ones(self):
        number = 9
        result = Stringify(number)
        self.assertEqual(
            result, "nine", f"{number} is not stringified to English correctly"
        )

    def test_teens(self):
        number = 13
        result = Stringify(number)
        self.assertEqual(
            result, "thirteen", f"{number} is not stringified to English correctly"
        )

    def test_two_digits(self):
        number = 22
        result = Stringify(number)
        self.assertEqual(
            result, "twenty-two", f"{number} is not stringified to English correctly"
        )

    def test_divisible_by_ten(self):
        number = 70
        result = Stringify(number)
        self.assertEqual(
            result, "seventy", f"{number} is not stringified to English correctly"
        )

    # can you think of other tests to add here?
