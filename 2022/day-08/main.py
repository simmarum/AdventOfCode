import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    forest = np.array([[int(c) for c in line] for line in inp])
    visible_trees = set()
    for x, row in enumerate(forest):
        high_tree_left = -1
        high_tree_right = -1
        row_len = len(row)
        for y in range(row_len):
            if row[y] > high_tree_left:
                visible_trees.add((x, y))
                high_tree_left = row[y]
            if row[row_len - y - 1] > high_tree_right:
                visible_trees.add((x, row_len - y - 1))
                high_tree_right = row[row_len - y - 1]
    for x, col in enumerate(forest.T):
        high_tree_up = -1
        high_tree_down = -1
        col_len = len(col)
        for y in range(col_len):
            if col[y] > high_tree_up:
                visible_trees.add((y, x))
                high_tree_up = col[y]
            if col[col_len - y - 1] > high_tree_down:
                visible_trees.add((col_len - y - 1, x))
                high_tree_down = col[col_len - y - 1]
    return len(visible_trees)


def part_2(inp):
    forest = np.array([[int(c) for c in line] for line in inp])
    min_x, min_y, max_x, max_y = 0, 0, *forest.shape
    scenic_notation_max = 0
    for ix, iy in np.ndindex(forest.shape):
        tree = forest[ix, iy]
        scenic_notation = 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            visible_trees = 0
            new_x, new_y = ix, iy
            while True:
                new_x, new_y = new_x + dx, new_y + dy
                if (min_x <= new_x < max_x) and (min_y <= new_y < max_y):
                    if forest[new_x, new_y] < tree:
                        visible_trees += 1
                    else:
                        visible_trees += 1
                        break
                else:
                    break
            scenic_notation *= visible_trees
        scenic_notation_max = max(scenic_notation_max, scenic_notation)
    return scenic_notation_max


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
