from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    read_file_lines_raw,
    transpose_matrix,
    pad_matrix,
    process_divided_input,
    flatten
)

def part1(filelines):
    processed_input1 = [s.split() for s in filelines]
    final_processed_input = []
    for i, l in enumerate(processed_input1):
        if i == len(processed_input1)-1:
            final_processed_input.append(l)
        else:
            final_processed_input.append([int(num) for num in l])

    equation_results = []
    
    for eq in zip(*final_processed_input):
        if eq[-1] == '+':
            equation_results.append(sum(eq[:-1]))
        elif eq[-1] == '*':
            prod = 1
            for num in eq[:-1]:
                prod *= num
            equation_results.append(prod)
    
    print(sum(equation_results))


def part2(filelines):

    results = []
    to_compute = []
    for data in reversed(list(zip(*filelines))):
        if data[-1] == '*' or data[-1] == '+':
            if not ''.join(data[:-1]).isspace(): # not only whitespace characters
                to_compute.append(int(''.join(data[:-1])))
            # compute solution and add to result
            # and clear the computation list
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
            if not ''.join(data[:-1]).isspace(): # not only whitespace characters
                to_compute.append(int(''.join(data[:-1])))

    print(sum(results))

            

def main():
    # file_lines = read_file_lines_raw('input6_test.txt')
    file_lines = read_file_lines_raw('input6.txt')
    part2(file_lines)
    


if __name__ == '__main__':
    main()