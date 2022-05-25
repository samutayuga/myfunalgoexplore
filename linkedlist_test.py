import time
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
        linkedlist.remove("jack")
        self.assertEqual(2, linkedlist.num_of_nodes)

    """
    This is to compare the insert performance
    on array and linked list data structure
    The expectation is that, the array needs O(N) running time complexity
    while linked list needs O(1) running time complexity
    as far as inserting in the beginning of data structure is a concern
    """

    def test_benchmark(self):
        linkedlist = LinkedList()
        array = []

        now = time.time()
        for i in range(50000):
            array.insert(0, i)
        total_time_arrinsert = time.time() - now
        print("time to insert 50000 item into array is %s", str(total_time_arrinsert))
        now = time.time()
        for i in range(50000):
            linkedlist.insert_start(i)
        total_time_llinsert = time.time() - now
        print("time to insert 50000 item into linkedlist is %s", str(total_time_llinsert))
        ratio = total_time_arrinsert / total_time_llinsert
        print("ratio", str(ratio))


if __name__ == '__main__':
    unittest.main()
