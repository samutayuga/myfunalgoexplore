import unittest

from funalgotest import MyAlgoForFun

alg = MyAlgoForFun()


class TestFunAlgo(unittest.TestCase):

    def test_dutch_flag(self):
        self.assertEqual([0, 0, 1, 1, 1, 2, 2],
                         alg.dutch_flag([0, 1, 2, 0, 1, 2, 1]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
