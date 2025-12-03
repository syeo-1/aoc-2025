from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    transpose_matrix,
    singleline_split,
    generate_factors
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

def part2(str_ranges, digits_per_entry):

    # for all factors of number. eg if length is 8, theres 8, 2, 4
    # for 10 there 10,5,2
    # for 16 theres 16,2,8,4
    # for 5 theres 5, eg 11111. 
    # factors will give the pattern for invalid entries

    overall_invalid_ids = []
    for ind, dig in enumerate(digits_per_entry):

        dig_0_factors = generate_factors(dig[0])
        dig_1_factors = generate_factors(dig[1])
        
        # remove does so in place, so doesn't return a value (keep that in mind!)
        dig_0_factors.remove(1)
        dig_1_factors.remove(1)
        if len(dig_0_factors) > 0: # account for when the number in the range is a single digit (eg. 4-17)
            max_factor_dig0 = max(dig_0_factors) # get the largest factor for generating invalid ids
        if len(dig_1_factors) > 0:
            max_factor_dig1 = max(dig_1_factors)

        # generate invalid ids
        invalid_ids = set()
        # dig0
        for factor in dig_0_factors:
            expo = max_factor_dig0//factor
            for j in range(1,int(10**(expo))):
                invalid_ids.add(''.join([str(j)]*factor))

        # dig1
        for factor in dig_1_factors:
            expo = max_factor_dig1//factor
            for j in range(1,int(10**expo)):
                invalid_ids.add(''.join([str(j)]*factor))

        # check if invalid ids in the given range and
        # append to overall result list
        for id in invalid_ids:
            if int(str_ranges[ind][0]) <= int(id) <= int(str_ranges[ind][1]):
                overall_invalid_ids.append(int(id))
        
    print(sum(overall_invalid_ids))


def main():
    split_output = singleline_split('input2.txt', ',')

    str_ranges = [s.split('-') for s in split_output]

    # get the number of digits per entry using stringlength
    digits_per_entry = [[len(s[0]), len(s[1])] for s in str_ranges]

    part2(str_ranges, digits_per_entry)


if __name__ == '__main__':
    main()