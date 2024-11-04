def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def part_1(inp):

    # ###
    # ### r = [0,0,0,0,0,0]
    # ### r = [A,B,C,D,E,F]

    # #ip 4                         Register 4 is for IP counter -> E = IP
    # ###                           r = [A,B,C,D,ip,F]

    # // this part check if we use proper BITWISE operator
    # 00 # seti 123 0 5             F = 123                             ip = 1
    # 01 # bani 5 456 5             F = 123 & 456 = 72                  ip = 2
    # 02 # eqri 5 72 5              F = 72 == 72 = 1                    ip = 3
    # 03 # addr 5 4 4               ip = 3 + 1 = 4                      ip = 5
    # 04 # seti 0 0 4               // skipped goto 0

    # // clear register before starting real calculation
    # 05 # seti 0 7 5               F = 0                               ip = 6

    # First loop
    # 06 # bori 5 65536 3           D = 0 | 65536 = 65536               ip = 7
    # 07 # seti 733884 6 5          F = 733884                          ip = 8

    # Second loop
    # 08 # bani 3 255 1             B = 65536 & 255 = 0                 ip = 9
    # 09 # addr 5 1 5               F = 733884 + 0 = 733884             ip = 10
    # 10 # bani 5 16777215 5        F = 733884 & 16777215 = 733884      ip=11
    # 11 # muli 5 65899 5           F = 733884 * 65899 = 48362221716    ip=12
    # 12 # bani 5 16777215 5        F = 48362221716 & 16777215 = 10285204   ip=13
    # 13 # gtir 256 3 1             B = 253 > 65536 = 0                 ip=14
    # 14 # addr 1 4 4               ip = 14 + 0 = 14                    ip=15
    # 15 # addi 4 1 4               ip = 15 + 1 = 16                    ip = 17
    # 16 # seti 27 8 4              // skipped goto line 28             ip = 28
    # 17 # seti 0 6 1               B = 0                               ip = 18

    # /// Loop that increase C one at the time as long as C * 256 > 65536 is TRUE
    # /// 65536 / 256 = 256 times
    # /// after that in line 20 C = 1 and line 23 will be triggered
    # /// Can be implement as d = d // 256
    # 18 # addi 1 1 2               C = 0 + 1 = 1                       ip = 19
    # 19 # muli 2 256 2             C = 1 * 256 = 256                   ip = 20
    # 20 # gtrr 2 3 2               C = 256 > 65536 = 0                 ip = 21
    # 21 # addr 2 4 4               ip = 21 + 0 = 21                    ip = 22
    # 22 # addi 4 1 4               ip = 22 + 1 = 23                    ip = 24
    # 23 # seti 25 4 4              // skipped goto line 26             ip = 26
    # 24 # addi 1 1 1               B = 0 + 1 = 1                       ip = 25
    # 25 # seti 17 8 4              ip = 17 // goto line 18             ip = 18
    # 26 # setr 1 7 3               D = 256                             ip = 27
    # 27 # seti 7 0 4               ip = 7  // goto line 8              ip = 8

    # 28 # eqrr 5 0 1               B = F == A // part one we need to be sure that this is true - so we can return whatever is in F
    # 29 # addr 1 4 4               ip = ip + A
    # 30 # seti 5 9 4               ip = 5                              ip = 6
    _, b, _, d, _, f = 0, 0, 0, 0, 0, 0
    # register a,c,ip is use as auxilary fields - here are not needed
    while True:
        d = f | 65536
        f = 733884
        while True:
            b = d & 255
            f += b
            f &= 16777215
            f *= 65899
            f &= 16777215
            if (256 > d):
                return f
            d = d // 256

    return None


def part_2(inp):
    _, b, _, d, _, f = 0, 0, 0, 0, 0, 0
    seen = set()
    seen_list = list()
    # register a,c,ip is use as auxilary fields - here are not needed
    while True:
        d = f | 65536
        f = 733884
        while True:
            b = d & 255
            f += b
            f &= 16777215
            f *= 65899
            f &= 16777215
            if (256 > d):
                if f in seen:
                    return seen_list[-1]
                else:
                    seen.add(f)
                    seen_list.append(f)
                    break
            d = d // 256

    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
