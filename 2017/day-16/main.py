def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def solve(inp, rounds, is_part_2):
    moves = inp[0].split(',')
    program_len = 16
    programs = [chr(i + ord('a')) for i in range(program_len)]
    all_data = [''.join(programs)]
    round_offset = None
    round_modulo = None
    for round in range(1, rounds + 1):
        for move in moves:
            if move[0] == 's':
                idx = int(move[1:])
                programs = (programs[-idx:]) + programs[:-idx]
            elif move[0] == 'x':
                idx_a, idx_b = list(map(int, move[1:].split('/')))
                programs[idx_a], programs[idx_b] = programs[idx_b], programs[idx_a]
            elif move[0] == 'p':
                p_a, p_b = move[1:].split('/')
                idx_a, idx_b = programs.index(p_a), programs.index(p_b)
                programs[idx_a], programs[idx_b] = programs[idx_b], programs[idx_a]
        str_programs = ''.join(programs)
        if str_programs in all_data:
            round_offset = all_data.index(str_programs)
            round_modulo = round - round_offset
            break
        all_data.append(str_programs)

    if is_part_2 is False:
        return ''.join(programs)
    else:
        return ''.join(all_data[(rounds - round_offset) % round_modulo])


def part_1(inp):
    return solve(inp, 1, False)


def part_2(inp):
    return solve(inp, 1_000_000_000, True)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
