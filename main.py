from Grid.grid import *
from Shape.shape import *
from Shape.buildShapes import *
from Configurations.generateConfig import generateConfig
from constraint import *
from View.view import *
from ConnectedComponent.CC import *

difficulty = 0 # difficulty in range(6)
fixed_variables = []
problem = Problem()

for shape in generateConfig(difficulty):
    problem.addVariable(shape.name,shape.domain)
    fixed_variables.append((shape.color,shape.domain[0],shape.name))
    # the allowed value for the variable is the only value which exists in its domain
    problem.addConstraint(lambda v : v == shape.domain[0], shape.name)
# startDraw(fixed_variables)

path = './shape_code.txt'
grid = Grid(11,9)
array = buildShapes(path,path,grid,fixed_variables)
FAKE_solution = [(shape.color,shape.domain[0],shape.name) for shape in array]
drawSolution(fixed_variables,FAKE_solution)

# drawSingleShape((array[0].color,array[0].domain[0]))

#def sillySolver(fixed_variables,array):


#print(array[0].domain)
print(len(array[0].domain))
