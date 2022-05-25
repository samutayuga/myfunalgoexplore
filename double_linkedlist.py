class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # this operation inserts items at the end of the linked list
    # so we have to manipulate the tail node in O(1) running time
    def insert(self, data):
        new_node = Node(data)
        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # when there is at least 1 item in the data structure
        # we keep inserting items at the end of the linked list
        else:
            # make the new node previous node point to the current's last node tail
            new_node.previous = self.tail
            # the tail's next is new node
            self.tail.next = new_node
            # the tail is now pointing to the new node
            self.tail = new_node

    def traverse_forward(self):
        actual_node = self.head
        while actual_node is not None:
            print("%d", actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail
        while actual_node is not None:
            print("%d", actual_node.data)
            actual_node = actual_node.previous
