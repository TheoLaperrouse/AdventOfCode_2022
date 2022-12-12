import pathlib
import sys
import re
import copy


def operation(worry_level, op):
    if '+' in op:
        to_add = op.split('+ ')[1]
        worry_level += int(to_add) if 'old' not in to_add else worry_level
    if '*' in op:
        to_mul = op.split('* ')[1]
        worry_level *= int(to_mul) if 'old' not in to_mul else worry_level
    print(worry_level / 3)
    return int(worry_level / 3)


def parse(text_input):
    """Parse input."""
    monkeys = [monkey.split('\n') for monkey in text_input.split('\n\n')]
    monkey_objects = [{
        "inspected": 0,
        "list_object": list(map(int, re.findall(r"\d+", monkey[1]))),
        "operation": monkey[2].split('=')[1],
        "divisor": int(re.search(r"\d+", monkey[3]).group(0)),
        "true": int(monkey[4][-1]),
        "false": int(monkey[5][-1]),
    } for monkey in monkeys]
    return monkey_objects


def part1(monkey_inputs):
    """Solve part 1."""
    monkeys = copy.deepcopy(monkey_inputs)
    for _ in range(0, 20):
        for monkey in monkeys:
            print(monkey)
            for index, object in enumerate(monkey['list_object']):
                monkey['inspected'] += 1
                object = operation(
                    object, monkey['operation'])
                if object % monkey['divisor']:
                    monkeys[monkey['true']]['list_object'].append(object)
                else:
                    monkeys[monkey['false']]['list_object'].append(object)
                monkey['list_object'].pop(index)
    print(monkeys)
    return 0


def part2(cycle_inputs):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        parsed_text = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(parsed_text)}')
        print(f'Part 2 : {part2(parsed_text)}')
