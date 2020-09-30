def readTextFromFile(targetFile):
    f = open(targetFile, 'r')
    lines = f.readlines()
    f.close

    lines = list(set(lines))
    lines.sort()

    nf = open("new "+targetFile, 'w')
    for line in lines :
        nf.write(line)

    nf.close

readTextFromFile("text.txt")

