def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def solve(inp, is_part_2):
    data = [x.split() for x in inp]
    div1, div26 = [], []
    for i in range(0, len(data) - 4, 18):
        if data[i + 4][2] == "1":
            div1.append(int(data[i + 15][2]))
            div26.append(None)
        else:
            div1.append(None)
            div26.append(int(data[i + 5][2]))

    modelNo = [0] * 14
    stack = []
    if is_part_2 is False:
        startDigit = 9
    else:
        startDigit = 1
    for i, (a, b) in enumerate(zip(div1, div26)):
        if a:
            stack.append((i, a))
        else:
            ia, a = stack.pop()
            diff = a + b
            if is_part_2 is False:
                modelNo[ia] = min(startDigit, startDigit - diff)
                modelNo[i] = min(startDigit, startDigit + diff)
            else:
                modelNo[ia] = max(startDigit, startDigit - diff)
                modelNo[i] = max(startDigit, startDigit + diff)
    return ''.join([str(x) for x in modelNo])


def part_1(inp):
    return solve(inp, False)


def part_2(inp):
    return solve(inp, True)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
