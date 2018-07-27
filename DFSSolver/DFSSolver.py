#risolutore problema con DFS
from ConnectedComponent.CC import minCC
from pythonConstraint import drawCurrentAssignemnt
from time import time

STEPS = 0

def DFSSolver(shape_array, fixed_variable, grid, PG,screen,smart_choice):
    assignment = {}
    for var in fixed_variable:
        assignment[var.color] = var.domain[0]
    shape_array = list(set(shape_array)^set(fixed_variable))
    t0 = time()
    sol, steps = DFS(assignment, shape_array, grid, PG, screen, smart_choice)
    return time() - t0, steps

def DFS(assignment, shape_array, grid, PG, screen, smart_choice):
    global STEPS
    if not shape_array:
        return assignment, STEPS

    next_var = shape_array[0]
    for value in next_var.domain:
        if isConsistent(value, assignment, shape_array, smart_choice):
            assignment[next_var.color] = value
            drawCurrentAssignemnt(assignment,grid,PG,screen)
            STEPS += 1
            result, STEPS = DFS(assignment, shape_array[1:], grid, PG, screen,smart_choice)
            if result != None:
                return result, STEPS
            del assignment[next_var.color]

    return None, STEPS


def isConsistent(value, assignment, shape_array, smart_choice):
    for a in assignment:
        for coord in value:
            #a is a tupla (color,position)
            if coord in assignment[a]:
                return False

    if smart_choice:
        min_dimension = min([var.dimension for var in shape_array])

        partial_assignment = [assignment[x] for x in assignment] + [value]
        if 0 < minCC(partial_assignment) < min_dimension:
            return False
    return True
