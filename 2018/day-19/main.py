from copy import copy


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def run_source_code(inp, max_iter, r_init, print_after_n_iter):
    r = copy(r_init)
    ip_bound = int(inp[0][-1])
    source_code = [[c if idx == 0 else int(
        c) for idx, c in enumerate(line.split())] for line in inp[1:]]
    max_ip = len(source_code)
    ip = 0
    it = 1
    while it <= max_iter:
        it += 1
        if ip >= max_ip:
            # print(f"Found results after {it=}")
            return True, r
        opcode, a, b, c = source_code[ip]
        r[ip_bound] = ip
        if opcode == 'seti':
            r[c] = a
        elif opcode == 'setr':
            r[c] = r[a]
        elif opcode == 'addi':
            r[c] = r[a] + b
        elif opcode == 'addr':
            r[c] = r[a] + r[b]
        elif opcode == 'muli':
            r[c] = r[a] * b
        elif opcode == 'mulr':
            r[c] = r[a] * r[b]
        elif opcode == 'eqrr':
            r[c] = int(r[a] == r[b])
        elif opcode == 'gtrr':
            r[c] = int(r[a] > r[b])
        else:
            raise RuntimeError(f"Found new {opcode=}")

        ip = r[ip_bound]
        ip += 1
        # if it % print_after_n_iter == 0:
        #     print(f"{r=} ({it=})")
    return False, r


def part_1(inp):
    max_iter = 10_000_000
    is_part_1, r = run_source_code(
        inp,
        max_iter=max_iter,
        r_init=[0, 0, 0, 0, 0, 0],
        print_after_n_iter=10_000_000
    )
    if is_part_1:
        return r[0]
    else:
        raise RuntimeError(f"Please increase {max_iter=}")


def part_2(inp):
    # With help of stack overflow and re-engineer solution.
    # Wait some time (in my case 1mln iteration)
    # Find the biggest number (in my case on register 3)
    # Find all factors of this number
    # Sum all factors and return as results

    _, r = run_source_code(
        inp,
        max_iter=1_000_000,
        r_init=[1, 0, 0, 0, 0, 0],
        print_after_n_iter=1_000_000
    )
    n = r[3]
    all_dividors = [d for d in range(1, n + 1) if n % d == 0]
    return sum(all_dividors)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
