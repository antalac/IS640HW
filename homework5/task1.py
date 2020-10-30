logfile = open("homework5/log.txt", "w")
try:
    file1 = open("homework5/scores.txt", "r")
    lines = file1.readlines()
    scores = []
    for line in lines:
        linesplit = line.split(' ')
        try:
            scores.append(int(linesplit[1]))
        except:
            logfile.write(f'Bad score value for {linesplit[0]}, ignored \n')
    classavg = sum(scores) / len(scores)
    logfile.write(f'The class average is {classavg} for {len(scores)} students \n')
except Exception as e:
    print(f'error exception {e}')
    