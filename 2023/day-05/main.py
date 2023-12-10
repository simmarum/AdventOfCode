def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    seeds = []
    idx = 0
    for line in inp:
        if "seeds:" in line:
            seeds = [[int(x.strip())]
                     for x in line.replace("seeds: ", "").split(" ")]
            continue
        if "map:" in line:
            idx += 1
            continue
        if "\n" == line:
            if idx > 0:
                for seed in seeds:
                    if len(seed) <= idx:
                        seed.append(seed[-1])
            continue
        map_line = [int(x.strip()) for x in line.split(" ")]
        for seed in seeds:
            if (map_line[1] <= seed[idx - 1] <=
                    map_line[1] + (map_line[2] - 1)):
                seed.append(seed[idx - 1] - map_line[1] + map_line[0])

    if idx > 0:
        for seed in seeds:
            if len(seed) <= idx:
                seed.append(seed[-1])
    return min([s[7] for s in seeds])


def part_2(inp):
    seeds = []
    maps = []
    one_map = []
    for line in inp:
        if "seeds:" in line:
            tmp_seeds = [int(x.strip())
                         for x in line.replace("seeds: ", "").split(" ")]
            seeds = [
                (
                    tmp_seeds[i * 2],
                    tmp_seeds[i * 2] + tmp_seeds[(i * 2) + 1] - 1
                )
                for i in range(len(tmp_seeds) // 2)
            ]
            seeds = sorted(seeds)
            continue
        if "map:" in line:
            if one_map:
                maps.append(sorted(one_map, key=lambda x: x[1]))
            one_map = []
            continue
        if "\n" == line:
            continue
        one_map.append([int(x.strip()) for x in line.split(" ")])
    maps.append(one_map)
    final_locations = []
    for seed in seeds:
        ranges = [[seed[0], seed[1]]]
        results = []
        for one_map in maps:
            while ranges:
                range_start, range_end = ranges.pop()
                for one_map_line in one_map:
                    map_start = one_map_line[1]
                    map_end = one_map_line[1] + one_map_line[2]
                    offset = one_map_line[0] - one_map_line[1]
                    if range_start >= map_end:
                        continue
                    if range_end <= map_start:
                        continue
                    if range_start < map_start:
                        ranges.append([range_start, map_start])
                        range_start = map_start
                    if range_end > map_end:
                        ranges.append([map_end, range_end])
                        range_end = map_end
                    results.append([range_start + offset, range_end + offset])
                    break
                else:
                    results.append([range_start, range_end])
            ranges = results
            results = []
        final_locations += ranges
    return min([x[0] for x in final_locations])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
