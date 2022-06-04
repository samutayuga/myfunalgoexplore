class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            # we have found the node we want to remove
            # there are 3 options
            # LEAF NODE CASE
            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node ...%d" % node.data)
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:
                    self.root = None

                del node
            # WHEN THERE iS A SINGLE CHILD
            elif node.left_node is None and node.right_node is not None:
                print("Removing a node with single right child")
                parent = node.parent
                """
                    4
                 3      6 
                1  2   5  
                         7
                """

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                """
                                    4
                                 3      5 
                                1  2      6
                                            7
               """
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                if parent is None:
                    self.root = node.right_node
                node.right_node.parent = parent

                del node
            elif node.left_node is not None and node.right_node is None:
                print("Removing a node with single left child")
                parent = node.parent
                """
                    4
                 3      6 
                1  2   5  
                         7
                """

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node
                """
                                    4
                                 3      5 
                                1  2      6
                                            7
               """
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node

                if parent is None:
                    self.root = node.left_node
                node.left_node.parent = parent

                del node

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
