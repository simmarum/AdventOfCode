import itertools


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def _load_data(inp):
    data = {}
    scanner = None
    beacons = set()
    for line in inp:
        if 'scanner' in line:
            if scanner is not None:
                data[scanner] = beacons
            scanner = int(line.split()[2])
            beacons = set()
        if ',' in line:
            beacon = tuple(map(int, line.split(',')))
            beacons.add(beacon)
    data[scanner] = beacons
    return data


def _rot(xx, yy, zz, one_rot):
    if one_rot[0][0] == 1:
        if one_rot[1] in (0, -0):
            xx, yy, zz = xx, yy, zz
        elif one_rot[1] in (90, -270):
            xx, yy, zz = xx, -zz, yy
        elif one_rot[1] in (180, -180):
            xx, yy, zz = xx, -yy, -zz
        elif one_rot[1] in (270, -90):
            xx, yy, zz = xx, zz, -yy
    elif one_rot[0][1] == 1:
        if one_rot[1] in (0, -0):
            xx, yy, zz = xx, yy, zz
        elif one_rot[1] in (90, -270):
            xx, yy, zz = zz, yy, -xx
        elif one_rot[1] in (180, -180):
            xx, yy, zz = -xx, yy, -zz
        elif one_rot[1] in (270, -90):
            xx, yy, zz = -zz, yy, xx
    elif one_rot[0][2] == 1:
        if one_rot[1] in (0, -0):
            xx, yy, zz = xx, yy, zz
        elif one_rot[1] in (90, -270):
            xx, yy, zz = -yy, xx, zz
        elif one_rot[1] in (180, -180):
            xx, yy, zz = -xx, -yy, zz
        elif one_rot[1] in (270, -90):
            xx, yy, zz = yy, -xx, zz
    return xx, yy, zz


def _conv(x, y, z, rotate):
    xx, yy, zz = x, y, z
    for one_rot in rotate:
        xx, yy, zz = _rot(xx, yy, zz, one_rot)
    return (xx, yy, zz)


def _conv_back(x, y, z, rotate):
    xx, yy, zz = x, y, z
    for one_rot in reversed(rotate):
        xx, yy, zz = _rot(xx, yy, zz, [one_rot[0], -one_rot[1]])
    return (xx, yy, zz)


def part_1(inp):
    data = _load_data(inp)
    scanner_to_process = [0]
    scanner_good = set([0])
    beacons_good = set(data[0])
    scanners_pos = {
        0: (0, 0, 0)
    }

    all_rotates = [
        (((1, 0, 0), 0), ((0, 1, 0), 0), ((0, 0, 1), 180)),
        (((1, 0, 0), 270), ((0, 1, 0), 0), ((0, 0, 1), 180)),
        (((1, 0, 0), 0), ((0, 1, 0), 180), ((0, 0, 1), 0)),
        (((1, 0, 0), 270), ((0, 1, 0), 180), ((0, 0, 1), 0)),
        (((1, 0, 0), 0), ((0, 1, 0), 180), ((0, 0, 1), 90)),
        (((1, 0, 0), 0), ((0, 1, 0), 270), ((0, 0, 1), 90)),
        (((1, 0, 0), 0), ((0, 1, 0), 0), ((0, 0, 1), 90)),
        (((1, 0, 0), 0), ((0, 1, 0), 90), ((0, 0, 1), 90)),
        (((1, 0, 0), 270), ((0, 1, 0), 180), ((0, 0, 1), 90)),
        (((1, 0, 0), 0), ((0, 1, 0), 90), ((0, 0, 1), 180)),
        (((1, 0, 0), 270), ((0, 1, 0), 0), ((0, 0, 1), 90)),
        (((1, 0, 0), 90), ((0, 1, 0), 270), ((0, 0, 1), 270)),
        (((1, 0, 0), 0), ((0, 1, 0), 180), ((0, 0, 1), 180)),
        (((1, 0, 0), 270), ((0, 1, 0), 180), ((0, 0, 1), 180)),
        (((1, 0, 0), 0), ((0, 1, 0), 0), ((0, 0, 1), 0)),
        (((1, 0, 0), 270), ((0, 1, 0), 0), ((0, 0, 1), 0)),
        (((1, 0, 0), 0), ((0, 1, 0), 0), ((0, 0, 1), 270)),
        (((1, 0, 0), 0), ((0, 1, 0), 90), ((0, 0, 1), 270)),
        (((1, 0, 0), 0), ((0, 1, 0), 180), ((0, 0, 1), 270)),
        (((1, 0, 0), 0), ((0, 1, 0), 270), ((0, 0, 1), 270)),
        (((1, 0, 0), 270), ((0, 1, 0), 0), ((0, 0, 1), 270)),
        (((1, 0, 0), 0), ((0, 1, 0), 270), ((0, 0, 1), 180)),
        (((1, 0, 0), 270), ((0, 1, 0), 180), ((0, 0, 1), 270)),
        (((1, 0, 0), 0), ((0, 1, 0), 90), ((0, 0, 1), 0)),
    ]
    while len(scanner_to_process) > 0:
        new_data = []
        for act in scanner_to_process:
            for k, v in data.items():
                print(
                    f"Progress: check {act} vs {k} (already found [{len(scanners_pos)}] {scanner_good}")
                if k in scanner_good:
                    continue
                at_least_12 = False
                res_data = None
                scanner_data = None
                for rotate in all_rotates:
                    for x, y, z in data[act]:
                        for xx, yy, zz in v:
                            cnt = 0
                            for xxx, yyy, zzz in data[act]:
                                if (x == xxx) and (y == yyy) and (z == zzz):
                                    continue
                                xv = xxx - x
                                yv = yyy - y
                                zv = zzz - z
                                xvv, yvv, zvv = _conv(xv, yv, zv, rotate)
                                if (xx + xvv, yy + yvv, zz + zvv) in v:
                                    cnt += 1
                            if cnt >= 11:
                                x, y, z = _conv(x, y, z, rotate)
                                xv, yv, zv = x - xx, y - yy, z - zz
                                res_data = set(
                                    [_conv_back(x + xv, y + yv, z + zv, rotate) for x, y, z in v])
                                scanner_data = _conv_back(xv, yv, zv, rotate)
                                at_least_12 = True
                            if at_least_12:
                                break
                        if at_least_12:
                            break
                    if at_least_12:
                        break
                if res_data is not None:
                    new_data.append(k)
                    scanner_good.add(k)
                    data[k] = res_data
                    scanners_pos[k] = scanner_data
                    beacons_good = beacons_good.union(res_data)
        scanner_to_process = new_data
    return len(beacons_good), scanners_pos


def part_2(scanners_pos):
    max_distance = 0
    for (x1, y1, z1), (x2, y2, z2) in itertools.combinations(scanners_pos.values(), 2):
        max_distance = max(max_distance, abs(x1 - x2) +
                           abs(y1 - y2) + abs(z1 - z2))
    return max_distance


def main():
    inp = read_file()
    res_1, scanners_pos = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(scanners_pos)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
