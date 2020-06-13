import sys


def read_file(file):
    lines = [line.rstrip('\n') for line in open(file)]
    return lines


def compare(f1, f2):
    lines1 = read_file(f1)
    lines2 = read_file(f2)
    for i in range(len(lines1)):
        diff = True
        if lines1[i].isspace():
            continue
        for j in range(len(lines2)):
            if lines1[i] == lines2[j]:
                diff = False
        if diff:
            print(f1 + ',#' + str(i) + ': ' + lines1[i] + '\n' + f2 + ',#' + str(i) + ': ' + lines2[i] + '\n')


if len(sys.argv) == 3:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    compare(file1, file2)
    compare(file2, file1)
