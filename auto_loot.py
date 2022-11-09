#ROBERT PANERIO
#PROJECT 4; AUTO - LOOT
#DR. GRANT WILLIAMS

import sys
import time
from functools import lru_cache

start_time = time.time_ns()

@lru_cache()
def main():

    #manage the input for the stdin, store the input a dictionary
    item_dic = {}
    item_matrix = [[], []]
    count_line = -1
    weight_limit = 0

    #read all inputs from standard in
    for line in sys.stdin:

        #saves the weight limit
        if count_line == -1:
            weight_limit = int(line)

        #splits the input and save it to a dictionary
        #save the weight and values on arrays respectively
        else:
            line_array = line.split(";")
            item_dic[count_line] = line_array
            item_matrix[0].append(int(line_array[1]))
            item_matrix[1].append(int(line_array[2]))
        count_line += 1

    #adds the carriage return and line feed on the last line input
    item_dic[count_line-1][2] = item_dic[count_line-1][2] + "\r\n"

    #creates a 2D array
    matrix = [[0 for _ in range(weight_limit + 1)] for _ in range(len(item_matrix[1]) + 1)]

    #bottom up approach
    for rows in range(len(item_matrix[1]) + 1):
        for cols in range(weight_limit + 1):
            if rows == 0 or cols == 0:
                matrix[rows][cols] = 0
            elif item_matrix[0][rows-1] > cols:
                matrix[rows][cols] = matrix[rows - 1][cols]
            else:
                max_value = max(item_matrix[1][rows-1] + matrix[rows-1][cols-item_matrix[0][rows-1]], matrix[rows-1][cols])
                matrix[rows][cols] = max_value

    final_value = matrix[len(item_matrix[1])][weight_limit]

    #determines if the value is included in the bag
    #stores the index of the values
    item_index = []
    col_pointer = weight_limit
    for rows in range(len(item_matrix[1]), 0, -1):
        if matrix[rows][col_pointer] != matrix[rows-1][col_pointer]:
            item_index.append(rows-1)
            col_pointer = col_pointer - item_matrix[0][rows-1]

    #with the given index find the items in the dictionary
    final_weight = 0
    for index in range(len(item_index)-1, -1, -1):
        if item_dic.__contains__(item_index[index]):
            final_weight += int(item_dic[item_index[index]][1])
            print(f"{item_dic[item_index[index]][0]}, {item_dic[item_index[index]][1]}, {item_dic[item_index[index]][2]}", end="")

    print(f"final weight: {final_weight}\r")
    print(f"final value: {final_value}\r")


if __name__ == "__main__":
    main()
    time_taken_in_microseconds = (time.time_ns() - start_time) / 1000.0
    print("time taken in microseconds:", time_taken_in_microseconds)
