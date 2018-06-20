with open("/Users/albertzhang/desktop/text_files/txt/output_arrays.txt") as fp:
    lines = fp.read().split("\n")

total_count = 0
bad_interval_count = 0
differences = {}
# print("length: " + str(len(lines)))
for line in lines:
    if total_count == 0:
        first_num = 0
        second_num = float(line[1: line.find(',')])/1000
        previous = float(line[line.find(',')+2: line.find(']')])/1000
    elif total_count == len(lines) -1:
        first_num = second_num = float(line[1: line.find(',')])/1000
        second_num = float(line[line.find(',')+2: line.find(']')])/1000
    else:
        first_num = previous
        second_num = float(line[1: line.find(',')])/1000
        previous = float(line[line.find(',')+2: line.find(']')])/1000
    # print("first num " + str(count)+ ": "+ str(first_num))
    # print("second num " + str(count)+ ": "+ str(second_num))
    diff = second_num - first_num
    # print("difference " + str(count)+ ": "+ str(diff))
    # print("")
    if diff >= 0.5 and total_count < len(lines):
        print([first_num, second_num])
        differences[str(total_count) + "-" + str(total_count+1)] = diff
        bad_interval_count += 1
    total_count += 1

#differences were for intervals themselves, not between intervals
# print("differences", differences)
