with open("/Users/albertzhang/desktop/text_files/txt/bad_intervals_arr.txt") as fp:
    lines = fp.read().split("\n")

total_count = 0
bad_interval_count = 0
for line in lines:
    if total_count == 0:
        first_num = 0
        second_num = float(line[1: line.find(',')])
        previous = float(line[line.find(',')+2: line.find(']')])
    else:
        first_num = previous
        second_num = float(line[1: line.find(',')])
        previous = float(line[line.find(',')+2: line.find(']')])
    diff = second_num - first_num
    if diff >= 0.5 and total_count < len(lines):
        print([first_num, second_num])
        bad_interval_count += 1
    total_count += 1
