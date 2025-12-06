from functools import reduce

def split_file_line_contents_whitespace(file_contents, datatype='str'):
    '''
    given the lines of the file, split each line into individual elements that compose the line.
    Splits by whitespace in the line

    at the same time, detect the appropriate data type that should be used for each element of the line

    returns a list of lists, where each individual sublist contains a split line's contents composed of the
    appropriate datatype

    by default, leaves contents as strings. Pass in 'int' to convert contents of each split line to integers
    '''

    result = []

    for line in file_contents:
        if datatype == 'int':
            result.append([int(num) for num in line.split()])
        elif datatype == 'str':
            result.append(line.split())

    return result

def read_file_lines_raw(filepath):
    '''
    read and split the contents of text input by newlines without getting rid of extra whitespace at the end of input lines
    
    :param filepath: path to the file
    '''
    result = []
    with open(filepath) as file:
        for line in file:
            result.append(line.rstrip('\n'))

    return result


def read_file_lines(filepath):
    '''
    read and split the contents of text input by newlines

    returns the contents of the file as a list of strings
    '''
    result = []
    with open(filepath) as file:
        for line in file:
            result.append(line.rstrip())

    return result

def transpose_matrix(m):
    '''
    takes a list of lists (ie. a matrix) and performs a transpose on it (rows become columns)
    and returns the transposed matrix as a new value
    '''
    return list(map(list, zip(*m)))


def flatten(l):
    '''
    flattens a nested list up to 10 levels
    refer to this post for more info: http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
    '''
    out = []
    for item in l:
        if isinstance(item, (list, tuple)):
            out.extend(flatten(item))
    else:
        out.append(item)
    return out


def singleline_split(filepath, split_char):
    '''
    takes a file and splits the single line input based on the given character
    '''
    with open(filepath) as file:
        output = file.readline()
        
    return output.split(split_char)
    
    # print()

def generate_factors(n):
    '''
    Docstring for generate_factors
    
    :param num: given a number, generate and return a set containing all of its factors (including 1)
    '''
    # Source - https://stackoverflow.com/a
    # Posted by agf, modified by community. See post 'Timeline' for change history
    # Retrieved 2025-12-02, License - CC BY-SA 4.0
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def pad_matrix(M, wall_char):
    '''
    sometimes it may be easier to pad the outside of a 2d array to work with edge cases.
    This function pads the outside of the 2d array with the given wall character and returns a new modified 2d array
    
    :param M: matrix to add padding to
    :param wall_char: use this character when adding padding to the matrix
    :param target_char: use this for any other needed operations
    '''

    result = []
    result.append([wall_char]*(len(M[0])+2))
    for row in M:
        result.append([wall_char]+row+[wall_char])
    result.append([wall_char]*(len(M[0])+2))

    return result

def process_divided_input(filename):
    '''
    processes the given filename in which there are two distinct input types separated by a double newline
    '''
    filelines = read_file_lines(filename)

    empty_string_index = filelines.index('')

    return [
        filelines[:empty_string_index],
        filelines[empty_string_index+1:]
    ]



def main():
    # file_lines = read_file_lines('input1.txt')
    # processed_file_lines = split_file_line_contents_whitespace(file_lines, 'int')
    # print(generate_factors(2))
    print(process_divided_input('input5_test.txt'))

if __name__ == '__main__':
    main()
    