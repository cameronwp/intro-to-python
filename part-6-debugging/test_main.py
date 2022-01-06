import unittest

# this is how we import a function from another Python file
from .main import Stringify


class StringificationTests(unittest.TestCase):
    def test_ones(self):
        number = 9
        result = Stringify(number)
        self.assertEqual(result, "nine")

    def test_teens(self):
        number = 13
        result = Stringify(number)
        self.assertEqual(result, "thirteen")

    def test_two_digits(self):
        number = 22
        result = Stringify(number)
        self.assertEqual(result, "twenty-two")

    def test_divisible_by_ten(self):
        number = 70
        result = Stringify(number)
        self.assertEqual(result, "seventy")

    # can you think of other tests to add here?
