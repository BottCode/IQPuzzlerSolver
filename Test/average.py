PATH = "Test/testResult.txt"
TABLE_LATEX_PATH ="Test/tableResult.txt"

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
        if words[len(words) - 1] != "FAIL":
            total_time += float(words[len(words) - 4])
            total_steps += float(words[len(words) - 2])
            n += 1
            if line_number % 6 == 0:
                avg_time = total_time / n
                avg_steps = total_steps / n
                data = (str(avg_time)[:6], str(avg_steps)[:7])
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
                           
    
        line_number += 1

computeAverage()
#print("\\begin{table} \\begin{tabular}{|l||*{4}{c|}}\\hline\\backslashbox{Miglioria}{Solver}&\\makebox{DFS}&\\makebox{Backtracking}&\\makebox{Recursive Backtracking}	&\\makebox{MinConflicts}\\\\ \\hline Sì&" + dict_data["DFSm"][0] + (dict_data["DFSm"][1]) + "&" + dict_data["BTm"][0] + (dict_data["BTm"][1])+"&"+dict_data["RBTm"][0] + (dict_data["RBTm"][1])+"&"+dict_data["MCm"][0] + (dict_data["MCm"][1])  +" \\\\ \\hline No&"+dict_data["DFS"][0] + (dict_data["DFS"][1])+"&"+dict_data["BT"][0] + (dict_data["BT"][1])+"&"+dict_data["RBT"][0] + (dict_data["RBT"][1])+"&"+dict_data["MC"][0] + (dict_data["MC"][1]) +"  \\\\ \\hline \\end{tabular}")


