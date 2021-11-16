def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line.replace("\n", "").replace(".", "")) for line in f.readlines()]


def part_1(inp):
    max_dist = 0
    for val in inp:
        tmp_data = val.split(" ")
        who = tmp_data[0]
        speed = int(tmp_data[3])
        fly = int(tmp_data[6])
        rest = int(tmp_data[13])
        race = 2503  # sec of the race
        full_loop = race//(fly+rest)
        last_sec = race % (fly+rest)
        last_dist_sec = last_sec
        if last_sec > fly:
            last_dist_sec = fly
        dist = full_loop*speed*fly + last_dist_sec*speed
        max_dist = max(max_dist, dist)
    return max_dist


def part_2(inp):
    data = []
    points = {}
    for val in inp:
        tmp_data = val.split(" ")
        who = tmp_data[0]
        speed = int(tmp_data[3])
        fly = int(tmp_data[6])
        rest = int(tmp_data[13])
        data.append((who, speed, fly, rest))
    for who, _, _, _ in data:
        points[who] = 0
    for i in range(1, 2503+1):
        race = i
        max_dist = 0
        tmp_res = []
        for who, speed, fly, rest in data:
            full_loop = race//(fly+rest)
            last_sec = race % (fly+rest)
            last_dist_sec = last_sec
            if last_sec > fly:
                last_dist_sec = fly
            dist = full_loop*speed*fly + last_dist_sec*speed
            tmp_res.append((who, dist))
            max_dist = max(max_dist, dist)
        for w in [x for x, y in tmp_res if y == max_dist]:
            points[w] += 1

    return max(points.values())


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
