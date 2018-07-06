PATH = 'testResult.txt'

def computeAverage():
    f = open(PATH, "a+")
    line_number = 1
    n = 0
    total_time, total_steps, avg_time, avg_steps = 0, 0, 0, 0
    for line in f:
        words = line.split()
        if words[len(words) - 1] != "FAIL":
            total_time += float(words[len(words) - 4])
            total_steps += float(words[len(words) - 2])
            n += 1
            if line_number % 6 == 0:
                avg_time = total_time / n
                avg_steps = total_steps / n
                n = 0
                avg_report = ""
                if "CC" in words or "Restart" in words:
                    avg_report = [word + " " in for word in words[:9]]
                else:
                    avg_report = [word + " " in for word in words[:5]]
                f.write(avg_report + "AVG TIME: " + avg_time + ", AVG STEPS: " + avg_steps)
                
        line_number += 1