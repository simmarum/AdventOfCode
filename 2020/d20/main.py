import numpy as np
from collections import defaultdict
import math
from functools import reduce
from operator import mul

np.set_printoptions(linewidth=300)


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [line for line in f.read().split("\n\n")]


def _prep_in(inp):
    in_data = {}
    for val in inp:
        val = val.split("\n")
        k = int(val[0].split(" ")[1].replace(":", ""))
        v = np.array([[c for c in line] for line in val[1:]])
        in_data[k] = v
    return in_data


def _edges(v):
    e1 = v[0]
    e2 = v[-1]
    e3 = v[:, 0]
    e4 = v[:, -1]
    ee = [e1, e2, e3, e4]
    ee = ee + [reversed(x) for x in ee]
    return [''.join(x) for x in ee]


def _next_state(v):
    for _ in range(4):
        yield v
        yield np.flip(v, axis=0)
        v = np.rot90(v, k=3)


def _find_next_square(new_k, new_v, eem, in_data):
    e3 = ''.join(new_v[:, -1])
    tmp_k = [x for x in eem[e3] if x != new_k][0]
    new_vv = in_data[tmp_k]
    for nnv in _next_state(new_vv):
        if e3 == ''.join(nnv[:, 0]):
            return tmp_k, nnv


def _check_all_poss_1(in_data):
    eem = defaultdict(list)
    for k, v in in_data.items():
        for e in _edges(v):
            eem[e].append(k)

    cors = []
    for k, v in in_data.items():
        cnt = sum([len(eem[e])-1 for e in _edges(v)[:4]])
        if cnt == 2:
            cors.append(k)

    return reduce(mul, cors)


def _check_all_poss_2(in_data):
    sqr = int(math.sqrt(len(in_data)))

    eem = defaultdict(list)
    for k, v in in_data.items():
        for e in _edges(v):
            eem[e].append(k)

    cors = []
    for k, v in in_data.items():
        cnt = sum([len(eem[e])-1 for e in _edges(v)[:4]])
        if cnt == 2:
            cors.append(k)

    ltk = cors[0]
    ltv = in_data[ltk]
    for nltv in _next_state(ltv):
        if ((len(eem[''.join(nltv[:, -1])]) == 2)
                and (len(eem[''.join(nltv[-1])]) == 2)):
            ltv = nltv
            break

    big_square_ind = [[None]*sqr for _ in range(sqr)]
    big_square_ind[0][0] = (ltk, ltv)
    for y in range(sqr):
        if y > 0:
            ak, av = big_square_ind[y-1][0]
            nk, nv = _find_next_square(ak, np.flip(
                np.rot90(av, k=1), axis=0), eem, in_data)
            big_square_ind[y][0] = (nk, np.flip(np.rot90(nv, k=1), axis=0))

        for x in range(1, sqr):
            ak, av = big_square_ind[y][x-1]
            big_square_ind[y][x] = _find_next_square(ak, av, eem, in_data)

    rows = []
    for y in range(sqr):
        rows.append(
            np.hstack(
                [big_square_ind[y][x][1][1:-1, 1:-1] for x in range(sqr)]))
    big_image = np.vstack(rows)

    monster = np.array([
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
         '.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
        ['#', '.', '.', '.', '.', '#', '#', '.', '.', '.',
         '.', '#', '#', '.', '.', '.', '.', '#', '#', '#'],
        ['.', '#', '.', '.', '#', '.', '.', '#', '.', '.',
         '#', '.', '.', '#', '.', '.', '#', '.', '.', '.']
    ])
    ly_m = len(monster)
    lx_m = len(monster[0])
    l_img = len(big_image)
    for n_img in _next_state(big_image):
        cnt = 0
        for y in range(l_img-ly_m):
            for x in range(l_img-lx_m):
                good_one = True
                for ym in range(ly_m):
                    for xm in range(lx_m):
                        if ((monster[ym][xm] == '#')
                                and (n_img[y+ym][x+xm] != '#')):
                            good_one = False
                            break
                    if not good_one:
                        break
                if good_one:
                    cnt += 1
        if cnt > 0:
            break

    res = np.count_nonzero(n_img == '#') - cnt*np.count_nonzero(monster == '#')
    return res


def part_1(inp):
    in_data = _prep_in(inp)
    res = _check_all_poss_1(in_data)
    return res


def part_2(inp):
    in_data = _prep_in(inp)
    res = _check_all_poss_2(in_data)
    return res


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
