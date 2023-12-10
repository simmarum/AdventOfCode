def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    reg = [-1, 1]
    cycle = 0
    for line in inp:
        if 'noop' in line:
            cycle += 1
            reg.append(0)
        elif 'addx' in line:
            cycle += 1
            reg.append(0)
            cycle += 1
            reg.append(int(line.split()[1]))
        else:
            print("???")
    magic_x = 0
    signal = 0
    for i in range(1, 222):
        magic_x += reg[i]
        if i in [20, 60, 100, 140, 180, 220]:
            signal += (magic_x * i)
    return signal


def part_2(inp):
    reg = [-1, 1]
    magic_x = 1
    cycle = 0
    sprite_position = [1, 2, 3]
    screen = []
    for line in inp:
        if cycle >= 40:
            cycle -= 40
        if 'noop' in line:
            cycle += 1
            screen.append('#' if cycle in sprite_position else '.')
            reg.append(0)
        elif 'addx' in line:
            cycle += 1
            screen.append('#' if cycle in sprite_position else '.')
            reg.append(0)

            cycle += 1
            screen.append('#' if cycle in sprite_position else '.')
            reg.append(int(line.split()[1]))
            magic_x += reg[-1]
            sprite_position = [0 + magic_x, 1 + magic_x, 2 + magic_x]
    [print(''.join(screen[(i * 40):(i + 1) * 40])) for i in range(6)]
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
