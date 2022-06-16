import time
import unittest
from linkedlist import LinkedList, Node, do_merge


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
        print("time to insert 50000 item into array is {}".format(str(total_time_arrinsert)))
        now = time.time()
        for i in range(50000):
            linkedlist.insert_start(i)
        total_time_llinsert = time.time() - now
        print("time to insert 50000 item into linkedlist is {}".format(str(total_time_llinsert)))
        ratio = total_time_arrinsert / total_time_llinsert
        print("ratio {}".format(str(ratio)))

    def test_get_middle_node(self):
        linkedlist = LinkedList()
        linkedlist.insert_start(10)
        linkedlist.insert_start(19)
        linkedlist.insert_start(30)
        linkedlist.insert_start(21)
        linkedlist.insert_start(23)

        self.assertEqual(30, linkedlist.get_middle_node().data)

    def test_reverse(self):
        linkedlist = LinkedList()
        linkedlist.insert_start(10)
        linkedlist.insert_start(19)
        linkedlist.insert_start(30)
        linkedlist.insert_start(21)
        linkedlist.insert_start(23)
        print("before reverse")
        linkedlist.traverse()
        linkedlist.reverse()
        print("after reverse")
        linkedlist.traverse()

    def test_merge_lnodes(self):
        ll1=LinkedList()
        ll1.insert_start(Node(1))
        ll1.insert_start(Node(3))
        ll1.insert_start(Node(7))
        ll1.insert_start(Node(9))

        ll2 = LinkedList()
        ll2.insert_start(Node(1))
        ll2.insert_start(Node(2))
        ll2.insert_start(Node(6))
        ll2.insert_start(Node(10))

        print(do_merge(ll1, ll2))


if __name__ == '__main__':
    unittest.main()
