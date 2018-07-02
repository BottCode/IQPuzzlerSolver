from Configurations.generateConfig import getConfig
# from CSPSolver.CSPSolver import CSPSolver
from DFSSolver.DFSSolver import DFSSolver
from View.view import *


path = './shape_code.txt'
solution = []

# difficulty in range(7)
difficulty = int(input("Select difficulty level from 0 to 6: "))
solution_choice = int(input("Select how to solve IQPuzzler \n 1: DFS \n 2: Deafult Backtracking \n 3: Recursive Backtracking \n 4: MinConflicts Backtracking \n"))

fixed_variables, shape_array = getConfig(difficulty,path)


startingDraw(fixed_variables, shape_array, solution_choice) 

'''
if solution_choice == 1:
    solution = DFSSolver(shape_array) 
else:
    solution = CSPSolver(shape_array,solution_choice) '''
    
#startingDraw(fixed_variables, solution)


#print(array[0].domain)
#print(len(array[0].domain))
