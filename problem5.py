from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    transpose_matrix,
    pad_matrix,
    process_divided_input,
    flatten
)

def part1(id_ranges, ids):

    processed_id_ranges = [[int(r.split('-')[0]), int(r.split('-')[1])] for r in id_ranges]
    processed_ids = [int(num) for num in ids]
    # print(processed_id_ranges)
    # print(processed_ids)

    fresh_count = 0

    for id in processed_ids:
        for id_range in processed_id_ranges:
            if id_range[0] <= id <= id_range[1]:
                print(id_range)
                print(f'fresh: {id}')
                fresh_count += 1
                break
    
    print(fresh_count)

def merge_intervals(l):
    # merge intervals
    # ===
    merged_intervals = []
    for interval in l:
        if len(merged_intervals) == 0:
            merged_intervals.append(interval)
        else:
            # check for overlap. if there is no overlap, just add the interval to the merged intervals
            # otherwise, if there is overlap, modify the last interval in the merged intervals list to
            # be the bigger end value between the last element of the merged intervals and the interval
            # currently being viewed

            # check for overlap
            if merged_intervals[-1][0] <= interval[0] <= merged_intervals[-1][1]:
                # merge the interval
                merged_intervals[-1][1] = max(interval[1], merged_intervals[-1][1])
            else:
                # add a non overlapped interval
                merged_intervals.append(interval)
    # end merged intervals
    # ===
    return merged_intervals

# 342156542130419 is too low
def part2(id_ranges, ids):
    processed_id_ranges = [[int(r.split('-')[0]), int(r.split('-')[1])] for r in id_ranges]
    print(processed_id_ranges[-1])
    processed_ids = [int(num) for num in ids]
    # print(processed_id_ranges)
    # print(processed_ids)

    fresh_count = 0
    range_set = set()

    for id in processed_ids:
        for id_range in processed_id_ranges:
            if id_range[0] <= id <= id_range[1]:
                # an id range may likely be considered twice since the fresh ingredient can be counted in two different ranges
                # so I'd need to count both ranges
                range_set.add(tuple(id_range))
                # print(id_range)
                # print(f'fresh: {id}')
                fresh_count += 1
                # break
    
    # have to reduce memory usage. Refer to merge intervals problem on leetcode
    # print(range_set)
    range_list = list(list(r) for r in range_set)
    # sort by first element of the tuples
    range_list.sort(key=lambda x: x[0])
    # print(len(range_list))


    # print(len(merged_intervals))
    # print(merged_intervals)
    merged_intervals = merge_intervals(range_list)
    # merged_intervals = merge_intervals(merged_intervals0)

    # now that all ranges have no overlap, just count the number of items within each range to get the fresh count

    fresh_count = 0
    for interval in merged_intervals:
        fresh_count += (interval[1]-interval[0]) + 1 # plus one to include the number that starts the range itself
    
    print(merged_intervals)
    print(fresh_count)


# def working_answer()


def main():
    file_lines = process_divided_input('input5_test2.txt')
    # file_lines = process_divided_input('input5.txt')
    part2(file_lines[0], file_lines[1])
    


if __name__ == '__main__':
    main()