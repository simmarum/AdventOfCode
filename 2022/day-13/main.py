from ast import literal_eval
from functools import cmp_to_key


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def change_type(sub):
    if isinstance(sub, list):
        if len(sub) == 0:
            return [[]]
        else:
            return [change_type(ele) for ele in sub]
    else:
        return [int(sub)]


def parse_inp(inp):
    data = {}
    idx = 1
    left_line = None
    right_line = None
    for line in inp:
        if line == '':
            data[idx] = {
                'l': left_line,
                'r': right_line,
            }
            left_line = None
            right_line = None
            idx += 1

        elif left_line is not None:
            right_line = literal_eval(line)
        else:
            left_line = literal_eval(line)
    if (left_line is not None) and (right_line is not None):
        data[idx] = {
            'l': left_line,
            'r': right_line,
        }
        left_line = None
        right_line = None
        idx += 1

    return data


def compare_items(left, right):
    result = 0
    for i in range(min(len(left), len(right))):
        if (isinstance(left[i], list)) and (isinstance(right[i], list)):
            result = compare_items(left[i], right[i])
        elif (isinstance(left[i], list)) and (isinstance(right[i], list) is False):
            result = compare_items(left[i], [right[i]])
        elif (isinstance(left[i], list) is False) and (isinstance(right[i], list)):
            result = compare_items([left[i]], right[i])
        else:
            result = int(left[i] > right[i]) - int(left[i] < right[i])
        if result:
            return result
    return int(len(left) > len(right)) - int(len(left) < len(right))


def part_1(inp):
    data = parse_inp(inp)
    good_line_sum = 0
    for k, v in data.items():
        res = compare_items(v['l'], v['r'])
        if res < 0:
            good_line_sum += k
    return good_line_sum


def part_2(inp):
    data = parse_inp(inp)
    data = [[v['l'], v['r']] for _, v in data.items()]
    data = [item for sublist in data for item in sublist]
    divider_1 = [[2]]
    divider_2 = [[6]]
    data.extend([divider_1, divider_2])
    data.sort(key=cmp_to_key(compare_items))
    return (data.index(divider_1) + 1) * (data.index(divider_2) + 1)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
