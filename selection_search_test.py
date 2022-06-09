import unittest

from selection_search import selection_sort


# @parametrized([
#     ([5, 4, 3, -2, 1], [-2, 1, 3, 4, 5])
# ])
# def test_few_sel(input, expect):
#     assert_equal(expect, selection_sort(input))


class SelectionSortTest(unittest.TestCase):

    def test_selection_sort(self):
        v = [5, 4, 3, -2, 1]
        expected = [-2, 1, 3, 4, 5]
        self.assertEqual(expected, selection_sort(v))  # add assertion here


if __name__ == '__main__':
    unittest.main()
