import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    forest_input = puzzle_input.split('\n')
    for index, row in enumerate(forest_input):
        tab_forest = [int(tree) for tree in row]
        forest_input[index] = tab_forest
    return forest_input


def visible(value_tree, list_value):
    """Return if a tree is visible or not according to a list of value"""
    return all(val < value_tree or len(list_value) == 0 for val in list_value)


def tree_score(value_tree, list_value):
    """Return the score of a tree"""
    score = 0
    for val in list_value:
        score += 1
        if val >= value_tree:
            break
    return score


def part1(forest):
    """Solve part 1."""
    visible_trees = 0
    for index_row, row_forest in enumerate(forest):
        size = len(forest[0])
        for index_column, tree in enumerate(row_forest):
            column = [forest[index][index_column]
                      for index in range(0, size)]
            conditions = [
                visible(tree, row_forest[0:index_column]),  # Left
                visible(tree, row_forest[index_column + 1:]),  # Right
                visible(tree, column[:index_row]),  # Up
                visible(tree, column[index_row+1:]),  # Down
            ]
            visible_trees += 1 if any(conditions) else 0
    return visible_trees


def part2(forest):
    """Solve part 2."""
    scores = []
    for index_row, row_forest in enumerate(forest):
        size = len(forest[0])
        for index_column, tree in enumerate(row_forest):
            column = [forest[index][index_column]
                      for index in range(0, size)]
            scores.append(
                tree_score(tree, row_forest[0:index_column][::-1]) *
                tree_score(tree, row_forest[index_column + 1:]) *
                tree_score(tree, column[:index_row][::-1]) *
                tree_score(tree, column[index_row+1:])
            )
    return max(scores)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input_text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        input_forest = parse(input_text)
        print(path)
        print(f'Part 1 : {part1(input_forest)}')
        print(f'Part 2 : {part2(input_forest)}')
