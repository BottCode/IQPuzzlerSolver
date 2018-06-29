from Grid.grid import *
from Shape.shape import *
from Shape.buildShapes import *
from Configurations.generateConfig import generateConfig
from constraint import *
from View.view import *
from ConnectedComponent.CC import *

'''difficulty = 0 # difficulty in range(6)'''
fixed_variable = []
'''problem = Problem()

for shape in generateConfig(difficulty):
    problem.addVariable(shape.name,shape.domain)
    fixed_variable.append((shape.color,shape.domain[0]))
    # the allowed value for the variable is the only value which exists in its domain
    problem.addConstraint(lambda v : v == shape.domain[0], shape.name)

startDraw(fixed_variable)'''
path = './shape_code.txt'
grid = Grid(11,9)
array = buildShapes(path,path,grid,fixed_variable)


# drawSingleShape((array[0].color,array[0].domain[0]))

#def sillySolver(fixed_variable,array):


#print(array[0].domain)
print(len(array[0].domain))
