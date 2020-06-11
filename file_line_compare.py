import sys


def compareFiles(p1, p2):
    with open(p1) as f1, open(p2) as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                print(p1 + ': ' + line1 + p2 + ': ' + line2)


if len(sys.argv) == 3:
    compareFiles(sys.argv[1], sys.argv[2])
