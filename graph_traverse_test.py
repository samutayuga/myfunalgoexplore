import unittest
from graph_traverse import breadth_first_search, depth_first_search, Vertex,dfs_recurse


class TestGraphTraverse(unittest.TestCase):
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

    def test_dfs(self):
        vtxA = Vertex("A")
        vtxB = Vertex("B")
        vtxC = Vertex("C")
        vtxD = Vertex("D")
        vtxE = Vertex("E")
        vtxA.adjacency_list.append(vtxB)
        vtxA.adjacency_list.append(vtxC)
        vtxB.adjacency_list.append(vtxD)
        vtxD.adjacency_list.append(vtxE)
        depth_first_search(vtxA)
        self.assertTrue(vtxE.visited)

    def test_dfs_recurse(self):
        vtxA = Vertex("A")
        vtxB = Vertex("B")
        vtxC = Vertex("C")
        vtxD = Vertex("D")
        vtxE = Vertex("E")
        vtxA.adjacency_list.append(vtxB)
        vtxA.adjacency_list.append(vtxC)
        vtxB.adjacency_list.append(vtxD)
        vtxD.adjacency_list.append(vtxE)
        dfs_recurse(vtxA)
        self.assertTrue(vtxE.visited)


if __name__ == '__main__':
    unittest.main()
