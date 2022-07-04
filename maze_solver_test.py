import unittest
from maze_solver import MazeSolver


class TestMazeSolver(unittest.TestCase):
    def test_maze_solver(self):
        m = [
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1]
        ]
        maze_solver = MazeSolver(m)
        maze_solver.search(0, 0, 4, 4)
        maze_solver.show_result()


if __name__ == '__main__':
    unittest.main()
