import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    rounds = [line.split(',') for line in puzzle_input.split('\n')]
    return rounds

def part1(elf_assignments):
    """Solve part 1."""
    overlaps = 0
    for pair_elf_assignment in elf_assignments :
        min1_text, max1_text = pair_elf_assignment[0].split('-')
        min2_text, max2_text = pair_elf_assignment[1].split('-')
        min1,min2,max1,max2 = map(int, [min1_text, min2_text, max1_text, max2_text])
        if (min1 >= min2 and max1 <= max2) or (min2 >= min1 and max2 <= max1):
            overlaps += 1
    return overlaps


def part2(elf_assignments):
    """Solve part 2."""
    overlaps = 0
    for pair_elf_assignment in elf_assignments :
        min1_text, max1_text = pair_elf_assignment[0].split('-')
        min2_text, max2_text = pair_elf_assignment[1].split('-')
        min1,min2,max1,max2 = map(int, [min1_text, min2_text, max1_text, max2_text])
        for i in range(min1, max1 + 1):
            if i in range(min2, max2 + 1):
                overlaps += 1
                break
    return overlaps


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        assignments = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(assignments)}')
        print(f'Part 2 : {part2(assignments)}')
