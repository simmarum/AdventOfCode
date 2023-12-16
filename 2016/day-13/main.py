from copy import deepcopy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def create_board(x, y):
    board = []
    for _ in range(y):
        row = []
        for _ in range(x):
            row.append('.')
        board.append(row)
    return board


def print_board(b):
    print(''.join(['{0:2}'.format(str(i))
                   for i in ([' '] + list(range(len(b[0]))))]))
    for i in range(len(b)):
        print(''.join(['{0:2}'.format(str(x)) for x in ([i] + b[i])]))


def add_walls(b, x, y, magic_number):
    for j in range(y):
        for i in range(x):
            val = ((i * i) + (3 * i) + (2 * i * j) +
                   (j) + (j * j)) + magic_number
            cnt_ones = ("{0:b}".format(val)).count('1')
            if cnt_ones % 2 == 1:
                b[j][i] = '#'


class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):

    start_node = Node(None, start)
    start_node.g = 0
    start_node.h = 0
    start_node.f = 0

    end_node = Node(None, end)
    end_node.g = 0
    end_node.h = 0
    end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (
                current_node.position[0] +
                new_position[0],
                current_node.position[1] +
                new_position[1])
            if node_position[1] > (len(maze) - 1) or node_position[1] < 0 or node_position[0] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[0] < 0:
                continue

            if maze[node_position[1]][node_position[0]] != '.':
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = (abs(child.position[0] - end_node.position[0]) +
                       abs((child.position[1] - end_node.position[1])))
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)


def draw_path(b, path):
    for p in path:
        b[p[1]][p[0]] = 'O'


def aflood(b, start, steps):
    maze = deepcopy(b)
    open_list = []
    closed_list = []

    open_list.append((start[0], start[1], 0))

    while len(open_list) > 0:
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        if current_node[2] >= steps:
            continue

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (
                current_node[0] + new_position[0],
                current_node[1] + new_position[1],
                current_node[2] + 1)
            if node_position[1] > (len(maze) - 1) or node_position[1] < 0 or node_position[0] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[0] < 0:
                continue

            if maze[node_position[1]][node_position[0]] != '.':
                continue

            if (node_position[0], node_position[1]) in [
                    (c[0], c[1]) for c in closed_list]:
                continue

            if (node_position[0], node_position[1]) in [
                    (c[0], c[1]) for c in open_list]:
                continue

            open_list.append(node_position)

    return closed_list


def part_1(inp):
    x = 45
    y = 45
    magic_number = int(inp[0])
    board = create_board(x, y)
    add_walls(board, x, y, magic_number)
    start_node = (1, 1)  # y,x
    end_node = (31, 39)  # y,x
    path = astar(board, start_node, end_node)
    # draw_path(board, path)
    # print_board(board)
    return len(path) - 1


def part_2(inp):
    x = 60
    y = 60
    magic_number = int(inp[0])
    board = create_board(x, y)
    add_walls(board, x, y, magic_number)
    start_node = (1, 1)  # y,x
    points_in_50_steps = aflood(board, start_node, 50)
    # print_board(board)
    return len(points_in_50_steps)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
