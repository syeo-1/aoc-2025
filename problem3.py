from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    transpose_matrix
)

def part1(file_lines):
    processed_input1 = [list(s) for s in file_lines]
    # print(processed_input1)
    processed_input = []
    for l in processed_input1:
        processed_input.append([int(num) for num in l])
    # print(processed_input)

    joltages = []

    for row in processed_input:
        # find the largest value furthest left that has at least one element to its right
        max_left_index = row.index(max(row[:-1]))
        max_right_index = row.index(max(row[max_left_index+1:]))

        # create the num
        max_num = int(''.join([str(row[max_left_index]), str(row[max_right_index])]))
        joltages.append(max_num)
        # print(max_num)
    
    print(sum(joltages))
    # print(joltages)

def get_max_index(ls, exclude, min_i, max_i):
    '''
    Docstring for get_max_index
    
    :param ls: list of numbers
    :param exclude: return value must not be in this set
    :param min_i: minimum index to start search from
    :param max_i: maximum index to end search

    return the index of the maximum value not found in the exclude set within the range of min_i and max_i
    within the given list ls
    '''
    max_index = min_i
    max_num = -1

    for i in range(min_i, max_i):
        if ls[i] > max_num and i not in exclude: # strictly greater than, so index setting will be as low as possible
            max_num = ls[i]
            max_index = i
    return max_index


def part2(file_lines):
    processed_input1 = [list(s) for s in file_lines]
    processed_input = []
    for l in processed_input1:
        processed_input.append([int(num) for num in l])
    
    joltages = []

    for row in processed_input:
        exclusion_set = set()

        # make sure not to repeat an index
        max_left_index = row.index(max(row[:-11]))
        exclusion_set.add(max_left_index)

        digit_index_1 = get_max_index(row, exclusion_set, max_left_index+1, len(row)-10)
        exclusion_set.add(digit_index_1)

        digit_index_2 = get_max_index(row, exclusion_set, digit_index_1+1, len(row)-9)
        exclusion_set.add(digit_index_2)

        digit_index_3 = get_max_index(row, exclusion_set, digit_index_2+1, len(row)-8)
        exclusion_set.add(digit_index_3)

        digit_index_4 = get_max_index(row, exclusion_set, digit_index_3+1, len(row)-7)
        exclusion_set.add(digit_index_4)

        digit_index_5 = get_max_index(row, exclusion_set, digit_index_4+1, len(row)-6)
        exclusion_set.add(digit_index_5)
        digit_index_6 = get_max_index(row, exclusion_set, digit_index_5+1, len(row)-5)
        exclusion_set.add(digit_index_6)
        digit_index_7 = get_max_index(row, exclusion_set, digit_index_6+1, len(row)-4)
        exclusion_set.add(digit_index_7)
        digit_index_8 = get_max_index(row, exclusion_set, digit_index_7+1, len(row)-3)
        exclusion_set.add(digit_index_8)
        digit_index_9 = get_max_index(row, exclusion_set, digit_index_8+1, len(row)-2)
        exclusion_set.add(digit_index_9)
        digit_index_10 = get_max_index(row, exclusion_set, digit_index_9+1, len(row)-1)
        exclusion_set.add(digit_index_10)
        digit_index_11 = get_max_index(row, exclusion_set, digit_index_10+1, len(row))
        exclusion_set.add(digit_index_11)

        max_num = int(''.join([
            str(row[max_left_index]),
            str(row[digit_index_1]),
            str(row[digit_index_2]),
            str(row[digit_index_3]),
            str(row[digit_index_4]),
            str(row[digit_index_5]),
            str(row[digit_index_6]),
            str(row[digit_index_7]),
            str(row[digit_index_8]),
            str(row[digit_index_9]),
            str(row[digit_index_10]),
            str(row[digit_index_11])
        ]))

        joltages.append(max_num)
    
    print(sum(joltages))



def main():
    # file_lines = read_file_lines('input1_test.txt')
    # file_lines = read_file_lines('input3_test.txt')
    file_lines = read_file_lines('input3.txt')
    part2(file_lines)


if __name__ == '__main__':
    main()