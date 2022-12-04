import pathlib
import sys
import string


def parse(puzzle_input):
    """Parse input."""
    rounds = list(puzzle_input.split('\n'))
    return rounds

def get_letter_points(letter):
    """Get points associated to a letter."""
    letter_points = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    return letter_points.index(letter) + 1

def part1(input_bags):
    """Solve part 1."""
    res = 0
    for bag in input_bags :
        half_len = len(bag) // 2
        for letter in bag[:half_len] :
            if letter in bag[half_len:] :
                res += get_letter_points(letter)
                break
    return res


def part2(input_bags):
    """Solve part 2."""
    res = 0
    elf_groups = [input_bags[i:i + 3] for i in range(0, len(input_bags), 3)]
    for elf_group in elf_groups :
        for letter in elf_group[0]:
            if letter in elf_group[1] and letter in elf_group[2]:
                res += get_letter_points(letter)
                break
    return res


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        bags = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(bags)}')
        print(f'Part 2 : {part2(bags)}')
