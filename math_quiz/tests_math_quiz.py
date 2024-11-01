import unittest
from math_quiz import generate_random_integer, choose_operator, calculate_expression

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """Test if random numbers generated are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val,
                            f"Random number {rand_num} is out of bounds ({min_val}, {max_val})")

    def test_choose_operator(self):
        """Test that the chosen operator is one of the valid operators."""
        valid_operators = ['+', '-', '*']
        for _ in range(100):  # Test a reasonable number of times
            operator = choose_operator()
            self.assertIn(operator, valid_operators, 
                          f"Operator {operator} is not a valid operator")

    def test_calculate_expression(self):
        """Test that calculate_expression returns the correct problem and answer."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (3, 4, '*', '3 * 4', 12),
            (10, 5, '+', '10 + 5', 15),
            (7, 2, '-', '7 - 2', 5),
            (6, 3, '*', '6 * 3', 18),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_expression(num1, num2, operator)
            self.assertEqual(problem, expected_problem, 
                             f"Problem mismatch: expected {expected_problem}, got {problem}")
            self.assertEqual(answer, expected_answer, 
                             f"Answer mismatch: expected {expected_answer}, got {answer}")


if __name__ == "__main__":
    unittest.main()
