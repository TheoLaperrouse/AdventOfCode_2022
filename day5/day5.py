import pathlib
import sys
import re
import copy


def first_state(input_stacks):
    """Get an array of the beginning state according to input"""
    state = []
    stacks_lines = input_stacks.split('\n')[:-1][::-1]
    state = [[stacks_lines[0][i:i + 3][1]]
             for i in range(0, len(stacks_lines[0]), 4)]
    for stack in stacks_lines[1:]:
        columns = [stack[i:i + 3][1]
                   for i in range(0, len(stack), 4)]
        for index, column in enumerate(columns):
            if column != ' ':
                state[index] += column
    return state


def parse(puzzle_input):
    """Parse input."""
    input_stacks, moves = list(puzzle_input.split('\n\n'))
    return [first_state(input_stacks), moves.split('\n')]


def part1(parsed_input):
    """Solve part 1."""
    state, moves = copy.deepcopy(parsed_input)
    state = state[:]
    for move in moves:
        if move != '':
            number_moves, begin, final = map(int, re.findall(r'\d+', move))
            state[final-1] += state[begin-1][-number_moves:][::-1]
            state[begin-1] = state[begin-1][:-number_moves]
    return ''.join([column[-1] for column in state])


def part2(parsed_input):
    """Solve part 2."""
    state, moves = parsed_input
    for move in moves:
        if move != '':
            number_moves, begin, final = map(int, re.findall(r'\d+', move))
            state[final-1] += state[begin-1][-number_moves:]
            state[begin-1] = state[begin-1][:-number_moves]
    return ''.join([column[-1] for column in state])


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8')
        stacks = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(stacks)}')
        print(f'Part 2 : {part2(stacks)}')
