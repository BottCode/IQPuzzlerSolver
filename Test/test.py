PATH = "Test/testResult.txt" 
SCRIPT_PATH = "Test("
def writeReport(total_solving_time,steps,difficulty,solution_choice,smart_choice):
    report = "\nLevel " + str(difficulty) + ", solved with"
    if solution_choice == 1:
        report += " DFS "
    elif solution_choice == 3:
        report += " RecBT "
    elif solution_choice == 4:
        report += " MinConfl "
    else:
        report += " BT "
    
    if smart_choice and solution_choice != 4:
        report += "with CC check"
    elif smart_choice:
        report += "with Random Restart technique"
    
    if steps >= 0:
        report += " solved in: " + str(total_solving_time) + " in " + str(steps) + " steps"
    else:
        report += " FAIL "
    
    with open(PATH,"a") as report_file:
        report_file.write(report)

