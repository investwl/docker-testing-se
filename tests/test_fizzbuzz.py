# filepath: /c:/Cawu 4 - Software Engineering/latihan_tdd/tests/test_fizzbuzz.py
import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')

    def test_none(self):
        self.assertFalse(fizzbuzz(2))

if __name__ == '__main__':
    unittest.main()