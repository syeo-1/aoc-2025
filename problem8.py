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

def get_minimum_dist_points(distance_mapping):
    # get the two points with the minimum distance
    min_dist = -1
    min_points = []
    for point in distance_mapping:
        if min_dist == -1:
            min_dist_key = min(distance_mapping[point], key=distance_mapping[point].get)
            min_dist = distance_mapping[point][min_dist_key]
            min_points = [point, min_dist_key]
        else:
            min_dist_key = min(distance_mapping[point], key=distance_mapping[point].get)
            # print(min_dist_key)
            cur_min_dist = distance_mapping[point][min_dist_key]
            if cur_min_dist < min_dist:
                min_dist = cur_min_dist
                min_points = [point, min_dist_key]
    
    # print(min_dist)
    # print(min_points)
    return min_points

# 900 is too low
def part1(filelines):
    # seems like you want the num_points//2 closest connections!
    processed_lines = [[int(n) for n in s.split(',')] for s in filelines]
    processed_lines = [tuple(n) for n in processed_lines]

    # precompute distance between all points
    # to create a mapping
    distance_mapping = defaultdict(dict)
    # distance_mapping = defaultdict(list)

    for i in range(len(processed_lines)):
        cur_junction = processed_lines[i]
        for j in range(len(processed_lines)):
            other_junction = processed_lines[j]
            if i == j:
                continue
            else:
                distance_mapping[cur_junction][other_junction] = dist(cur_junction, other_junction)

    circuits = [] # list of sets for the circuits
    # allowable_connections = len(distance_mapping)//2 # number of connections allowed
    allowable_connections = 1000 # number of connections allowed
    connection_count = 0

    ind = 0

    while connection_count < allowable_connections:
        cur_min_points = get_minimum_dist_points(distance_mapping)
        del distance_mapping[cur_min_points[0]][cur_min_points[1]] # remove the two way min distance connection that was just retrieved
        del distance_mapping[cur_min_points[1]][cur_min_points[0]]

        # print(cur_min_points, dist(cur_min_points[0], cur_min_points[1]))
        # exit(0)

        if len(circuits) == 0:
            circuits.append(set([cur_min_points[0], cur_min_points[1]]))
            connection_count += 1
        else:
            p1_set_index = -1
            p2_set_index = -1
            p1 = cur_min_points[0]
            p2 = cur_min_points[1]

            # get the circuit in which each junction is in if it exists
            for i, c in enumerate(circuits):
                if p1 in c:
                    p1_set_index = i
                    break
            for i, c in enumerate(circuits):
                if p2 in c:
                    p2_set_index = i
                    break

            if p1_set_index != -1 and p2_set_index != -1 and p1_set_index != p2_set_index: # union two different circuits
                # create a union of their sets
                # union_circuit_set = circuits[p1_set_index].union(circuits[p2_set_index])
                circuits[p1_set_index].update(circuits[p2_set_index])
                # remove the original sets
                # circuits.remove(circuits[p1_set_index]) # can't remove by index since will modify the list itself, so need to remove by the element/contents
                # print(circuits)
                # print(p2_set_index)
                # print(len(circuits))
                circuits.remove(circuits[p2_set_index])
                # # add the unioned circuit
                # circuits.append(union_circuit_set)
                connection_count += 1
            elif p2_set_index != -1 and p2_set_index != -1 and p1_set_index == p2_set_index:# if in the same set, still need to increase the connection_count
                connection_count += 1
            elif p1_set_index != -1 and p2_set_index == -1: # only p1 is in one of the circuits
                # add the elements to the p1 index set
                for p in cur_min_points:
                    circuits[p1_set_index].add(p)
                connection_count += 1
            elif p1_set_index == -1 and p2_set_index != -1: # only p2 is in one of the circuits
                for p in cur_min_points:
                    circuits[p2_set_index].add(p)
                connection_count += 1
            elif p1_set_index == -1 and p2_set_index == -1: # neither of them are in the circuits
                circuits.append(set([cur_min_points[0], cur_min_points[1]]))
                connection_count += 1
            else:
                connection_count += 1
                
        # print(circuits)
        # print('===')
        # if ind == 25:
        #     break
        # ind += 1

    
    circuit_lengths = [len(c) for c in circuits]
    circuit_lengths.sort(reverse=True)

    result = 1
    for circuit_length in circuit_lengths[:3]:
        result *= circuit_length

    # print(circuit_lengths)
    print(result)


def main():
    # file_lines = read_file_lines('input8_test.txt')
    file_lines = read_file_lines('input8.txt')
    part1(file_lines)
    


if __name__ == '__main__':
    main()