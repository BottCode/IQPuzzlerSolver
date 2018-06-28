from Grid.grid import *
from Shape.shape import *
from Shape.buildShapes import *

path = './shape_code.txt'
grid = Grid(11,9)
array = buildShapes(path,path,grid)
print(array[0].domain)
print(len(array[0].domain))
