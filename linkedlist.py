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

    def size_of_list(self):
        return self.num_of_nodes
