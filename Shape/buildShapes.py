from Shape.shape import *
from Grid.grid import *
import os
import numpy as np
from ConnectedComponent.CC import *


def buildShapes(shapes_path,domains_path, grid,fixed_variables):
    shape_array = []
    f = open(shapes_path, "r")
    name_fixed_variables = [shape[2] for shape in fixed_variables]
    
    for line in f:
        words = line.split()
        name = words[0]
        if name not in name_fixed_variables:
            print("COSTRUISCO",name)
            print(name_fixed_variables)
            i = 1
            number_of_code = int(words[i])
            codes_array = []
            for k in range(number_of_code):
                code_lst = [int(j) for j in str(words[k+2])]
                codes_array.append(code_lst)
            i = i + number_of_code
            color = words[i+1]
            print(color)
            domain = buildDomain(domains_path,codes_array, grid)
            shape_array.append(Shape(codes_array,color,name, domain))

    return shape_array


def buildDomain(domains_path,codes_array, grid):
    '''if os.path.getsize(domains_path) > 0:
        dom_file = np.loadtxt(domains_path,delimiter="\t")
        # i-esima forma è i-esima riga
        # words = line[i].split()
    else:'''
    return generateDomain(grid, codes_array)


def generateDomain(grid, codes_array):
    dom = []
    directions = [(-1,1),(-1,-1),(1,1),(1,-1)] # UDX, USX, DDX, DSX
    map_shape_to_direction = {}

    for dir in directions:
        map_shape_to_direction[0] = dir
        possible1 = possibleDirection(directions, map_shape_to_direction, dir)
        for dir_1 in possible1:
            map_shape_to_direction[1] = dir_1
            possible2 = possibleDirection(directions, map_shape_to_direction, dir_1)
            for dir_2 in possible2:
                map_shape_to_direction[2] = dir_2
                possible3 = possibleDirection(directions, map_shape_to_direction, dir_2)
                for dir_3 in possible3:
                    map_shape_to_direction[3] = dir_3
                    #print(map_shape_to_direction)
                    dom.extend(findPossibleDomain(grid, map_shape_to_direction, codes_array))

                    del map_shape_to_direction[3]
                del map_shape_to_direction[2]
            del map_shape_to_direction[1]

    return dom

def findPossibleDomain(grid, map_shape_to_direction, codes_array):
    domain = []
    for coord in grid.coordinates:
        isValid = True
        coord_list = set()
        coord_list.add(coord)
        initial_coord = coord
        for code in codes_array:
            coord = initial_coord
            if isValid:
                for arc in code:
                    #print("ARC",arc)
                    d = map_shape_to_direction[arc]
                    new_coord = (coord[0] + d[0],coord[1] + d[1])
                    if grid.isCoordinateValid(new_coord, grid.row, grid.column):
                        coord_list.add(new_coord)
                        coord = new_coord
                    else:
                        isValid = False
                        break
            else:
                break
        if isValid:
            '''g = Grid(grid.row, grid.column)'''''' and (minCC(g, coord_list) > 2)'''
            #print(coord_list)
            #print("DOMAIN",domain)
            if list(coord_list) not in domain:
                domain.append(list(coord_list))
            #else:
                #print("INDOMAINS")

    return domain

def possibleDirection(directions, map_shape_to_direction, last_direction):
    #return the possible value after a change of direction
    notExploredDirection = [x for x in directions if x not in map_shape_to_direction.values()]
    if (-last_direction[0],-last_direction[1]) in notExploredDirection:
        notExploredDirection.remove((-last_direction[0],-last_direction[1]))
    return notExploredDirection

def getShapes(self):
    return self.shape_array
