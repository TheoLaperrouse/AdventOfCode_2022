import pathlib
import sys


def directory_path_size(input_commands):
    """Return the directory_path with the size of nested folders"""
    current_path = []
    directories = {}
    for command in input_commands:
        if "dir " in command:
            pass
        elif "$ ls" in command:
            pass
        elif "$ cd" in command:
            path_command = command.split()[2]
            if path_command == '..':
                current_folder = current_path.pop()
                str_path = build_path_string(current_path)
            else:
                current_folder = path_command
                current_path.append(current_folder)
                str_path = build_path_string(current_path)
                if str_path not in directories:
                    directories[str_path] = 0
        else:
            size = command.split()[0]
            for i in range(len(current_path)-1, 0, -1):
                dir_parent_path = build_path_string(current_path[:i])
                directories[dir_parent_path] += int(size)
            directories[str_path] += int(size)
    return directories


def build_path_string(path_array):
    """Return a path string according to an array of directory"""
    string_path = ''
    if len(path_array) == 1:
        return '/'
    for directory in path_array:
        if not string_path:
            string_path = directory
        elif string_path[-1] == '/':
            string_path += directory
        else:
            string_path += '/' + directory
    return string_path


def parse(puzzle_input):
    """Parse input."""
    lines_output = puzzle_input.split('\n')
    return lines_output


def part1(input_commands):
    """Solve part 1."""
    dirs = directory_path_size(input_commands)
    dir_sizes = [size for size in dirs.values() if size <= 100000]
    return sum(dir_sizes)


def part2(input_commands):
    """Solve part 2."""
    dirs = directory_path_size(input_commands)
    free_space = 70000000 - dirs['/']
    needed_space = 30000000 - free_space
    folder_sizes = [size for size in dirs.values() if size >
                    needed_space]
    return min(folder_sizes)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        commands = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(commands)}')
        print(f'Part 2 : {part2(commands)}')
