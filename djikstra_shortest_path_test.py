import unittest
from djikstra_shortest_path import Vertex, Edge,DijkstraAlgo


class DjikstraAlgoTest(unittest.TestCase):
    def test_shortest_path(self):
        vextex1 = Vertex("A")
        vextex2 = Vertex("B")
        vextex3 = Vertex("C")
        vextex4 = Vertex("D")
        vextex5 = Vertex("E")
        vextex6 = Vertex("F")
        vextex7 = Vertex("G")
        vextex8 = Vertex("H")

        # edges
        edge1 = Edge(5, vextex1, vextex2)
        edge2 = Edge(8, vextex1, vextex8)
        edge3 = Edge(9, vextex1, vextex5)
        edge4 = Edge(15, vextex2, vextex4)
        edge5 = Edge(12, vextex2, vextex3)
        edge6 = Edge(4, vextex2, vextex8)

        edge7 = Edge(7, vextex8, vextex3)
        edge8 = Edge(6, vextex8, vextex6)
        edge9 = Edge(5, vextex5, vextex8)

        edge10 = Edge(4, vextex5, vextex6)
        edge11 = Edge(20, vextex5, vextex7)
        edge12 = Edge(1, vextex6, vextex3)

        edge13 = Edge(13, vextex6, vextex7)
        edge14 = Edge(3, vextex3, vextex4)
        edge15 = Edge(11, vextex3, vextex7)

        edge16 = Edge(9, vextex4, vextex7)

        # handle the neighbor
        vextex1.adjacency_list.append(edge1)
        vextex1.adjacency_list.append(edge2)
        vextex1.adjacency_list.append(edge3)

        vextex2.adjacency_list.append(edge4)
        vextex2.adjacency_list.append(edge5)
        vextex2.adjacency_list.append(edge6)

        vextex8.adjacency_list.append(edge7)
        vextex8.adjacency_list.append(edge8)

        vextex5.adjacency_list.append(edge9)
        vextex5.adjacency_list.append(edge10)
        vextex5.adjacency_list.append(edge11)

        vextex6.adjacency_list.append(edge12)
        vextex6.adjacency_list.append(edge13)
        vextex3.adjacency_list.append(edge14)
        vextex3.adjacency_list.append(edge15)
        vextex4.adjacency_list.append(edge16)
        algo=DijkstraAlgo()
        algo.calculate(vextex1)
        algo.get_shortest_path(vextex7)
        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
