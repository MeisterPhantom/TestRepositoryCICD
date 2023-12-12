import unittest

class SumTest(unittest.TestCase):

    def test_sum_positive_numbers(self):
        self.assertEqual(sum([1, 2]), 3)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum([-1, -2]), -3)

if __name__ == "__main__":
    unittest.SumTest()
