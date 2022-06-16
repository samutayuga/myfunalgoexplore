import unittest
from binary_heap import Heap


class TestBinaryHeap(unittest.TestCase):
    def test_binary_heap(self):
        heap = Heap()
        heap.insert(13)
        heap.insert(-2)
        heap.insert(0)
        heap.insert(0)
        heap.insert(8)
        heap.insert(1)
        heap.insert(-5)
        heap.insert(99)
        heap.insert(100)
        heap.is_valid_heap()
        print(heap)
        heap.heap_sort()



        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
