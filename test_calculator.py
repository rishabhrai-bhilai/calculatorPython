import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_square_root(self):
        self.assertAlmostEqual(calculator.square_root(9), 3)
        self.assertAlmostEqual(calculator.square_root(16), 4)
        self.assertAlmostEqual(calculator.square_root(25), 5)

    def test_factorial(self):
        self.assertEqual(calculator.factorial(0), 1)
        self.assertEqual(calculator.factorial(1), 1)
        self.assertEqual(calculator.factorial(5), 120)
        self.assertEqual(calculator.factorial(10), 3628800)

    def test_natural_logarithm(self):
        self.assertAlmostEqual(calculator.natural_logarithm(1), 0)
        self.assertAlmostEqual(calculator.natural_logarithm(10), 2.302585092994046)
        self.assertAlmostEqual(calculator.natural_logarithm(100), 4.605170185988092)

    def test_power(self):
        self.assertAlmostEqual(calculator.power(2, 3), 8)
        self.assertAlmostEqual(calculator.power(3, 2), 9)
        self.assertAlmostEqual(calculator.power(4, 0.5), 2)

if __name__ == '__main__':
    unittest.main()
