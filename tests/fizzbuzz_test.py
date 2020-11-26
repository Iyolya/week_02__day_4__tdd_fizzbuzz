import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_3_returns_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(3))

    def test_fizzbuzz_5_returns_buzz(self):
	    self.assertEqual("Buzz", fizzbuzz(5))