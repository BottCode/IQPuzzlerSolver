# this script is used exclusively to generate starting configurations of the game

from Shape.shape import *
from Shape.buildShapes import *
from Grid.grid import *

def getConfig(n,path):
    grid = Grid(11,9)
    fixed_variables = []
    shape_array = []
    for shape in _generateConfig(n):
        fixed_variables.append(shape)
        shape_array.append(shape)
    shape_array.extend(buildShapes(path,grid,fixed_variables))
    return (fixed_variables,shape_array)


def _generateConfig(n):
    if n == 0:
        return _easy1()
    elif n == 1:
        return _easy2()
    elif n == 2:
        return _medium1()
    elif n == 3:
        return _medium2()
    elif n == 4:
        return _medium3()
    elif n == 5:
        return _hard1()
    else:    
        return _hardest()

def _hardest():
    return []

def _hard1():
    return [Shape([],"blue","L",[[(0,0),(1,1),(2,2),(3,3),(2,4)]]),
            Shape([],"violet","I",[[(2,0),(3,1),(4,2),(5,3)]]),
            Shape([],"red","P",[[(4,0),(5,1),(6,0),(6,2),(7,1)]])]

def _medium1():
    return [Shape([],"lightgreen","T",[[(0,0),(1,1),(2,0),(0,2)]]),
            Shape([],"blue","L",[[(0,4),(1,3),(2,2),(3,1),(4,2)]]),
            Shape([],"brown","Z",[[(4,0),(5,1),(6,0),(7,1)]]),
            Shape([],"yellow","C",[[(5,3),(6,2),(6,4),(7,5),(8,4)]]),
            Shape([],"pink","Y",[[(7,3),(8,2),(9,1),(10,0),(8,0)]])]

def _medium2(): # congif n. 18
    return [Shape([],"purple","W",[[(0,0),(1,1),(0,2),(1,3),(0,4)]]),
            Shape([],"red","P",[[(0,6),(0,8),(1,5),(2,6),(1,7)]]),
            Shape([],"green","BigZ",[[(2,0),(3,1),(2,2),(3,3),(4,4)]]),
            Shape([],"cyan","V",[[(2,4),(3,5),(4,6),(3,7),(2,8)]]),
            Shape([],"lightgreen","T",[[(4,0),(5,1),(6,0),(4,2)]]),
            Shape([],"blue","L",[[(8,0),(7,1),(6,2),(5,3),(6,4)]]),
            Shape([],"white","SmallV",[[(4,8),(5,7),(6,8)]]),
            Shape([],"violet","I",[[(5,5),(6,6),(7,7),(8,8)]])]

def _medium3(): # config n. 32
    return [Shape([],"blue","L",[[(0,0),(1,1),(2,2),(3,3),(2,4)]]),
            Shape([],"purple","W",[[(0,2),(1,3),(0,4),(1,5),(0,6)]]),
            Shape([],"red","P",[[(0,8),(1,7),(2,6),(3,7),(2,8)]]),
            Shape([],"green","BigZ",[[(2,0),(3,1),(4,0),(5,1),(6,2)]]),
            Shape([],"white","SmallV",[[(4,2),(5,3),(4,4)]]),
            Shape([],"cyan","V",[[(6,0),(7,1),(8,2),(7,3),(6,4)]]),
            Shape([],"lightgreen","T",[[(8,0),(9,1),(10,0),(10,2)]])]

def _easy1():
    return []

def _easy2():
    return []

'''# it generates coordinates of T shape (starting from a starting_coord)
def _T(starting_coord):
    coords = []
    x = starting_coord[0]
    y = starting_coord[1]
    # if x-2 < 0 or y-1 < 0:
    #     throw ValueError('Error: Invalid starting coord for shape T.')
    coords.extend([(x,y), (x-1,y+1), (x-2,y+2), (x-2,y)])
    return Shape([],"lightgreen","T",[coords])


def _BigZ(starting_coord):
    coords = []
    x = starting_coord[0]
    y = starting_coord[1]
    # if x+4 >= column or y+2 >= row:
    #     throw ValueError('Error: Invalid starting coord for shape L.')
    coords.extend([(x,y), (x+1,y+1), (x,y+2), (x+1,y+3), (x+2,y+4)])
    return Shape([],"green","BigZ",[coords])

def _I(starting_coord):
    coords = []
    x = starting_coord[0]
    y = starting_coord[1]
    coords.extend([(x,y), (x+1,y+1), (x+2,y+2), (x+3,y+3)])
    return Shape([],"violet","I",[coords])

def _C(starting_coord):
    coords = []
    x = starting_coord[0]
    y = starting_coord[1]
    coords.extend([(x,y), (x-1,y+1), (x,y+2), (x+1,y+3), (x+2,y+2)])
    return Shape([],"yellow","C",[coords])
'''