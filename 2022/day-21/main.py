import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    data = {}
    for line in inp:
        x = line.split()
        if len(x) == 4:
            data[x[0][:-1]] = f'({{{x[1]}}}{x[2]}{{{x[3]}}})'
        elif len(x) == 2:
            data[x[0][:-1]] = x[1]
        else:
            raise RuntimeError(f"New patter for {x}")
    equation = data['root']
    while True:
        new_equation = equation.format(**data)
        if new_equation == equation:
            break
        equation = new_equation
    res = eval(equation)
    res = int(res) if int(res) == res else res
    return res


def part_2(inp):
    # reversed data
    data = {}
    for line in inp:
        x = line.split()
        if len(x) == 4:
            data[x[0][:-1]] = f'({{{x[1]}}}{x[2]}{{{x[3]}}})'
        elif len(x) == 2:
            data[x[0][:-1]] = x[1]
        else:
            raise RuntimeError(f"New patter for {x}")
    equation_left, equation_right = re.split(r'\+|/|\*|\-', data['root'][1:-1])

    data['humn'] = 'my_magic_number'

    while True:
        new_equation = equation_left.format(**data)
        if new_equation == equation_left:
            break
        equation_left = new_equation
    while True:
        new_equation = equation_right.format(**data)
        if new_equation == equation_right:
            break
        equation_right = new_equation

    my_magic_number = 0
    diff = 1_000_000_000_000
    lower = False
    for step in range(100):

        tmp_equation_left = equation_left.replace(
            'my_magic_number', str(my_magic_number))
        tmp_equation_right = equation_right.replace(
            'my_magic_number', str(my_magic_number))
        res_left = eval(tmp_equation_left)
        res_left = int(res_left) if int(res_left) == res_left else res_left
        res_right = eval(tmp_equation_right)
        res_right = int(res_right) if int(
            res_right) == res_right else res_right
        # print(step, lower, diff, my_magic_number, res_left, res_right)
        if res_left == res_right:
            break
        elif res_left < res_right:
            if not lower:
                diff /= 2
                lower = True
            my_magic_number -= diff
        else:
            if lower:
                diff /= 2
                lower = False
            my_magic_number += diff

    my_magic_number = int(my_magic_number) if int(
        my_magic_number) == my_magic_number else my_magic_number
    return my_magic_number


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
