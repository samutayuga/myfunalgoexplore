import unittest
from avl_bst import AVLTree


class TestAvlTree(unittest.TestCase):
    def test_insert(self):
        avl = AVLTree()
        avl.insert(1)
        avl.insert(2)
        avl.insert(3)
        self.assertEqual(1, avl.root.height)
        self.assertEqual(0, avl.calculate_balance(avl.root))
        avl.insert(4)
        avl.insert(5)
        self.assertEqual(2, avl.root.height)
        self.assertEqual(-1, avl.calculate_balance(avl.root))
        avl.insert(6)
        self.assertEqual(2, avl.root.height)
        self.assertEqual(0, avl.calculate_balance(avl.root))
        avl.insert(9)
        avl.insert(8)
        avl.insert(7)
        self.assertEqual(3, avl.root.height)
        self.assertEqual(-1, avl.calculate_balance(avl.root))
        avl.insert(12)
        avl.insert(11)
        avl.insert(10)
        self.assertEqual(3, avl.root.height)
        self.assertEqual(-1, avl.calculate_balance(avl.root))

        avl.traverse_in_order(avl.root)



if __name__ == '__main__':
    unittest.main()
