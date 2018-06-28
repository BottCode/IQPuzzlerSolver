from shape import *
import os
import numpy as np


class buildShapes:
    def __init__(self,shapes_path,domains_path,row,column):
        self.shape_array = []
        f = np.loadtxt(shapes_path,delimiter="\t")
        for line in f:
            i = 0
            number_of_code = line[i]
            codes_array = []
            for k in range(number_of_code):
                code_lst = [int(j) for j in line[k+1]] # potrebbe servire str(line[k+1])?
                codes_array.append(code_lst)
            i = i + number_of_code
            color = line[i+1]
            name = line[i+2]
            domain = buildDomain(domains_path,codes_array)
            self.shape_array.append(Shape(codes_array,color,name))


    def buildDomain(self,domains_path,codes_array,row,column):
        if os.path.getsize(domains_path) > 0:
            dom_file = np.loadtxt(domains_path,delimiter="\t")
            # i-esima forma è i-esima riga
            # words = line[i].split() 
        else:
            generateDomain(row,column)


    def generateDomain(self,row,column,codes_array):
        coordinates = []
        dom = []
        directions = [(-1,1),(-1,-1),(1,1),(1,-1)] # UDX, USX, DDX, DSX
        map_shape_to_direction = {}
        is_buildable = True
        # all the grid coordinates [(0,0),(0,2)...]
        for x in range(row):
            for y in range(column):
                if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                    coordinates.append((x,y))
        
        for coord in coordinates:
            for dirs in directions:
                coord_list = [coord]
                i = 0
                map_shape_to_direction[0] = dirs
                for code in codes_array:
                    for arc in code:
                        if arc in map_shape_to_direction:
                            d = map_shape_to_direction[arc]
                            new_coord = (coord[0] + d[0],coord[1] + d[1])
                            if isCoordinateValid(new_coord,row,column):
                                coord_list.append(new_coord)
                                coord = new_coord
                            else:
                                coord_list[i].remove()

    def isCoordinateValid(new_coord,row,column):
        return True

                             



        


    def getShapes(self):
        return self.shape_array

            

