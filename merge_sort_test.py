import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        original = [14, 1000, -4, -10, 100000]
        expected = [-10, -4, 14, 1000, 100000]
        self.assertEqual(expected, merge_sort(original))  # add assertion here


if __name__ == '__main__':
    unittest.main()
