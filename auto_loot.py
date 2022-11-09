import sys
import time
import functools

start_time = time.time_ns()

def knap_sack():
    return

def main():

    #manage the input for the stdin, store the input a dictionary
    item_dic = {}
    item_weights = []
    item_values = []
    count_line = -1
    weight_limit = 0
    for line in sys.stdin:
        if count_line == -1:
            weight_limit = int(line)
        else:
            line_array = line.split(";")
            item_dic[str(count_line)] = line_array
            item_weights.append(int(line_array[1]))
            item_values.append(int(line_array[2][:-2]))
        count_line += 1

    print(weight_limit)
    print(item_weights)
    print(item_values)
    for key, values in item_dic.items():
        print(key, values)

    time_taken_in_microseconds = (time.time_ns() - start_time) / 1000.0
    print("total time in microseconds: ", time_taken_in_microseconds)


if __name__ == "__main__":
    main()
