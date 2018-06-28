from Shape.buildShapes import *

class Grid:
    def __init__(self, row, column):
        self.coordinates = []
        self.row = row
        self.column = column

        for x in range(row):
            for y in range(column):
                if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                    self.coordinates.append((x,y))

        self.adj_list = {}
        directions = [(-1,1),(-1,-1),(1,1),(1,-1)]
        for coord in self.coordinates:
            adj = []
            for dir in directions:
                neigh = (coord[0] + dir[0], coord[1] + dir[1])
                if isCoordinateValid(neigh, self.row, self.column):
                    adj.append(neigh)

            self.adj_list[coord] = adj
