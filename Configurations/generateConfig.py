# this script is used exclusively to generate starting configurations of the game

from Shape.shape import *

def generateConfig(n):
    if n == 0:
        return _easy1()
    elif n == 2:
        return _medium1()
    elif n == 3:
        return _medium2()
    elif n == 4:
        return _hard1()

def _hard1():
    return [_T((10,0)), _BigZ((0,0))]

def _medium1():
    return [_T((10,0)), _BigZ((0,0)), _I((2,0))]

def _medium2():
    return [_C((4,6)), _BigZ((0,0)), _I((2,0))]

def _easy1():
    return [_C((4,6)), _BigZ((0,0)), _I((2,0)), _T((10,0))]


# it generates coordinates of T shape (starting from a starting_coord)
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
