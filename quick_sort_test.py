import unittest
from quick_sort import QuickSort


class QuickSortTest(unittest.TestCase):
    def test_quick_sort(self):
        x = [1, -4, 0, 10, 5, 4, 3, 100]
        x_sorted = [-4, 0, 1, 3, 4, 5, 10, 100]
        qSort = QuickSort(x)
        qSort.sort()
        self.assertEqual(x_sorted, qSort.data)  # add assertion here


if __name__ == '__main__':
    unittest.main()
