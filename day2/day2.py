import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    rounds = [line.split(' ') for line in puzzle_input.split('\n')]
    return rounds


def part1(input_pairs):
    """Solve part 1."""
    res = 0
    for pair in input_pairs:
        my_score = 'XYZ'.index(pair[1]) + 1
        opponent_score = 'ABC'.index(pair[0]) + 1
        res += my_score
        winning_conditions = [
            (pair[1] == 'X' and pair[0] == 'C'),
            (pair[1] == 'Y' and pair[0] == 'A'),
            (pair[1] == 'Z' and pair[0] == 'B')
        ]
        if my_score == opponent_score:
            res += 3
        if any(winning_conditions):
            res += 6
    return res


def part2(input_pairs):
    """Solve part 2."""
    res = 0
    for pair in input_pairs:
        res += 0 if pair[1] == 'X' else 3 if pair[1] == 'Y' else 6
        if pair[1] == 'X':
            res += 3 if pair[0] == 'A' else 1 if pair[0] == 'B' else 2
        if pair[1] == 'Y':
            res += 1 if pair[0] == 'A' else 2 if pair[0] == 'B' else 3
        if pair[1] == 'Z':
            res += 2 if pair[0] == 'A' else 3 if pair[0] == 'B' else 1
    return res


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text().strip()
        pairs = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(pairs)}')
        print(f'Part 2 : {part2(pairs)}')
