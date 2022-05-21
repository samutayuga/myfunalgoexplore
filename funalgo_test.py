import unittest

from funalgo import MyAlgoForFun

alg = MyAlgoForFun()


class TestFunAlgo(unittest.TestCase):

    def test_dutch_flag(self):
        self.assertEqual([0, 0, 1, 1, 1, 2, 2],
                         alg.dutch_flag([0, 1, 2, 0, 1, 2, 1]))  # add assertion here

    def test_reverse(self):
        self.assertEqual([0, 0, 1, 1, 1, 2, 2],
                         alg.reverse([2, 2, 1, 1, 1, 0, 0]))  # add assertion here

    def test_polindrom(self):
        self.assertTrue(alg.is_polindrom("madam"))  # add assertion here

    def test_reverse_integer(self):
        self.assertEqual(12345, alg.reverse_integer(54321))

    def test_is_anagram(self):
        self.assertTrue(alg.is_anagram(['r', 'e', 's', 't', 'f', 'u', 'l'], ['f', 'l', 'u', 's', 't', 'e', 'r']))


if __name__ == '__main__':
    unittest.main()
