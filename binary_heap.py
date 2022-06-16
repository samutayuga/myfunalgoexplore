CAPACITY = 10


class Heap:
    def __init__(self):
        # this is the actual number of item in the ds
        self.heap_size = 0
        self.heap = [0] * CAPACITY

    def insert(self, item):
        if self.heap_size == CAPACITY:
            return
        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1

        # check the heap properties

        self.fix_up(self.heap_size - 1)
        # starting with the actual node we inserted
        # we have to compare with the parent node

    def fix_up(self, index):
        parent_index = (index - 1) // 2
        # we consider all the items above till we hit the root node
        # if heap property is violated then we swap the parent and child
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    # peek the maximum / minimum
    def get_max(self):
        return self.heap[0]

    # peek then remove
    def poll(self):
        max_item = self.get_max()
        # swap the root node with the last item and heafify
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size = self.heap_size - 1
        # make sure the head os heapified
        self.fix_down(0)

        return max_item

    def fix_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2
        largest_index = index

        # looking for the largest (parent ot left index)
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            largest_index = index_left

        # if the right child is greater than the left child: largest is the right child
        if index_right < self.heap_size and self.heap[index_right] > self.heap[largest_index]:
            largest_index = index_right
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)

    def is_valid_heap(self, index=0):

        # start from the root node
        index_left = 2 * index + 1
        index_right = 2 * index + 2
        while index < self.heap_size:
            if self.heap[index_left] < self.heap[index] and self.heap[index_right] < self.heap[index]:
                index = index_right
                self.is_valid_heap(index)
            else:
                return False
        return True

    def heap_sort(self):
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)
