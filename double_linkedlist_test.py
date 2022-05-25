import unittest
from double_linkedlist import DoublyLinkedList, Node


class DoublyLinkedListTest(unittest.TestCase):
    def test_insert(self):
        doubly_linked_list = DoublyLinkedList()
        # insert several item
        doubly_linked_list.insert(1)
        doubly_linked_list.insert(10)
        doubly_linked_list.insert(3)
        doubly_linked_list.traverse_forward()
        doubly_linked_list.traverse_backward()

        self.assertEqual(1, doubly_linked_list.head.data)
        self.assertEqual(3, doubly_linked_list.tail.data)  # add assertion here


if __name__ == '__main__':
    unittest.main()
