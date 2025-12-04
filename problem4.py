from aoc_helper import (
    split_file_line_contents_whitespace,
    read_file_lines,
    transpose_matrix,
    pad_matrix
)

def part1(M):
    # print(M)
    roll_counter = 0
    for i in range(1, len(M)-1):
        for j in range(1, len(M[0])-1):
            if M[i][j] == '@':
                surround_counter = 0
                if M[i-1][j-1] == '@':
                    surround_counter += 1
                if M[i-1][j] == '@':
                    surround_counter += 1
                if M[i-1][j+1] == '@':
                    surround_counter += 1
                if M[i][j-1] == '@':
                    surround_counter += 1
                if M[i][j+1] == '@':
                    surround_counter += 1
                if M[i+1][j-1] == '@':
                    surround_counter += 1
                if M[i+1][j] == '@':
                    surround_counter += 1
                if M[i+1][j+1] == '@':
                    surround_counter += 1

                if surround_counter < 4:
                    roll_counter += 1

    print(roll_counter)


def roll_remover(M):
    '''
    given the map, return the new map where the rolls have been removed and the number of rolls removed
    
    :param M: Description
    '''

    coords = [] # coordinates where rolls were removed
    roll_counter = 0
    for i in range(1, len(M)-1):
        for j in range(1, len(M[0])-1):
            if M[i][j] == '@':
                surround_counter = 0
                if M[i-1][j-1] == '@':
                    surround_counter += 1
                if M[i-1][j] == '@':
                    surround_counter += 1
                if M[i-1][j+1] == '@':
                    surround_counter += 1
                if M[i][j-1] == '@':
                    surround_counter += 1
                if M[i][j+1] == '@':
                    surround_counter += 1
                if M[i+1][j-1] == '@':
                    surround_counter += 1
                if M[i+1][j] == '@':
                    surround_counter += 1
                if M[i+1][j+1] == '@':
                    surround_counter += 1

                if surround_counter < 4:
                    roll_counter += 1
                    # M[i][j] = '.' # don't modify in place, because it affects the surrounding and thus the end calculation
                    coords.append([i, j])

    print(f'removed {roll_counter} rolls of paper')
    return {
        'roll_counter': roll_counter,
        'coords': coords
    }

def modify_map(M, coords):
    '''
    take the coordinates and modifies M in place
    
    :param M: 2d matrix representing the map
    :param coords: list of coordinates to modify the map
    '''
    for coord in coords:
        M[coord[0]][coord[1]] = '.'


def part2(M):

    overall_roll_counter = 0

    while True:
        data = roll_remover(M)
        modify_map(M, data['coords'])
        overall_roll_counter += data['roll_counter']

        if data['roll_counter'] == 0:
            break
    
    print(overall_roll_counter)

def main():
    # file_lines = read_file_lines('input4_test.txt')
    file_lines = read_file_lines('input4.txt')
    split_lines = [list(s) for s in file_lines]
    new_m = pad_matrix(split_lines, '.')
    part2(new_m)


if __name__ == '__main__':
    main()