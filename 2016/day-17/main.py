from hashlib import md5


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def adoor(start, end, salt):
    dirs = {
        0: 'U',
        1: 'D',
        2: 'L',
        3: 'R',
    }
    open_list = [(salt, start)]
    max_length = 0
    min_path = None

    while open_list:
        next_salt, current_pos = open_list.pop(0)
        if current_pos == end:
            path = next_salt[len(salt):]
            path_len = len(path)
            max_length = max(max_length, path_len)
            if min_path is None or path_len < len(min_path):
                min_path = path
            continue

        x, y = current_pos
        for i, tmp_pos in enumerate(
                [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]):
            xx, yy = tmp_pos
            h = md5(next_salt.encode()).hexdigest()[:4]
            if (0 <= xx <= 3) and (0 <= yy <= 3) and (h[i] in 'bcdef'):
                open_list.append((next_salt + dirs[i], tmp_pos))

    return min_path, max_length


def part_1(inp):
    start_node = (0, 0)
    end_node = (3, 3)
    salt = inp[0]
    # salt = 'ihgpwlah'  # DDRRRD
    # salt = 'kglvqrro'  # DDUDRLRRUDRD
    # salt = 'ulqzkmiv'  # DRURDRUDDLLDLUURRDULRLDUUDDDRR
    min_path, _ = adoor(start_node, end_node, salt)
    return min_path


def part_2(inp):
    start_node = (0, 0)
    end_node = (3, 3)
    salt = inp[0]
    # salt = 'ihgpwlah'  # 370
    # salt = 'kglvqrro'  # 492
    # salt = 'ulqzkmiv'  # 830
    _, max_length = adoor(start_node, end_node, salt)
    return max_length


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
