import heapq


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [[int(c) for c in str(line).replace('\n', '')]
                for line in f.readlines()]


def part_1(inp):
    yy = len(inp) - 1
    xx = len(inp[yy]) - 1
    start_point = (0, 0, 0)
    end_point = (xx, yy, 0)

    search_points = []

    heapq.heappush(search_points, start_point)
    path_risks = {(0, 0): 0}

    while(len(search_points) > 0):
        act_point = heapq.heappop(search_points)
        if (act_point[0] == end_point[0]) and (act_point[1] == end_point[1]):
            break

        children = []
        for new_pos in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            new_x = act_point[0] + new_pos[0]
            new_y = act_point[1] + new_pos[1]
            if (new_x > xx) or (new_x < 0) or (new_y > yy) or (new_y < 0):
                continue
            children.append((new_x, new_y, -1))

        for child in children:
            new_risk = path_risks[(act_point[0], act_point[1])] + \
                inp[child[1]][child[0]]
            if ((child[0], child[1]) not in path_risks) or (
                    new_risk < path_risks[(child[0], child[1])]):

                path_risks[(child[0], child[1])] = new_risk
                tmp_risk = new_risk + \
                    (abs(child[0] - end_point[0])) + \
                    (abs(child[1] - end_point[1]))
                heapq.heappush(search_points, (child[0], child[1], tmp_risk))
    return path_risks[(end_point[0], end_point[1])]


def part_2(inp):
    tyy = len(inp)
    txx = len(inp[0])
    yy = (5 * len(inp)) - 1
    xx = (5 * len(inp[0])) - 1
    start_point = (0, 0, 0)
    end_point = (xx, yy, 0)

    search_points = []

    heapq.heappush(search_points, start_point)
    path_risks = {(0, 0): 0}

    while(len(search_points) > 0):
        act_point = heapq.heappop(search_points)
        if (act_point[0] == end_point[0]) and (act_point[1] == end_point[1]):
            break

        children = []
        for new_pos in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            new_x = act_point[0] + new_pos[0]
            new_y = act_point[1] + new_pos[1]
            if (new_x > xx) or (new_x < 0) or (new_y > yy) or (new_y < 0):
                continue
            children.append((new_x, new_y, -1))

        for child in children:
            tmp_risk_calc = (inp[child[1] %
                                 tyy][child[0] %
                                      txx] + child[0] // txx + child[1] // tyy)
            tmp_risk_calc = tmp_risk_calc % 9 if tmp_risk_calc > 9 else tmp_risk_calc
            new_risk = path_risks[(act_point[0], act_point[1])] + tmp_risk_calc
            if ((child[0], child[1]) not in path_risks) or (
                    new_risk < path_risks[(child[0], child[1])]):

                path_risks[(child[0], child[1])] = new_risk
                tmp_risk = new_risk + \
                    (abs(child[0] - end_point[0])) + \
                    (abs(child[1] - end_point[1]))
                heapq.heappush(search_points, (child[0], child[1], tmp_risk))
    return path_risks[(end_point[0], end_point[1])]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
