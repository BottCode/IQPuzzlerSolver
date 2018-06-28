from Grid.grid import *
from Shape.shape import *
from Shape.buildShapes import *
from Configurations.generateConfig import *
from constraint import *
from View.view import *

difficulty = 3 # difficulty in range(5)
fixed_variable = []
problem = Problem()

for shape in Hard1():
    problem.addVariable(shape.name,shape.domain)
    print(shape.name," ",shape.domain[0],"\n")
    fixed_variable.append((shape.color,shape.domain[0]))
    # the allowed value for the variable is the only value which exists in its domain
    problem.addConstraint(lambda v : v == shape.domain[0], shape.name)

startDraw(fixed_variable)
path = './shape_code.txt'
grid = Grid(11,9)
print(fixed_variable)
array = buildShapes(path,path,grid,fixed_variable)

# print(array[0].domain)
# print(len(array[0].domain))
