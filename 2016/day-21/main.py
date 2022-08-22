import re
from collections import deque
from itertools import permutations


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def scramble(inp, password):
    for line in inp:
        m = re.match('swap position (\\d+) with position (\\d+)', line)
        if m:
            x = int(m.group(1))
            y = int(m.group(2))
            password[x], password[y] = password[y], password[x]
            continue
        m = re.match('swap letter (\\w) with letter (\\w)', line)
        if m:
            x = m.group(1)
            y = m.group(2)
            password = list((''.join(password)).translate(
                str.maketrans({x: y, y: x})))
            continue
        m = re.match('rotate (\\w+) (\\d+) step', line)
        if m:
            direction = -1 if m.group(1) == 'left' else 1
            step = int(m.group(2)) % len(password)
            password = deque(password)
            password.rotate(step * direction)
            password = list(password)
            continue
        m = re.match('rotate based on position of letter (\\w)', line)
        if m:
            x = m.group(1)
            idx = password.index(x)
            if idx >= 4:
                idx += 1
            idx += 1
            password = deque(password)
            password.rotate(idx)
            password = list(password)
            continue
        m = re.match('reverse positions (\\d+) through (\\d+)', line)
        if m:
            x = int(m.group(1))
            y = int(m.group(2))
            password = password[:x] + \
                password[x:y + 1][::-1] + password[y + 1:]
            continue
        m = re.match('move position (\\d+) to position (\\d+)', line)
        if m:
            x = int(m.group(1))
            y = int(m.group(2))
            xc = password[x]
            password = password[:x] + password[x + 1:]
            password = password[:y] + [xc] + password[y:]
            continue

    return ''.join(password)


def part_1(inp):
    password = list('abcdefgh')
    return scramble(inp, password)


def part_2(inp):
    password = list('abcdefgh')
    for password_perm in permutations(password):
        scr_pass = scramble(inp, list(password_perm))
        if scr_pass == 'fbgdceah':
            return ''.join(password_perm)

    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
