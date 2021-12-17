def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    data = inp[0].split(':')[1].split(',')
    x_area = list(map(int, data[0].split('=')[1].split('..')))
    y_area = list(map(int, data[1].split('=')[1].split('..')))

    max_x = -1
    found_max_x = False
    while not found_max_x:
        max_x += 1
        if sum(range(max_x + 1)) > x_area[0]:
            found_max_x = True
    all_vels = []

    max_y = -1
    while max_y < 200:
        max_y += 1
        vel_lock = [max_x, max_y]
        vel = [max_x, max_y]
        probe = [0, 0]
        probe_max_y = 0
        while True:
            probe = [probe[0] + vel[0], probe[1] + vel[1]]
            if vel[0] != 0:
                vel[0] = vel[0] - 1 if vel[0] > 0 else vel[0] + 1
            vel[1] -= 1
            probe_max_y = max(probe_max_y, probe[1])
            if (probe[0] >= x_area[0]) and (probe[0] <= x_area[1]) and (
                    probe[1] >= y_area[0]) and (probe[1] <= y_area[1]):
                all_vels.append((vel_lock, probe_max_y))
            if (probe[0] > x_area[1]) or (probe[1] < y_area[1]):
                # print("Overshot!", [max_x, max_y])
                break
    all_vels = sorted(all_vels, key=lambda x: x[1], reverse=True)
    # print(all_vels[0])
    return all_vels[0][1]


def part_2(inp):
    data = inp[0].split(':')[1].split(',')
    x_area = list(map(int, data[0].split('=')[1].split('..')))
    y_area = list(map(int, data[1].split('=')[1].split('..')))

    all_vels = set()
    for x in range(0, x_area[1] + 1):
        for y in range(y_area[0], -y_area[0]):
            vel = [x, y]
            probe = [0, 0]
            while True:
                probe = [probe[0] + vel[0], probe[1] + vel[1]]
                if vel[0] != 0:
                    vel[0] = vel[0] - 1 if vel[0] > 0 else vel[0] + 1
                vel[1] -= 1
                if (probe[0] >= x_area[0]) and (probe[0] <= x_area[1]) and (
                        probe[1] >= y_area[0]) and (probe[1] <= y_area[1]):
                    all_vels.add((x, y))
                if (probe[0] > x_area[1]) or (probe[1] < y_area[0]):
                    # print("Overshot!", [max_x, max_y])
                    break
    return len(all_vels)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
