from Configurations.generateConfig import getConfig
# from CSPSolver.CSPSolver import CSPSolver
from DFSSolver.DFSSolver import DFSSolver
from View.view import *
import itertools
import sys

path = './shape_code.txt'
solution = []

difficulty, solution_choice,min_cc_choice = 0, 0, 0
is_test_mode = False

if len(sys.argv) == 3+1:
    is_test_mode = True
    difficulty = int(sys.argv[1])
    solution_choice = int(sys.argv[2])
    min_cc_choice = int(sys.argv[3])
else:
    difficulty = int(input("Select difficulty level from 0 to 4:\n"))
    solution_choice = int(input("Select how to solve IQPuzzler \n 1: DFS \n 2: Deafult Backtracking \n 3: Recursive Backtracking \n 4: MinConflicts Backtracking \n"))
    min_cc_choice = int(input("Would you a like to use the \"Connected Components\" checks? \n 0: No \n 1: Yes \n"))

fixed_variables, shape_array = getConfig(difficulty,path)
startingDraw(fixed_variables, shape_array, solution_choice, min_cc_choice, difficulty, is_test_mode)
 

