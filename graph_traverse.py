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
            if not n.visited:
                queue.append(n)


def depth_first_search(starting_vertex=None):
    stack = [starting_vertex]

    while stack:
        vtx = stack.pop()
        vtx.visited = True
        print(vtx.name)
        for n in vtx.adjacency_list:
            if not n.visited:
                stack.append(n)


def dfs_recurse(starting_vertex=None):
    starting_vertex.visited = True
    print(starting_vertex.name)

    for n in starting_vertex.adjacency_list:
        if not n.visited:
            dfs_recurse(n)
