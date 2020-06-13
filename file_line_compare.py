import sys


def read_file(file):
    lines = [line.rstrip('\n') for line in open(file)]
    return lines


if len(sys.argv) == 3:
    lines1 = read_file(sys.argv[1])
    lines2 = read_file(sys.argv[2])
    for i in range(len(lines1)):
        diff = True
        for j in range(len(lines2)):
            if lines1[i] == lines2[j]:
                diff = False
        if diff:
            print(sys.argv[1] + ',#' + str(i) + ': ' + lines1[i] + '\n' + sys.argv[2] + ',#' + str(i) + ': ' + lines2[i] + '\n')
