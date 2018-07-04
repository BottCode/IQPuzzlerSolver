# this script is used exclusively to generate starting configurations of the game

from Shape.shape import Shape
from Shape.buildShapes import buildShapes
from Grid.grid import Grid

def getConfig(n,path):
    grid = Grid(11,9)
    fixed_variables = []
    shape_array = []
    for shape in _generateConfig(n):
        fixed_variables.append(shape)
        shape_array.append(shape)
        grid.deleteShapePosition(shape.domain[0])
    shape_array.extend(buildShapes(path,grid,fixed_variables))
    return (fixed_variables,shape_array)


def _generateConfig(n):
    if n == 0:
        return _easy1()
    elif n == 1:
        return _medium1()
    elif n == 2:
        return _medium2()
    elif n == 3:
        return _hard1()
    elif n == 4:
        return _hardest()

def _easy1(): # congif n. 18
    return [Shape([],"purple","W",[[(0,0),(1,1),(0,2),(1,3),(0,4)]],5),
            Shape([],"red","P",[[(0,6),(0,8),(1,5),(2,6),(1,7)]],5),
            Shape([],"green","BigZ",[[(2,0),(3,1),(2,2),(3,3),(4,4)]],5),
            Shape([],"cyan","V",[[(2,4),(3,5),(4,6),(3,7),(2,8)]],5),
            Shape([],"lightgreen","T",[[(4,0),(5,1),(6,0),(4,2)]],4),
            Shape([],"blue","L",[[(8,0),(7,1),(6,2),(5,3),(6,4)]],5),
            Shape([],"orange","SmallV",[[(4,8),(5,7),(6,8)]],3),
            Shape([],"violet","I",[[(5,5),(6,6),(7,7),(8,8)]],4)]

def _medium1(): # config n. 32
    return [Shape([],"blue","L",[[(0,0),(1,1),(2,2),(3,3),(2,4)]],5),
            Shape([],"purple","W",[[(0,2),(1,3),(0,4),(1,5),(0,6)]],5),
            Shape([],"red","P",[[(0,8),(1,7),(2,6),(3,7),(2,8)]],5),
            Shape([],"green","BigZ",[[(2,0),(3,1),(4,0),(5,1),(6,2)]],5),
            Shape([],"orange","SmallV",[[(4,2),(5,3),(4,4)]],3),
            Shape([],"cyan","V",[[(6,0),(7,1),(8,2),(7,3),(6,4)]],5),
            Shape([],"lightgreen","T",[[(8,0),(9,1),(10,0),(10,2)]],4)]

def _medium2(): # config n. 68
    return [Shape([],"lightgreen","T",[[(0,0),(1,1),(2,0),(0,2)]],4),
            Shape([],"blue","L",[[(0,4),(1,3),(2,2),(3,1),(4,2)]],5),
            Shape([],"brown","Z",[[(4,0),(5,1),(6,0),(7,1)]],4),
            Shape([],"yellow","C",[[(5,3),(6,2),(6,4),(7,5),(8,4)]],5),
            Shape([],"pink","Y",[[(7,3),(8,2),(9,1),(10,0),(8,0)]],5)]

def _hard1():
    return [Shape([],"blue","L",[[(0,0),(1,1),(2,2),(3,3),(2,4)]],5),
    Shape([],"violet","I",[[(2,0),(3,1),(4,2),(5,3)]],4),
    Shape([],"red","P",[[(4,0),(5,1),(6,0),(6,2),(7,1)]],5)]

def _hardest():
    return []
