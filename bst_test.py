import unittest
from bst import BinarySearchTree, TreeComparator


class BstTest(unittest.TestCase):
    """
                   Supposed we need to delete 9
                         5
                       /   \
                     3       7
                   /  \     / \
                   1   4   6   9
                          /   /
                         5   8
                  Where 7 is 9's parent node, and 9 is 7's right node
                   After removing 9, the 9's left node will become
                   7's right node
                  """

    def test_traverse(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(4)
        bst.insert(6)
        bst.insert(9)
        bst.insert(8)
        bst.traverse()

        self.assertEqual(9, bst.get_max())  # assert max
        self.assertEqual(1, bst.get_min())  # assert min

        bst.remove(3)
        bst.remove(8)
        bst.remove(6)
        bst.remove(9)
        bst.traverse()

    def test_comparebst(self):
        bst1 = BinarySearchTree()
        bst1.insert(5)
        bst1.insert(3)
        bst1.insert(6)
        bst1.insert(1)

        bst2 = BinarySearchTree()
        bst2.insert(5)
        bst2.insert(3)
        bst2.insert(6)
        bst2.insert(1)
        comparator = TreeComparator()

        self.assertTrue(comparator.compare(bst1.root, bst2.root))


if __name__ == '__main__':
    unittest.main()
