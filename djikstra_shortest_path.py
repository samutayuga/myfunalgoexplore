import heapq


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        # this is the name where to come from the shortest path
        # to build the shortest path tree
        self.predecessor = None
        self.adjacency_list = []
        # this is the minimum distance
        self.min_distance = float('inf')

    # this is how python compare the object
    # after inserting these object into the heap
    # heap can compare the given object
    def __lt__(self, other):
        return self.min_distance < other.min_distance


class DijkstraAlgo:
    def __init__(self):
        # this is the heap representation
        # binary heap not the fibobanncy
        self.heap = []

    def calculate(self, start_vertex):
        # initialize the vertices
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        # as long as the heap is empty
        while self.heap:
            # we pop the vertex with the lowest min distance parameter
            # pop removes the given item
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # we have to consider the neighbor

            for edge in actual_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight
                # there is a shorter path to the vertex v
                if new_distance < v.min_distance:
                    # when there is a shorter path is available then update
                    v.predecessor = u
                    v.min_distance = new_distance
                    # update the heap - this is the lazy implementation
                    # because it takes the O(N) to find the vertex we want to update (v)
                    # plus we have O(logN) to handle the heap again [O(N)+O(logN)=O(N)]
                    # Fibonacci heaps-O(1)
                    heapq.heappush(self.heap, v)
            actual_vertex.visited = True

    @staticmethod
    def get_shortest_path(vertex):
        print("shortest path to vertex is: %s" % str(vertex.min_distance))
        actual_vertex = vertex
        while actual_vertex:
            print("%s " % actual_vertex.name)
            actual_vertex = actual_vertex.predecessor

