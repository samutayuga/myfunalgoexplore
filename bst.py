class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # this is the first item in the BST
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # go to left sub tree
        if data < node.data:
            if node.left_node:
                # if left node exists keep going
                self.insert_node(data, node.left_node)
            else:
                # there is no left child node
                node.left_node = Node(data, node)
        # got to the right
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

    # it has O(NLogN) linear running time
    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left_node is None:
            return node.data
        else:
            return self.get_min_value(node.left_node)

    # it has O(NLogN) linear running time
    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_node is None:
            return node.data

        return self.get_max_value(node.right_node)

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    # it has O(N) linear running time
    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)
        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)
        # print(node.data)
