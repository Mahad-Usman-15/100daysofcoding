import unittest
class TestSum(unittest.TestCase):
    def test_sum_positive(self):
        self.assertEqual(sum(2, 3), 5)
    
    def test_sum_negative(self):
        self.assertEqual(sum(-1, -2), -3)
    
    def test_sum_mixed(self):
        self.assertEqual(sum(10, -5), 5)

if __name__ == '__main__':
    unittest.main()
def sum(a:int,b:int):
    return a+b


