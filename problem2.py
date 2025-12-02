from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    transpose_matrix,
    singleline_split
)

def part1(str_ranges, digits_per_entry):
    print(str_ranges)
    print(digits_per_entry)

    # exit(0)

    overall_invalid_ids = []
    for ind, dig in enumerate(digits_per_entry):
        # only check a range if one of the elements in the digits_per_entry is even
        # need even number of digits for the double pattern to occur
        if dig[0]%2 == 0 or dig[1]%2 == 0:
            # generate invalid ids
            invalid_ids = []
            for i in range(dig[0]//2, (dig[1]//2)+1):
                for j in range(int(10**i)): #only check up until 10 to power of the exponent. Eg. in range 1-99 inclusive, or 1-999 inclusive
                    invalid_ids.append(''.join([str(j), str(j)]))

            for id in invalid_ids:
                if int(str_ranges[ind][0]) <= int(id) <= int(str_ranges[ind][1]):
                    overall_invalid_ids.append(int(id))
    print(overall_invalid_ids)
    print(sum(overall_invalid_ids))


def main():
    # file_lines = read_file_lines('input1_test.txt')
    # file_lines = read_file_lines('input2_test.txt')
    # split_output = singleline_split('input2_test.txt', ',')
    split_output = singleline_split('input2.txt', ',')
    print(split_output)
    # print(file_lines)

    str_ranges = [s.split('-') for s in split_output]
    # print(str_ranges)

    # get the number of digits per entry using stringlength
    digits_per_entry = [[len(s[0]), len(s[1])] for s in str_ranges]
    # print(digits_per_entry)

    part1(str_ranges, digits_per_entry)


if __name__ == '__main__':
    main()