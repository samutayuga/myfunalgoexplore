import unittest
from bst import BinarySearchTree


class BstTest(unittest.TestCase):
    """
                   Supposed we need to delete 9
                         4
                       /   \
                     3       7
                   /  \     / \
                   1   2   6   9
                          /   /
                         5   8
                  Where 7 is 9's parent node, and 9 is 7's right node
                   After removing 9, the 9's left node will become
                   7's right node
                  """

    def test_traverse(self):
        bst = BinarySearchTree()
        bst.insert(4)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(6)
        bst.insert(9)
        bst.insert(5)
        bst.insert(8)
        bst.traverse()

        self.assertEqual(9, bst.get_max())  # assert max
        self.assertEqual(1, bst.get_min())  # assert min


        bst.remove(3)
        bst.remove(8)
        bst.remove(6)
        bst.remove(9)
        bst.traverse()


if __name__ == '__main__':
    unittest.main()
