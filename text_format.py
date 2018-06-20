import sys

with open(sys.argv[1]) as fp:
    lines = fp.read().split("\n")

for line in lines:
    first_num = line[1: line.find(',')]
    second_num = line[line.find(' ')+1 :line.rfind(']')]
    print(first_num, second_num)
