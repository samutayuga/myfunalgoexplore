import unittest
from linkedlist import LinkedList, Node


class LinkedListTest(unittest.TestCase):
    def test_insert_start(self):
        linkedlist = LinkedList()

        linkedlist.insert_start("head")
        self.assertEqual(1, linkedlist.num_of_nodes)  # add assertion here
        p = linkedlist.head
        self.assertTrue(p.next_node is None)
        linkedlist.insert_end("tail")
        linkedlist.insert_start("jack")
        self.assertEqual(3, linkedlist.num_of_nodes)
        p1 = linkedlist.head
        self.assertTrue(p1.next_node.data == "head")
        linkedlist.traverse()


if __name__ == '__main__':
    unittest.main()
