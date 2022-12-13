import pathlib
import sys
import string
import copy 

def is_climbable(first, second):
    '''Return true if is second is climbable from first'''
    alphabet = string.ascii_lowercase
    return second == 'E' or (second != '.' and alphabet.index(first) - alphabet.index(second) >= -2)

def possible_dir(coord, map, value_coord):
    '''Return a possible directions according a map and coord'''
    len_line = len(map)
    len_column = len(map[0])
    directions = []
    if  len_line > coord[0] + 1:
        var_move = map[coord[0] + 1][coord[1]]
        if is_climbable(value_coord, var_move):
            directions.append([coord[0] + 1,coord[1]])
    if len_column > coord[1] + 1:
        var_move = map[coord[0]][coord[1]  + 1]
        if is_climbable(value_coord, var_move):
            directions.append([coord[0],coord[1] + 1])
    if coord[0] - 1 > 0:
        var_move = map[coord[0] - 1][coord[1]]
        if is_climbable(value_coord, var_move):
            directions.append([coord[0]  - 1, coord[1]])
    if coord[1] - 1 > 0 :
        var_move = map[coord[0]][coord[1] - 1]
        if is_climbable(value_coord, var_move):
            directions.append([coord[0],coord[1] - 1])
    return directions

def map_recursiv(end, coord, map, res, value_coord):
    '''Recursive function to recurse on map'''
    dirs = possible_dir(coord, map, value_coord)
    print(res + 1)
    if not dirs:
        return 1
    for dir in dirs :
        cloned_map = copy.deepcopy(map)
        val = cloned_map[coord[0]][coord[1]]
        cloned_map[coord[0]][coord[1]] = '.'
        map_recursiv(end, dir,cloned_map, res + 1, val)
    if coord == end:
        return res + 1
    else:
        return 1

def parse(text_input):
    """Parse input."""
    map_site = [list(line.strip()) for line in text_input.split('\n')]
    start = []
    end = []
    for index_line, line in enumerate(map_site): 
        for index_column,point in enumerate(line):
            if point == 'S':
                map_site[index_line][index_column] = 'z'
                start = [index_line,index_column]
            if point == 'E':
                end = [index_line, index_column]
    return [map_site, start, end]


def part1(input_climb):
    """Solve part 1."""
    map, start, end = input_climb
    print(map_recursiv(end,start,map,0,'z'))
    return input_climb


def part2(input_climb):
    """Solve part 2."""
    return input_climb



if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        parsed_map = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(parsed_map)}')
        print(f'Part 2 : {part2(parsed_map)}')
