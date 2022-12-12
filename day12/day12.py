import pathlib
import sys

def parse(text_input):
    """Parse input."""
    return text_input


def part1(input_climb):
    """Solve part 1."""
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
