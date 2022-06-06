class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # we have to consider the left subtree
        if data < node.data:
            # we have to check if the left node is a None
            # when the left node is  not None
            if node.left_node:
                # recursive
                self.insert_node(data, node.left_node)
            else:
                # create a left node
                node.left_node = Node(data, node)
                # update height parameter
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
        else:
            # we have to check if the right node is None
            # when the right child is not None
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
        # after every insertion WE HAVE TO CHECK whether the AVL properties are violated
        self.handle_violation(node)

    def remove_node(self, data, node):
        if node is None:
            return
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            # this is the node we want to remove
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
                # after every insertion WE HAVE TO CHECK whether the AVL properties are violated
                self.handle_violation(parent)
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
                # after every insertion WE HAVE TO CHECK whether the AVL properties are violated
                self.handle_violation(parent)
            elif node.left_node is not None and node.right_node is None:
                print("Removing a node with single left child")
                parent = node.parent
                """
                supposed we delete 6
                      4
                    /   \
                  3       7 
                /  \     / \
                1   2   6   9
                       /   /
                      5   8
                Where 7 is 6's parent node, and 6 is 7's left node
                After removing 6, the 6's left node will become
                7's left node
                """

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node

                """
                Supposed we need to delete 9
                      4
                    /   \
                  3       7 
                /  \     / \
                1   2   6   9
                       /   /
                      5   8
               Where 7 is 9's parent node, and 9 is 7's right node
                After removing 9, the 9's left node will become
                7's right node
               """
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node

                if parent is None:
                    self.root = node.left_node
                node.left_node.parent = parent

                del node
                # after every insertion WE HAVE TO CHECK whether the AVL properties are violated
                self.handle_violation(parent)
            # WHEN THERE iS A SINGLE CHILD
            else:
                print("Removing node with 2 children")
                """
                                Supposed we need to delete 3
                                      4
                                    /   \
                                  3       7 
                                /  \     / \
                                1   2   6   9
                                       /   /
                                      5   8
                               Where 7 is 9's parent node, and 9 is 7's right node
                                After removing 9, the 9's left node will become
                                7's right node
                """
                predecessor = self.get_predecessor(node.left_node)
                # swap the node and predecessor
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def handle_violation(self, parent_node):
        # check the nodes from the node we have inserted up to root node
        while parent_node is not None:
            parent_node.height = max(self.calc_height(parent_node.left_node),
                                     self.calc_height(parent_node.right_node)) + 1
            self.violation_helper(parent_node)
            # whenever we settle a violation (rotations) it may happen that it
            # violates the AVL properties in the other part of the tree
            parent_node = parent_node.parent

    # check whether the subtree is balanced with root node = node
    def violation_helper(self, node):
        balance = self.calculate_balance(node)
        # OK, we know the tree is left heavy BUT it can be left-right-heavy or left-left-heavy
        if balance > 1:
            # left right heavy situation: left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)
            # this is the right rotation on grandparent (if left-left heavy, that's single right rotation
            self.rotate_right(node)

        # OK, we know the tree is left heavy BUT it can be left-right-heavy or left-left-heavy
        if balance < -1:
            # right - left heavy situation: so we need a right rotation before left rotation
            if self.calculate_balance(node.left_node) > 0:
                self.rotate_right(node.right_node)
            # left rotate
            self.rotate_left(node)

    # for a given node, normally the node that is added for insert use case
    # or the parent of the node in case removal use case
    def rotate_right(self, node):
        print("Rotating to the right on node ", node.data)
        # backup the left node
        temp_left_node = node.left_node
        # left node will become the parent of right node
        t = temp_left_node.right_node

        # the current node becomes the right node of the right node that now is its parent
        temp_left_node.right_node = node
        # the old right node's left node becomes the right node
        node.left_node = t
        if t is not None:
            # change the parent for previous right node to current node
            t.parent = node
        # escalate
        temp_parent = node.parent
        # current node parent change accordingly
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node))
        temp_left_node.height = max(self.calc_height(temp_left_node.left_node),
                                    self.calc_height(temp_left_node.right_node)) + 1

        # for a given node, normally the node that is added for insert use case
        # or the parent of the node in case removal use case

    def rotate_left(self, node):
        print("Rotating to the left on node ", node.data)
        # backup the left node
        temp_right_node = node.right_node
        # left node will become the parent of right node
        t = temp_right_node.left_node

        # the current node becomes the right node of the left node
        temp_right_node.left_node = node
        # the old right node becomes the left node
        node.right_node = t
        if t is not None:
            t.parent = node
        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node))
        temp_right_node.height = max(self.calc_height(temp_right_node.left_node),
                                     self.calc_height(temp_right_node.right_node)) + 1

    def calc_height(self, node):
        # this is when the node is a NULL
        if node is None:
            return -1
        return node.height

    def calculate_balance(self, node):
        if node is None:
            return 0
        return self.calc_height(node.left_node) - self.calc_height(node.right_node)

    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)

        l, r, p = '', '', ''

        if node.left_node is not None:
            l = node.left_node.data
        else:
            l = 'NULL'
        if node.right_node is not None:
            r = node.right_node.data
        else:
            r = 'NULL'

        if node.parent is not None:
            p = node.parent.data
        else:
            p = 'NULL'

        print("%s left: %s right: %s parent: %s height: %s" % (node.data, l, r, p, node.height))

        if node.right_node:
            self.traverse_in_order(node.right_node)
