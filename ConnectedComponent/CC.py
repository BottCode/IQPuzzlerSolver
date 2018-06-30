from Grid.grid import Grid


def DFSVisited(grid,u,visited,color):
    color[u] = "gray"
    visited.append(u)
    for v in grid.adj_list[u]:
        if (color[v] == "white"):
            visited = DFSVisited(grid,v,visited,color)
    color[u] = "black"
    return visited


def minCC(shape_position):
    grid = Grid(11,9)
    grid.deleteShapePosition(shape_position)
    color = dict()
    for i in grid.adj_list.keys():
        color[i] = "white"
    CC = []
    for i in grid.adj_list.keys():
        if (color[i] == "white"):
            comp = DFSVisited(grid,i,[],color)
            CC.append(comp)
    if not CC:
        return 0
    return min(len(l) for l in CC)

def checkCoordConstraint(a,b):
    for el in a:
        if el in b:
            return False
    return True
