import numpy


class Model:

    def __init__(self, cells_amount_x, cells_amount_y):
        self.cells_amount_x = cells_amount_x
        self.cells_amount_y = cells_amount_y
        self.set_initial_position()


    def set_initial_position(self):
        self.grid = numpy.zeros((self.cells_amount_y, self.cells_amount_x))
        start_pattern = numpy.array([[1, 0, 0],
                                     [1, 1, 1],
                                     [0, 1, 0]]).transpose()
        pos = (30, 30)
        self.grid[pos[0]:pos[0]+start_pattern.shape[0], pos[1]:pos[1]+start_pattern.shape[1]] = start_pattern
        pos = (10, 10)
        self.grid[pos[0]:pos[0]+start_pattern.shape[0], pos[1]:pos[1]+start_pattern.shape[1]] = start_pattern


    def update(self):
        new_grid = numpy.zeros((self.grid.shape[0], self.grid.shape[1]))

        for x, y in numpy.ndindex(self.grid.shape):
            neighborhood = numpy.sum(self.grid[x-1:x+2, y-1:y+2]) - self.grid[x, y]

            if (self.grid[x, y] == 1 and 2 <= neighborhood <= 3) or (self.grid[x, y] == 0 and neighborhood == 3):
                new_grid[x, y] = 1
        self.grid = new_grid