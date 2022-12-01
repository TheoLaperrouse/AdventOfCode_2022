import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    groups = [line.split('\n') for line in puzzle_input.split('\n\n')]
    sum_group = [sum(map(int, group)) for group in groups]
    return sum_group


def part1(input_numbers):
    """Solve part 1."""
    return max(input_numbers)


def part2(input_numbers):
    """Solve part 2."""
    input_numbers.sort()
    input_numbers.reverse()
    return sum(input_numbers[0:3])


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        input_text = pathlib.Path(path).read_text().strip()

        numbers = parse(input_text)
        print(part1(numbers))
