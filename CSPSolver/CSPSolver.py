from pythonConstraint import *
from ConnectedComponent.CC import minCC, checkCoordConstraint
from time import time

def CSPSolver(shape_array, csp_type_choice,grid, PG,clock,screen,min_cc_choice):
    problem = None

    if csp_type_choice == 3:
        problem = Problem(RecursiveBacktrackingSolver())
    elif csp_type_choice == 4:
        problem = Problem(MinConflictsSolver())
    else:
        problem = Problem()

    for shape in shape_array:
        #print(shape.name)
        problem.addVariable(shape.color, shape.domain)
        problem.addConstraint(lambda v : minCC([v]) > 2, [shape.color])

    for i in range(len(shape_array)):
        for j in range(i+1, len(shape_array)):
            problem.addConstraint(lambda a,b: checkCoordConstraint(a,b), [shape_array[i].color, shape_array[j].color])

    t0 = time()
    problem.getSolution(grid,PG,clock,screen,min_cc_choice)
    return time() - t0
