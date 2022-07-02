import unittest
from bfs import breadth_first_search, Vertex


class TestBfs(unittest.TestCase):
    def test_bfs(self):
        vtxA = Vertex("A")
        vtxB = Vertex("B")
        vtxC = Vertex("C")
        vtxD = Vertex("D")
        vtxE = Vertex("E")
        vtxA.adjacency_list.append(vtxB)
        vtxA.adjacency_list.append(vtxC)
        vtxB.adjacency_list.append(vtxD)
        vtxD.adjacency_list.append(vtxE)
        breadth_first_search(vtxA)
        self.assertTrue(vtxE.visited)


if __name__ == '__main__':
    unittest.main()
