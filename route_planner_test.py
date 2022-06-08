import unittest

from route_planner import route_planner


class RoutePlannerTest(unittest.TestCase):
    def test_route(self):
        m = [0 for _ in range(0, 5)]
        m[0] = [True, False, False]
        m[1] = [True, True, False]
        m[2] = [False, True, False]
        m[3] = [False, True, True]
        m[4] = [False, True, True]

        route_planner(m=m, a=[0, 0, 4, 2])


if __name__ == '__main__':
    unittest.main()
