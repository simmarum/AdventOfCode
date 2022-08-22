import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    all_lines = []
    all_cnt = 0
    for line in inp:
        decompress_line = ''
        a = ''
        is_a = False
        b = ''
        is_b = False
        is_pattern = False
        tmp_to_repeat = ''
        to_repeat_char = 0
        for c in line:
            if is_pattern:
                tmp_to_repeat += c
                to_repeat_char += 1
                if to_repeat_char == int(a):
                    for _ in range(int(b)):
                        decompress_line += tmp_to_repeat
                    tmp_to_repeat = ''
                    is_pattern = False
                    to_repeat_char = 0
                    a = ''
                    b = ''
            elif c == 'x':
                is_a = False
                is_b = True
            elif c == ')':
                is_a = False
                is_b = False
                is_pattern = True
            elif is_a:
                a += c
            elif is_b:
                b += c
            elif c == '(':
                is_a = True
                is_b = False
            else:
                decompress_line += c
        all_lines.append(decompress_line)
        all_cnt += len(decompress_line)
    return all_cnt


def part_2(inp):
    all_cnt = 0
    for line in inp:
        cnt = 0
        w = []
        for _ in range(len(line)):
            w.append(1)
        i = 0
        while i < len(line):
            c = line[i]
            if c == '(':
                m = re.search('\\((\\d+)x(\\d+)\\)', line[i:])
                a = int(m.group(1))
                b = int(m.group(2))
                i += len(m.group(0))
                for j in range(a):
                    w[i + j] *= b
            else:
                cnt += w[i]
                i += 1

        all_cnt += cnt
    return all_cnt


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
