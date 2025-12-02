from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    transpose_matrix
)

# if it goes from 0 to positive or 0 to negative, that doesn't count as a click
# so a click only counts if it goes from strictly positive to negative or vice versa

# jk, its strictly within 1 to 99 to less than 0 or greater than 100
def part1(file_lines):
    cur_position = 50

    zero_counter = 0

    processed_input = [[s[0], int(s[1:])] for s in file_lines]

    for instruction in processed_input:
        if instruction[0] == 'L':

            original = cur_position
            if instruction[1] >= 100:
                zero_counter += instruction[1] // 100
                cur_position -= instruction[1] // 100
            else:
                cur_position -= instruction[1]

            if cur_position < 0 and original > 0:
                zero_counter += 1
                print('left cross zero')

            cur_position %= 100
            print(cur_position)
            if cur_position == 0:
                zero_counter += 1
                print('left equal zero')
                print(cur_position)
                # cur_position %= 100
        elif instruction[0] == 'R':


            original = cur_position
            if instruction[1] >= 100:
                zero_counter += instruction[1] // 100
                cur_position += instruction[1] // 100
            else:
                cur_position += instruction[1]


            if cur_position > 100 and original < 100:
                zero_counter += 1
                print('right cross zero')

            cur_position %= 100
            print(cur_position)
            if cur_position == 0:
                zero_counter += 1
                print('right equal zero')
                print(cur_position)
    print(zero_counter)

# answer is higher than 5488
# also not 5829...
# not 6212

# is it 5894??
def part2_clean(file_lines):
    cur_position = 50

    zero_counter = 0

    processed_input = [int(s[1:]) if s[0] == 'R' else -int(s[1:]) for s in file_lines]
    # print(processed_input)

    for i in processed_input:

        prev = cur_position

        zero_counter += int(abs(i) / 100)
        # print(f'what: {i//100}')
        # print(f'what2; {i}')
        # actual_step = i%100
        if i > 0:
            cur_position += i%100
        elif i < 0:
            temp_i = -i
            temp_i %= 100
            cur_position -= temp_i
        # cur_position += actual_step

        # single wrap
        # to count situations where the number change is less than 100, but still causes a transition over the zero point to occur
        # print(f'prev {prev}')
        # print(f'cur {cur_position}')
        if 0 < prev < 100 and (cur_position < 0 or cur_position > 100):
            zero_counter += 1

        # now set the number to the proper value after counting the wrap around
        cur_position %= 100
        # print(f'cur: {cur_position}')

        if cur_position == 0:
            zero_counter += 1
        # print(f'zero_counter: {zero_counter}')
    print(zero_counter)

    



def main():
    # file_lines = read_file_lines('input1_test.txt')
    file_lines = read_file_lines('input1.txt')
    part2_clean(file_lines)
    # print(file_lines)


if __name__ == '__main__':
    main()