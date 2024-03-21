import unittest

class MathOperationsTests(unittest.TestCase):
    def setUp(self):
        self.math_ops = MathOperations()

    def test_factorial(self):
        self.assertEqual(self.math_ops.factorial(0), 1)
        self.assertEqual(self.math_ops.factorial(1), 1)
        self.assertEqual(self.math_ops.factorial(5), 120)

    def test_is_palindrome(self):
        self.assertTrue(self.math_ops.is_palindrome("racecar"))
        self.assertTrue(self.math_ops.is_palindrome("madam"))
        self.assertFalse(self.math_ops.is_palindrome("hello"))

    def test_power(self):
        self.assertEqual(self.math_ops.power(2, 3), 8)
        self.assertEqual(self.math_ops.power(5, 0), 1)
        self.assertEqual(self.math_ops.power(10, -2), 0.01)

if __name__ == '__main__':
    unittest.main()