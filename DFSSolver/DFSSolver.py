#risolutore problema con DFS

def DFSSolver(shape_array, fixed_variable, grid, PG,screen):
    assignment = [(x.color,x.domain[0]) for x in fixed_variable]
    shape_array = list(set(shape_array)^set(fixed_variable))
    solution = DFS(assignment, shape_array, grid, PG, screen)
    print(solution)

def DFS(assignment, shape_array, grid, PG, screen):
    if not shape_array:
        return assignment

    next_var = shape_array.pop(0)
    for value in next_var.domain:
        if isConsistent(value, assignment):
            assignment.append((next_var.color, value))
            result = DFS(assignment, shape_array, grid, PG, screen)
            if result != None:
                return result
            assignment.remove((next_var.color, value))
    return None


def isConsistent(value, assignment):
    for a in assignment:
        for coord in value:
            #a is a tupla (color,position)
            if coord in a[1]:
                return False
    return True
