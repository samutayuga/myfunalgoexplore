class Node:
    def __init__(self, data):
        """
        :param data:
        :return:
        """
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        """
        This is the first node of the linked list
        :return:
        """
        self.head = None
        self.num_of_nodes = 0

    # O(1)
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)
        # the head is NULL
        if self.head is None:
            self.head = new_node
        else:
            # we have to update the reference
            new_node.next_node = self.head
            self.head = new_node

    # O(N)
    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head
        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node
        return slow_pointer

    # O(n)
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
        else:
            # this is when the linked list is  not empty
            actual_node = self.head
            while actual_node.next_node is not None:
                # iterate
                actual_node = actual_node.next_node
            actual_node.next_node = new_node

    # O(N)
    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    # O(N) linear running time
    def remove(self, data):
        # if the list is empty
        if self.head is None:
            return
        actual_node = self.head
        # we have to track the previous node for future pointer updates
        # this is ahy doubly linked lists are better - we can get the previous
        # node
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node
        # search miss
        if actual_node is None:
            return
        # update the references (so we have the data we want to remove)
        # if the head node is the one we want to remove
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # remove the internal node
            # NO NEED to del the node because the garbage collection will do that
            previous_node.next_node = actual_node.next_node
        self.num_of_nodes -= 1

    def size_of_list(self):
        return self.num_of_nodes
