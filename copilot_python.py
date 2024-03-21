class MathOperations:
    """
    A class that provides various mathematical operations.

    Attributes:
        MAX_EXPONENT (int): The maximum exponent allowed for the power operation.

    Methods:
        factorial(n): Calculates the factorial of a given number.
        is_palindrome(string): Checks if a given string is a palindrome.
        power(base, exponent): Calculates the power of a given base raised to a given exponent.
    """

    def __init__(self):
        self.MAX_EXPONENT = 10

    def factorial(self, n):
        """
        Calculates the factorial of a given number.

        Args:
            n (int): The number to calculate the factorial for.

        Returns:
            int: The factorial of the given number.
        """
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

    def is_palindrome(self, string):
        """
        Checks if a given string is a palindrome.

        Args:
            string (str): The string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        reversed_string = string[::-1]
        if string == reversed_string:
            return True
        else:
            return False

    def power(self, base, exponent):
        """
        Calculates the power of a given base raised to a given exponent.

        Args:
            base (int or float): The base number.
            exponent (int or float): The exponent.

        Raises:
            ValueError: If either base or exponent is not a number, or if the exponent is outside the allowed range.

        Returns:
            int or float: The result of the power operation.
        """
        if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
            raise ValueError("Both base and exponent must be numbers")
        if abs(exponent) > self.MAX_EXPONENT:
            raise ValueError(f"Exponent must be between -{self.MAX_EXPONENT} and {self.MAX_EXPONENT}")
        return base ** exponent