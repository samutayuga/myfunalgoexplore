import unittest
from bubble_sort import BubbleSort


class BubbleSortTest(unittest.TestCase):
    def test_bs(self):
        original = [-10, -11, 10, 7, 8, 1000]
        expected = [-11, -10, 7, 8, 10, 1000]
        bs = BubbleSort(original)
        bs.sort()
        self.assertEqual(expected, bs.nums)  # add assertion here
        expected_desc = [1000, 10, 8, 7, -10, -11]
        bs.sort(ascending=False)
        self.assertEqual(expected_desc, bs.nums)  # add assertion here


if __name__ == '__main__':
    unittest.main()
