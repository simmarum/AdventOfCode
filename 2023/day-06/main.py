from sympy import symbols, solve


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    times = [int(x.strip())
             for x in inp[0].replace("Time:", "").split(" ") if x.strip() != ""]
    distances = [int(x.strip())
                 for x in inp[1].replace("Distance:", "").split(" ") if x.strip() != ""]

    magic_num = 1
    for race in range(len(times)):
        t = times[race]
        d = distances[race]
        x = symbols('x')
        expr = (t - x) * x - d - 0.1
        sol = solve(expr)
        wins = int(sol[1]) - int(sol[0])
        magic_num *= wins
    return magic_num


def part_2(inp):
    t = int(inp[0][5:].replace(" ", ""))
    d = int(inp[1][9:].replace(" ", ""))
    x = symbols('x')
    expr = (t - x) * x - d - 0.1
    sol = solve(expr)
    wins = int(sol[1]) - int(sol[0])
    return wins


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
