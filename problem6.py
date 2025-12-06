from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    read_file_lines_raw,
    transpose_matrix,
    pad_matrix,
    process_divided_input,
    flatten
)

# too low 16326682677
# too low 5977758470893
def part1(filelines):
    processed_input1 = [s.split() for s in filelines]
    final_processed_input = []
    for i, l in enumerate(processed_input1):
        if i == len(processed_input1)-1:
            final_processed_input.append(l)
        else:
            # print(num)
            # if num == '*' or num == '+':
            # print(l)
            final_processed_input.append([int(num) for num in l])

    equation_results = []
    
    for eq in zip(*final_processed_input):
        # print(eq)
        if eq[-1] == '+':
            equation_results.append(sum(eq[:-1]))
        elif eq[-1] == '*':
            prod = 1
            for num in eq[:-1]:
                prod *= num
            equation_results.append(prod)
    
    # print(equation_results)
    print(sum(equation_results))

def part2_process_numbers(nums):
    # something with power of ten and modulus 10 power checks for summation stuff

    # mod ten, join the result, then integer divide by ten
    # loop it, then should get it
    ten_pow = 1
    print(nums)
    return [1,1,1]

# too low 9630000825309
def part2(filelines):

    results = []
    to_compute = []
    for data in reversed(list(zip(*filelines))):
        # print(data)
        # continue
        # exit(0)
        if data[-1] == '*' or data[-1] == '+':
            # print(data)
            if not ''.join(data[:-1]).isspace(): # not only whitespace characters
                to_compute.append(int(''.join(data[:-1])))
            # compute solution and add to result
            # and clear the computation list
            # print(to_compute)
            # exit(0)
            if data[-1] == '*':
                result = 1
                for num in to_compute:
                    result *= num
                results.append(result)
            elif data[-1] == '+':
                results.append(sum(to_compute))
            to_compute.clear()
        else:
            # add the integer to be computed later
            # print(''.join(data[:-1]))
            # print(data)
            if not ''.join(data[:-1]).isspace(): # not only whitespace characters
                # print(data)
                # exit(0)
                to_compute.append(int(''.join(data[:-1])))

        # print(data)
    # print(results)
    print(sum(results))

            

def main():
    # file_lines = read_file_lines_raw('input6_test.txt')
    file_lines = read_file_lines_raw('input6.txt')
    # print(file_lines)
    part2(file_lines)
    


if __name__ == '__main__':
    main()