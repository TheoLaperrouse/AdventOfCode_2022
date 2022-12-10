import pathlib
import sys

def parse(text_input):
    """Parse input."""
    return list(text_input.split('\n'))


def part1(cycle_inputs):
    """Solve part 1."""
    res = 1
    cycles = [0]
    somme = 0
    for cycle in cycle_inputs:
        if cycle == 'noop':
            cycles.append(res)
        elif 'addx' in cycle :
            val = int(cycle.split()[1])
            cycles.append(res)
            res += val
            cycles.append(res)
    important_cycles = [20, 60, 100, 140, 180, 220]
    for i in important_cycles :
        somme += cycles[i - 1] * i
    return somme


def part2(cycle_inputs):
    """Solve part 2."""
    res = 1
    cycles = [0]
    for cycle in cycle_inputs:
        if cycle == 'noop':
            cycles.append(res)
        elif 'addx' in cycle :
            val = int(cycle.split()[1])
            cycles.append(res)
            res += val
            cycles.append(res)
    string = ''
    for index, i in enumerate(cycles):
        actual_index = index % 40
        print(actual_index)
        if i in [actual_index - 1, actual_index, actual_index + 1]:
            cycles[index] = '#'
        else :
            cycles[index] = ' '
    for index, i in enumerate(cycles):
        if index % 40 == 0:
            string += '\n'
        string += i
    return string


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        move_inputs = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(move_inputs)}')
        print(f'Part 2 : {part2(move_inputs)}')
