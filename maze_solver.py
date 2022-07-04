from collections import deque


class MazeSolver:
    def __init__(self, matrix):
        self.matrix = matrix
        # model the move right, left, above, below
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        # move right, (move_x[0],move_y[0])
        # initialize the maze with the visited status
        self.visited = [[False for _ in range(len(self.matrix))] for _ in range(len(self.matrix))]
        self.min_distance = float('inf')

    def is_valid(self, row, col):
        """
        Check if a location for a given row and column
        is valid. Assume the matrix is square matrix
        :param row:
        :param col:
        :return:
        """
        if row < 0 or row >= len(self.matrix):
            return False
        if col < 0 or col >= len(self.matrix):
            return False
        if self.matrix[row][col] == 0:
            return False
        if self.visited[row][col]:
            return False

        return True

    def search(self, i, j, destination_x, destination_y):
        """
        This the BFS implementation


        :param i: is the initial x position
        :param j: is the initial y position
        :param destination_x: is the destination x position
        :param destination_y: is the destination y position
        :return:
        """
        self.visited[i][j] = True

        queue = deque()
        # initial distance is 0
        # i,j is initial position for x and y
        queue.append((i, j, 0))

        while queue:
            (i, j, dist) = queue.popleft()
            # check if we reach the destination
            # means the algorithm will stop
            if i == destination_x and j == destination_y:
                self.min_distance = dist
                break
            # we are at the location (i,j) we have to make a given mode
            # possible move, UP, DOWN, LEFT, RIGHT
            for move in range(len(self.move_x)):
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]
                if self.is_valid(next_x, next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):
        if self.min_distance != float('inf'):
            print("The shortest path from source to destination: ", self.min_distance)
        else:
            print("No feasible solution - the destination cannot be reached !!")
