import pathlib
import sys
import re
import copy
import math

def operation(worry_level, oper):
    """Apply the operation to the worry level"""
    if '+' in oper:
        to_add = oper.split('+ ')[1]
        worry_level += int(to_add) if 'old' not in to_add else worry_level
    if '*' in oper:
        to_mul = oper.split('* ')[1]
        worry_level *= int(to_mul) if 'old' not in to_mul else worry_level
    return int(worry_level / 3)

def operation2(worry_level, oper):
    """Apply the operation to the worry level"""
    if '+' in oper:
        to_add = oper.split('+ ')[1]
        worry_level += int(to_add) if 'old' not in to_add else worry_level
    if '*' in oper:
        to_mul = oper.split('* ')[1]
        worry_level *= int(to_mul) if 'old' not in to_mul else worry_level
    return int(worry_level)


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
            for  object_monkey in monkey['list_object']:
                monkey['inspected'] += 1
                object_monkey = operation(
                    object_monkey, monkey['operation'])
                if object_monkey % monkey['divisor'] == 0:
                    monkeys[monkey['true']]['list_object'].append(object_monkey)
                else:
                    monkeys[monkey['false']]['list_object'].append(object_monkey)
                monkey['list_object'] = monkey['list_object'][1:]
    monkeys.sort(key=lambda m: m['inspected'], reverse=True)
    return monkeys[0]['inspected'] * monkeys[1]['inspected']


def part2(monkey_inputs):
    """Solve part 2."""
    lcm = math.lcm(monkey['divisor'] for monkey in monkey_inputs)
    monkeys = copy.deepcopy(monkey_inputs)
    for _ in range(0, 10000):
        for monkey in monkeys:
            for  object_monkey in monkey['list_object']:
                monkey['inspected'] += 1
                object_monkey = operation2(object_monkey, monkey['operation']) % lcm
                if object_monkey % monkey['divisor'] == 0:
                    monkeys[monkey['true']]['list_object'].append(object_monkey)
                else:
                    monkeys[monkey['false']]['list_object'].append(object_monkey)
                monkey['list_object'] = monkey['list_object'][1:]
    monkeys.sort(key=lambda m: m['inspected'], reverse=True)
    return monkeys[0]['inspected'] * monkeys[1]['inspected']



if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        parsed_text = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(parsed_text)}')
        print(f'Part 2 : {part2(parsed_text)}')
