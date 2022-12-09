import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(moves_inputs):
    """Solve part 1."""
    return moves_inputs


def part2(moves_inputs):
    """Solve part 2."""
    return moves_inputs


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        move_inputs = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(move_inputs)}')
        print(f'Part 2 : {part2(move_inputs)}')
