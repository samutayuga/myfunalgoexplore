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
        # 1. initial distance is 0
        # 2. i,j is initial position for x and y
        queue.append((i, j, 0))
        # 3. Continue the iteration while the queue is not empty
        while queue:
            # 4. Get the fist item inserted into the queue
            (i, j, dist) = queue.popleft()
            # 5.  check if we reach the destination
            if i == destination_x and j == destination_y:
                # 6.  update the min distance with the updated one
                self.min_distance = dist
                # 7.  means the algorithm will stop
                break
            # 8. In case this is not yet in the destination we have to make a given mode
            # possible move, UP, DOWN, LEFT, RIGHT
            for move in range(len(self.move_x)):
                # try RIGHT,UP,DOWN,LEFT
                next_x, next_y = i + self.move_x[move], j + self.move_y[move]
                # 9. For all possible move check if it is valid
                if self.is_valid(next_x, next_y):
                    # 10. in case it is a valid move, update the visited flag to True
                    self.visited[next_x][next_y] = True
                    # 11. push the updated position into the queue, with the updated minimum distance
                    # the object pushed into the queue is the tuple with structure
                    # (updated_x_loc,updated_y_loc,min_dist)
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):
        if self.min_distance != float('inf'):
            print("The shortest path from source to destination: ", self.min_distance)
        else:
            print("No feasible solution - the destination cannot be reached !!")
