import unittest
from Testing.real_python import test_sum, test_sum_tuple


class Test(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(test_sum(1, 2, 3), 6)

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5)


if __name__ == '__main__':
    unittest.main()
