import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(input_code):
    """Solve part 1."""
    packet = ''
    for index, letter in enumerate(input_code, 1):
        if letter in packet:
            packet = packet[packet.index(letter) + 1:]
        packet += letter
        if len(packet) >= 4:
            return index
    return -1


def part2(input_code):
    """Solve part 2."""
    packet = ''
    for index, letter in enumerate(input_code, 1):
        if letter in packet:
            packet = packet[packet.index(letter) + 1:]
        packet += letter
        if len(packet) >= 14:
            return index
    return -1


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        code = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(code)}')
        print(f'Part 2 : {part2(code)}')
