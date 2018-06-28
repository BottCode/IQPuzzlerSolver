# this script is used exclusively to generate starting configurations of the game

from Shape.shape import *

def Hard1():
    return [_T((0,10)), _BigZ((0,0))]

def Medium1():
    return [_T((0,10)), _BigZ((0,0)), _I((0,2))]

def Medium2():
    return [_C((6,4)), _BigZ((0,0)), _I((0,2))]

def Easy1():
    return [_C((6,4)), _BigZ((0,0)), _I((0,2)), _T((0,10))]


# it generates coordinates of T shape (starting from a starting_coord)
def _T(starting_coord):
    coords = []
    x = starting_coord[0]
    y = starting_coord[1]
    # if x-2 < 0 or y-1 < 0:
    #     throw ValueError('Error: Invalid starting coord for shape T.')
    coords.extend([(x,y), (x+1,y-1), (x+2,y-2), (x,y-2)])
    return Shape([],"lightgreen","T",[coords])


def _BigZ(starting_coord):
    coords = []
    x = starting_coord[0]
    y = starting_coord[1]
    # if x+4 >= column or y+2 >= row:
    #     throw ValueError('Error: Invalid starting coord for shape L.')
    coords.extend([(x,y), (x+1,y+1), (x+2,y), (x+3,y+1), (x+4,y+2)])
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