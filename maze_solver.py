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
    #def is_valid(self):

