def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def part_1(inp):
    return sum(((int(line) // 3) - 2 for line in inp))


def part_2(inp):
    total_fuel = 0
    for line in inp:
        mass = int(line)
        fuel = 0
        while mass > 0:
            mass = max(0, (mass // 3) - 2)
            fuel += mass
        total_fuel += fuel
    return total_fuel


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
