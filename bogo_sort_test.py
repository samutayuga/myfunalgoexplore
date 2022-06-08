import unittest
from bogo_sort import BogoSort


class BogoSortTest(unittest.TestCase):
    def test_bogo_sort(self):
        original = [-10, -11, 10, 7, 8, 1000]
        expected = [-11, -10, 7, 8, 10, 1000]
        bg = BogoSort(original)
        bg.sort()
        self.assertEqual(expected, bg.nums)  # add assertion here


if __name__ == '__main__':
    unittest.main()
