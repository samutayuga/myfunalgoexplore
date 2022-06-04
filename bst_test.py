import unittest
from bst import BinarySearchTree


class BstTest(unittest.TestCase):
    def test_traverse(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(15)
        bst.insert(27)
        bst.insert(1)
        bst.insert(4)
        bst.insert(3)
        bst.traverse()

        self.assertEqual(27, bst.get_max())  # assert max
        self.assertEqual(1, bst.get_min())  # assert min


if __name__ == '__main__':
    unittest.main()
