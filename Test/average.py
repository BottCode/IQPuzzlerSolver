PATH = "Test/testResult.txt"
TABLE_LATEX_PATH ="Test/tableResult.txt"
SCRIPT_PATH = "Test/scriptTest.sh"
TEST_FOR_EACH_COMB = 40

def computeAverage():
    open(TABLE_LATEX_PATH,"w").close()
    f = open(PATH, "r")
    line_number = 1
    n = 0
    total_time, total_steps, avg_time, avg_steps = 0, 0, 0, 0
    dict_data = {
        "DFS": ("",""),
        "DFSm": ("",""),
        "BT": ("",""),
        "BTm": ("",""),
        "RBT": ("",""),
        "RBTm": ("",""),
        "MC": ("",""),
        "MCm": ("","")
    } 
    for line in f:
        words = line.split()
        if "STOP" in words:
            break
        print(line,line_number)
        if words[len(words) - 1] != "FAIL":
            total_time += float(words[len(words) - 4])
            total_steps += float(words[len(words) - 2])
            n += 1
            if line_number % TEST_FOR_EACH_COMB == 0:
                avg_time = total_time / n
                avg_steps = total_steps / n
                data = (str(avg_time)[:6], str(avg_steps)[:8])
                avg_report = ""
                if "CC" in words or "Restart" in words:
                    for word in words[:9]:
                        avg_report += word + " "
                    if "DFS" in words:
                        dict_data["DFSm"] = data
                    elif "BT" in words:
                        dict_data["BTm"] = data
                    elif "RecBT" in words:
                        dict_data["RBTm"] = data
                    elif "MinConfl" in words:
                        dict_data["MCm"] = data
                        with open(TABLE_LATEX_PATH,"a") as table_file:
                            table_file.write("\n \\begin{table} \n \\begin{tabular}{|l||*{4}{c|}}\\hline \n \\backslashbox{Miglioria}{Solver} \n &\\makebox{DFS}&\\makebox{Backtracking}&\\makebox{Recursive Backtracking}	&\\makebox{MinConflicts}\\\\ \\hline \n Sì&" + dict_data["DFSm"][0] + " ("+(dict_data["DFSm"][1]) + ")" + "&" + dict_data["BTm"][0] + " ("+ (dict_data["BTm"][1])+")"+"&"+dict_data["RBTm"][0] + " ("+ (dict_data["RBTm"][1])+")&"+dict_data["MCm"][0] + " ("+ (dict_data["MCm"][1])  +") \\\\ \\hline \n No&"+dict_data["DFS"][0] + " ("+ (dict_data["DFS"][1])+")&"+dict_data["BT"][0]+ " (" + (dict_data["BT"][1])+")&"+dict_data["RBT"][0] + " ("+ (dict_data["RBT"][1])+")&"+dict_data["MC"][0] + " ("+ (dict_data["MC"][1]) +")  \\\\ \\hline \n \\end{tabular} \n \\end{table}")
                            for key in dict_data.keys():
                                dict_data[key] = ("","")   
                else:
                    for word in words[:5]:
                        avg_report += word + " "
                    if "DFS" in words:
                        dict_data["DFS"] = data
                    elif "BT" in words:
                        dict_data["BT"] = data
                    elif "RecBT" in words:
                        dict_data["RBT"] = data
                    elif "MinConfl" in words:
                        dict_data["MC"] = data
                avg_report += "AVG TIME: " + str(avg_time)[:6] + ", AVG STEPS: " + str(avg_steps)[:6]
                with open(PATH,"a") as report_file:
                    report_file.write("\n"+avg_report)

                n, total_steps, total_time = 0, 0, 0
        elif line_number % TEST_FOR_EACH_COMB == 0:
                avg_time = total_time / n
                avg_steps = total_steps / n
                data = (str(avg_time)[:6], str(avg_steps))
                avg_report = ""
                if "CC" in words or "Restart" in words:
                    for word in words[:9]:
                        avg_report += word + " "
                    if "DFS" in words:
                        dict_data["DFSm"] = data
                    elif "BT" in words:
                        dict_data["BTm"] = data
                    elif "RecBT" in words:
                        dict_data["RBTm"] = data
                    elif "MinConfl" in words:
                        dict_data["MCm"] = data
                        with open(TABLE_LATEX_PATH,"a") as table_file:
                            table_file.write("\n \\begin{table} \n \\begin{tabular}{|l||*{4}{c|}}\\hline \n \\backslashbox{Miglioria}{Solver} \n &\\makebox{DFS}&\\makebox{Backtracking}&\\makebox{Recursive Backtracking}	&\\makebox{MinConflicts}\\\\ \\hline \n Sì&" + dict_data["DFSm"][0] + " ("+(dict_data["DFSm"][1]) + ")" + "&" + dict_data["BTm"][0] + " ("+ (dict_data["BTm"][1])+")"+"&"+dict_data["RBTm"][0] + " ("+ (dict_data["RBTm"][1])+")&"+dict_data["MCm"][0] + " ("+ (dict_data["MCm"][1])  +") \\\\ \\hline \n No&"+dict_data["DFS"][0] + " ("+ (dict_data["DFS"][1])+")&"+dict_data["BT"][0]+ " (" + (dict_data["BT"][1])+")&"+dict_data["RBT"][0] + " ("+ (dict_data["RBT"][1])+")&"+dict_data["MC"][0] + " ("+ (dict_data["MC"][1]) +")  \\\\ \\hline \n \\end{tabular} \n \\end{table}")
                            for key in dict_data.keys():
                                dict_data[key] = ("","")   
                else:
                    for word in words[:5]:
                        avg_report += word + " "
                    if "DFS" in words:
                        dict_data["DFS"] = data
                    elif "BT" in words:
                        dict_data["BT"] = data
                    elif "RecBT" in words:
                        dict_data["RBT"] = data
                    elif "MinConfl" in words:
                        dict_data["MC"] = data
                avg_report += "AVG TIME: " + str(avg_time) + ", AVG STEPS: " + str(avg_steps)
                with open(PATH,"a") as report_file:
                    report_file.write("\n"+avg_report)                             
    
        line_number += 1

def generateScript():
    with open(SCRIPT_PATH,"a") as script_file:
        script_file.write("#! /bin/sh\n> Test/testResult.txt\n")
        for level in range(5):
            for algorithm in range(1,5):
                for smart in range(2):
                    if not ((level == 3 and algorithm == 1 and smart == 0) or (level == 4 and algorithm == 1)):
                        for _ in range(TEST_FOR_EACH_COMB):
                            script_file.write("python3 main.py "+str(level)+" "+str(algorithm)+" "+str(smart)+ "\n")
            script_file.write("\n")
        script_file.write("echo \"STOP\" >> Test/testResult.txt \n python3 Test/average.py")

#generateScript()
computeAverage()


