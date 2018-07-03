#risolutore problema con DFS
from ConnectedComponent.CC import *
from pythonConstraint import drawCurrentShape
from time import time

def DFSSolver(shape_array, fixed_variable, grid, PG,screen,min_cc_choice):
    assignment = [(x.color,x.domain[0]) for x in fixed_variable]
    shape_array = list(set(shape_array)^set(fixed_variable))
    t0 = time()
    DFS(assignment, shape_array, grid, PG, screen, min_cc_choice)
    return time() - t0

def DFS(assignment, shape_array, grid, PG, screen, min_cc_choice):
    if not shape_array:
        return assignment

    next_var = shape_array[0]
    for value in next_var.domain:
        if isConsistent(value, assignment,min_cc_choice): 
            assignment.append((next_var.color, value))
            drawCurrentShape(value,next_var.color,grid,PG,None,screen)
            result = DFS(assignment, shape_array[1:], grid, PG, screen,min_cc_choice)
            if result != None:
                return result
            assignment.remove((next_var.color, value))

    return None


def isConsistent(value, assignment,min_cc_choice):
    for a in assignment:
        for coord in value:
            #a is a tupla (color,position)
            if coord in a[1]:
                return False
    if min_cc_choice:
        partial_assignment = [x[1] for x in assignment] + [value]
        if 0 < minCC(partial_assignment) <= 2:
            return False
    return True
