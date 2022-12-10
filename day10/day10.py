import pathlib
import sys


def move_dir(position):  # , move):
    # match move:
    #     case 'R':
    #         position[0] += 1
    #     case 'L':
    #         position[0] -= 1
    #     case 'U':
    #         position[1] += 1
    #     case 'D':
    #         position[1] -= 1
    return position


def parse(text_input):
    """Parse input."""
    return [[line.split()[0], int(line.split()[1])] for line in text_input.split('\n')]


def part1(moves_inputs):
    """Solve part 1."""
    visited_positions = []
    last_position_H = [0, 0]
    position_H = [0, 0]
    position_T = [-1, 0]
    last_dist = 0
    for move in moves_inputs:
        for _ in range(0, move[1]):
            position_H = move_dir(position_H, move[0])
            dist = abs(position_H[0] - position_T[0]) + \
                abs(position_H[1] - position_T[1])
            if last_dist > dist:
                pass
            # Diagonale
            elif abs(position_H[0] - position_T[0]) + abs(position_H[1] - position_T[1]) == 2\
                    and abs(position_H[0] - position_T[0]) > 0 and abs(position_H[1] - position_T[1]) > 0:
                position_T = last_position_H[:]
                visited_positions.append(position_T)
            # H revient vers T (T bouge pas)

            # Comportement normal
            else:
                position_T = move_dir(position_T, move[0])
                visited_positions.append(position_T[:])
            last_position_H = position_H[:]
            print(position_H, position_T)
            last_dist = dist
    known_positions = []
    for position in visited_positions:
        if position not in known_positions:
            known_positions.append(position)
    print(known_positions)
    return len(known_positions)


def part2(moves_inputs):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        move_inputs = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(move_inputs)}')
        print(f'Part 2 : {part2(move_inputs)}')
