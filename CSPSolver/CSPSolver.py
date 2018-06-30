from pythonConstraint import * 
from ConnectedComponent.CC import minCC, checkCoordConstraint


def CSPSolver(shape_array, csp_type_choice,grid, PG,clock,screen):
    problem = Problem()
    for shape in shape_array:
        #print(shape.name)
        problem.addVariable(shape.color, shape.domain)
        problem.addConstraint(lambda v : minCC(v) > 2, [shape.color])

    for i in range(len(shape_array)):
        for j in range(i+1, len(shape_array)):
            problem.addConstraint(lambda a,b: checkCoordConstraint(a,b), [shape_array[i].color, shape_array[j].color])

    return problem.getSolution(grid,PG,clock,screen)     