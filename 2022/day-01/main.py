def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line.replace('\n', '')) for line in f.readlines()]


def part_1(inp):
    max_calories = 0
    elf_calories = 0
    for line in inp:
        if line == '':
            max_calories = max(max_calories, elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(line)
    else:
        max_calories = max(max_calories, elf_calories)

    return max_calories


def part_2(inp):
    all_calories = []
    elf_calories = 0
    for line in inp:
        if line == '':
            all_calories.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(line)
    else:
        all_calories.append(elf_calories)
    all_calories = sorted(all_calories)
    print(all_calories)
    return sum(all_calories[-3:])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
