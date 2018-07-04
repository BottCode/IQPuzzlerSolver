from Configurations.generateConfig import getConfig
from View.view import startingDraw
import sys

def main():
    SHAPE_CODE_PATH = './shape_code.txt'
    difficulty, solution_choice, min_cc_choice, is_test_mode = 0, 0, 0, False

    if len(sys.argv) == 3 + 1: # sys.argv[0] is file name
        is_test_mode = True
        difficulty = int(sys.argv[1])
        solution_choice = int(sys.argv[2])
        min_cc_choice = int(sys.argv[3])
    else:
        difficulty = int(input("Select difficulty level from 0 to 4:\n"))
        solution_choice = int(input("Select how to solve IQPuzzler \n 1: DFS \n 2: Default Backtracking \n 3: Recursive Backtracking \n 4: MinConflicts Backtracking \n"))
        min_cc_choice = int(input("Would you a like to use the \"Connected Components\" checks? \n 0: No \n 1: Yes \n"))

    fixed_variables, shape_array = getConfig(difficulty,SHAPE_CODE_PATH)

    # this function computes the solution and draw each steps of it
    startingDraw(fixed_variables, shape_array, solution_choice, min_cc_choice, difficulty, is_test_mode)
    

if __name__ == "__main__":
    main()