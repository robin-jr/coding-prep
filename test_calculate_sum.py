import unittest
from calculate_sum import calculate_sum 

class TestCalculateSum(unittest.TestCase):
    def test_naturals(self):
        self.assertAlmostEqual(calculate_sum(1,2),3)
    def test_zero(self):
        self.assertAlmostEqual(calculate_sum(0,0),0)
    def test_negative(self):
        self.assertAlmostEqual(calculate_sum(-1,-3),-4)
