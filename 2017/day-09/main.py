def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    for line in inp:
        magic_sum = 0
        group_lvl = 0
        is_garbage_open = False
        is_exclamation_mark = False
        for c in line:
            if is_exclamation_mark:
                is_exclamation_mark = False
            elif c == '!':
                is_exclamation_mark = True
            elif c == '<' and is_garbage_open is False:
                is_garbage_open = True
            elif c == '>':
                is_garbage_open = False
            elif c == '{' and is_garbage_open is False:
                group_lvl += 1
            elif c == '}' and is_garbage_open is False:
                magic_sum += group_lvl
                group_lvl -= 1
    return magic_sum


def part_2(inp):
    for line in inp:
        removed_chars = 0
        is_garbage_open = False
        is_exclamation_mark = False
        for c in line:
            if is_garbage_open:
                removed_chars += 1
            if is_exclamation_mark:
                is_exclamation_mark = False
                removed_chars -= 1
            elif c == '!':
                is_exclamation_mark = True
                removed_chars -= 1
            elif c == '<' and is_garbage_open is False:
                is_garbage_open = True
            elif c == '>' and is_garbage_open is True:
                is_garbage_open = False
                removed_chars -= 1
            elif c == '{' and is_garbage_open is False:
                pass
            elif c == '}' and is_garbage_open is False:
                pass
    return removed_chars


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
