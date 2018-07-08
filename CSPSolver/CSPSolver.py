from pythonConstraint import Problem, RecursiveBacktrackingSolver, MinConflictsSolver
from ConnectedComponent.CC import minCC, checkCoordConstraint
from time import time
from Shape.buildShapes import getMinimunDimension

def CSPSolver(shape_array, csp_type_choice,grid, PG,screen,smart_choice):
    problem = None

    if csp_type_choice == 3:
        problem = Problem(RecursiveBacktrackingSolver())
    elif csp_type_choice == 4:
        problem = Problem(MinConflictsSolver())
    else:
        problem = Problem()

    min_dimension = getMinimunDimension(shape_array)
    for shape in shape_array:
        #print(shape.name)
        problem.addVariable(shape.color, shape.domain)
        problem.addConstraint(lambda v : minCC([v]) >= min_dimension, [shape.color])

    for i in range(len(shape_array)):
        for j in range(i+1, len(shape_array)):
            problem.addConstraint(lambda a,b: checkCoordConstraint(a,b), [shape_array[i].color, shape_array[j].color])

    t0 = time()
    steps = problem.getSolution(grid,PG,screen,smart_choice)
    print("SOL",steps)
    return time() - t0, steps
