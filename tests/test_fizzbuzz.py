import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertTrue(fizzbuzz(3) == 'Fizz')
        self.assertTrue(fizzbuzz(5) == 'Buzz')
        self.assertTrue(fizzbuzz(15) == 'FizzBuzz')
        self.assertFalse(fizzbuzz(4) == 'Fizz')
        self.assertFalse(fizzbuzz(6) == 'Buzz')
        self.assertFalse(fizzbuzz(1232131) == 'Fizz')
        self.assertFalse(fizzbuzz(1232131) == 'Buzz')
        
    # def test_string_fizzbuzz(self):
    #     self.assertFalse(fizzbuzz('hi') == 'Fizz')

    # def test_decimal_fizzbuzz(self):
    #     self.assertTrue(fizzbuzz(3.0) == 'Fizz')
    #     self.assertTrue(fizzbuzz(5.1) == 'Buzz')
    #     self.assertTrue(fizzbuzz(15.0) == 'FizzBuzz')

    # def test_negative_fizzbuzz(self):
    #     self.assertTrue(fizzbuzz(-3) == 'Fizz')
    #     self.assertTrue(fizzbuzz(-5) == 'Buzz')
    #     self.assertTrue(fizzbuzz(-16) == 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()