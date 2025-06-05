import unittest
from main import remainder

class TestRemainder(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(remainder(32, 5), 2)

    def test_negative_dividend(self):
        self.assertEqual(remainder(54, 8), 6)

    def test_negative_divisor(self):
        self.assertEqual(remainder(25, 4), 1)

    def test_both_negative(self):
        self.assertEqual(remainder(44, 7), 2)

    def test_zero_dividend(self):
        self.assertEqual(remainder(0, 7), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            remainder(14, 0)

if __name__ == '__main__':
    unittest.main()

