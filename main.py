from Grid.grid import *
from Shape.shape import *
from Shape.buildShapes import *
from Configurations.generateConfig import generateConfig
from constraint import *
from View.view import *
from ConnectedComponent.CC import *

difficulty = 4 # difficulty in range(6)
fixed_variables = []
problem = Problem()
array_shape = []

for shape in generateConfig(difficulty):
    fixed_variables.append(shape)
    array_shape.append(shape)
    # the allowed value for the variable is the only value which exists in its domain
    #problem.addConstraint(lambda v : v == shape.domain[0], shape.name)
# startDraw(fixed_variables)

path = './shape_code.txt'
grid = Grid(11,9)
array_shape.extend(buildShapes(path,grid,fixed_variables))

for shape in array_shape:
    print(shape.name)
    problem.addVariable(shape.color, shape.domain)
    problem.addConstraint(lambda v : minCC(Grid(11,9), v) > 2, [shape.color])


for i in range(len(array_shape)):
    for j in range(i+1, len(array_shape)):
        problem.addConstraint(lambda a,b: checkCoordConstraint(a,b), [array_shape[i].color, array_shape[j].color])

solution = problem.getSolution()
print(solution)

drawSolution(fixed_variables, solution)

# drawSingleShape((array[0].color,array[0].domain[0]))

#def sillySolver(fixed_variables,array):


#print(array[0].domain)
#print(len(array[0].domain))
