import unittest
from day5.task4 import sum

# Tests are crucial for ensuring code reliability, catching bugs early,
# documenting expected behavior, and enabling safe refactoring.
# Unit tests verify individual functions work correctly in isolation.



class TestSum(unittest.TestCase):
    """Test cases for the sum function."""

    def test_sum_positive_integers(self):
        """Test sum with two positive integers."""
        self.assertEqual(sum(2, 3), 5)

    def test_sum_negative_integers(self):
        """Test sum with negative integers."""
        self.assertEqual(sum(-2, -3), -5)

    def test_sum_mixed_signs(self):
        """Test sum with mixed positive and negative integers."""
        self.assertEqual(sum(5, -3), 2)

    def test_sum_with_zero(self):
        """Test sum with zero."""
        self.assertEqual(sum(0, 5), 5)
        self.assertEqual(sum(0, 0), 0)

    def test_sum_large_numbers(self):
        """Test sum with large integers."""
        self.assertEqual(sum(1000000, 2000000), 3000000)


if __name__ == '__main__':
    unittest.main()