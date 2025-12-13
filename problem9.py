from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    read_file_lines_raw,
    transpose_matrix,
    pad_matrix,
    process_divided_input,
    flatten
)
from math import dist
from collections import defaultdict

def calculate_rectangle_area(p1,p2):
    x_len = int(abs(p1[0]-p2[0]))+1
    y_len = int(abs(p1[1]-p2[1]))+1

    return x_len*y_len

def part1(filelines):
    processed_input = [[int(s.split(',')[0]), int(s.split(',')[1])] for s in filelines]
    print(processed_input)

    max_area = 0
    for i, p1 in enumerate(processed_input):
        for j, p2 in enumerate(processed_input):
            cur_area = calculate_rectangle_area(p1, p2)
            max_area = max(cur_area, max_area)

        
    print(max_area)

    # print(filelines)


def main():
    # file_lines = read_file_lines('input9_test.txt')
    file_lines = read_file_lines('input9.txt')
    part1(file_lines)
    


if __name__ == '__main__':
    main()