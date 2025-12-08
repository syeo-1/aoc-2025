from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    read_file_lines_raw,
    transpose_matrix,
    pad_matrix,
    process_divided_input,
    flatten
)
from math import comb

def part1(filelines):
    processed_lines = [list(s) for s in filelines]
    # print(processed_lines)
    split_count = 0
    for i in range(1, len(processed_lines)):
        for j in range(len(processed_lines[0])):
            cur = processed_lines[i][j]
            prev = processed_lines[i-1][j]

            if cur == '.' and (prev == 'S' or prev == '|'):
                processed_lines[i][j] = '|'
            elif cur == '^' and prev == '|':
                processed_lines[i][j-1] = '|'
                processed_lines[i][j+1] = '|'
                split_count += 1
    # print(split_count)
    return processed_lines

def part2(filelines):
    # refer to this: https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2F2025-day-7-part-2-hint-v0-9lxea8kv9q5g1.gif%3Fwidth%3D625%26auto%3Dwebp%26s%3D1aff8c97090bb5f5fd84efc2cd1d5b67f085eae1
    # can populate the branches with numbers
    mapped_data = part1(filelines)
    for thing in mapped_data:
        print(''.join(thing))
    # print(mapped_data)


def main():
    file_lines = read_file_lines('input7_test.txt')
    # file_lines = read_file_lines('input7.txt')
    part2(file_lines)
    


if __name__ == '__main__':
    main()