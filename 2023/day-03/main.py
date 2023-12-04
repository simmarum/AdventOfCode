import numpy as np


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    sum_of_good_nums = 0
    adj = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 0], [0, 1],
        [1, -1], [1, 0], [1, 1],
    ]
    engine = np.array([[y for y in x] for x in inp])
    nums = [

    ]
    curr_num = []
    for iy, ix in np.ndindex(engine.shape):
        if ix == 0:
            curr_num = []
        if engine[iy, ix] in '1234567890':
            curr_num.append((iy, ix))
        else:
            if curr_num:
                nums.append(curr_num)
                curr_num = []
        if ix == engine.shape[1] - 1:
            if curr_num:
                nums.append(curr_num)
                curr_num = []

    for num in nums:
        num_adjs = set()
        for dig in num:
            for a in adj:
                niy = dig[0] + a[0]
                nix = dig[1] + a[1]
                if (0 <= niy < engine.shape[0]) and (
                        0 <= nix < engine.shape[1]):
                    num_adjs.add((niy, nix))
        num_adjs.difference_update(set(num))
        is_good_num = False
        for num_adj in num_adjs:
            if engine[num_adj[0], num_adj[1]] != '.':
                is_good_num = True
        if is_good_num:
            good_num = ''
            for dig in num:
                good_num += engine[dig[0], dig[1]]
            good_num = int(good_num)
            sum_of_good_nums += good_num
    return sum_of_good_nums


def part_2(inp):
    sum_of_good_ratio = 0
    adj = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 0], [0, 1],
        [1, -1], [1, 0], [1, 1],
    ]
    engine = np.array([[y for y in x] for x in inp])
    for iy, ix in np.ndindex(engine.shape):
        if engine[iy, ix] in '*':
            potential_nums = set()
            for a in adj:
                niy = iy + a[0]
                nix = ix + a[1]
                if (0 <= niy < engine.shape[0]) and (
                        0 <= nix < engine.shape[1]):
                    if engine[niy, nix] in '1234567890':
                        potential_nums.add((niy, nix))
            poss_nums = set()
            for one_dig in potential_nums:
                new_num = engine[one_dig[0], one_dig[1]]
                more_on_left = True
                more_on_right = True
                shift_l = -1
                shift_r = 1
                while more_on_left or more_on_right:
                    if more_on_left:
                        niy = one_dig[0]
                        nix = one_dig[1] + shift_l
                        if (0 <= niy < engine.shape[0]) and (
                                0 <= nix < engine.shape[1]):
                            if engine[niy, nix] in '1234567890':
                                new_num = engine[niy, nix] + new_num
                                shift_l -= 1
                            else:
                                more_on_left = False
                        else:
                            more_on_left = False
                    if more_on_right:
                        niy = one_dig[0]
                        nix = one_dig[1] + shift_r
                        if (0 <= niy < engine.shape[0]) and (
                                0 <= nix < engine.shape[1]):
                            if engine[niy, nix] in '1234567890':
                                new_num = new_num + engine[niy, nix]
                                shift_r += 1
                            else:
                                more_on_right = False
                        else:
                            more_on_right = False
                new_num = int(new_num)
                poss_nums.add(new_num)
            if len(poss_nums) == 2:
                l_poss_nums = list(poss_nums)
                sum_of_good_ratio += l_poss_nums[0] * l_poss_nums[1]
    return sum_of_good_ratio


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
