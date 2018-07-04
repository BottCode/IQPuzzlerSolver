PATH = "Test/testResult.txt" 

def writeReport(total_solving_time,difficulty,solution_choice,min_cc_choice):
    report = "\nLevel " + str(difficulty) + ", solved with"
    if solution_choice == 1:
        report += " DFS "
    elif solution_choice == 3:
        report += " RecBT "
    elif solution_choice == 4:
        report += " MinConfl "
    else:
        report += " BT "
    
    if min_cc_choice and solution_choice != 4:
        report += "with CC check"
    
    report += " solved in: " + str(total_solving_time)
    
    with open(PATH,"a") as report_file:
        report_file.write(report)