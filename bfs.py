class Vertex:
    def __init__(self, name):
        self.visited = False
        self.name = name
        self.adjacency_list = []


def breadth_first_search(starting_vertex=None):
    # FIFO structure: first item we insert the first item we get
    queue = [starting_vertex]

    # we keep iterating until queue becomes empty
    while queue:
        # return and remove the first item
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)

        # let's consider the neighbors of the actual node one by one
        for n in actual_node.adjacency_list:
            queue.append(n)

