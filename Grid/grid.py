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
                if (neigh[0] < self.row) and (neigh[0] >= 0) and (neigh[1] >= 0) and (neigh[1] < self.column):
                    adj.append(neigh)

            self.adj_list[coord] = adj

    def deleteShapePosition(self, shape_position):
        for coord in shape_position:
            for key in self.adj_list:
                if coord in self.adj_list[key]:
                    self.adj_list[key].remove(coord)

            del self.adj_list[coord]
            self.coordinates.remove(coord)

    def isCoordinateValid(self, new_coord):
        if new_coord not in list(self.adj_list.keys()): # aggiungere il check se le new_coord sono già occupate da fixed variable
            return False
        return True
