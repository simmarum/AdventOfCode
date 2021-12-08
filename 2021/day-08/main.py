import itertools


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    all_easy_digit = 0
    for one_line in inp:
        data_in, data_out = one_line.split('|')
        data_in = data_in.split()
        data_out = data_out.split()
        all_easy_digit += sum([1 for one_digit in data_out if len(one_digit)
                               in (2, 4, 3, 7)])
    return all_easy_digit


def part_2(inp):
    all_perm = [''.join(x) for x in itertools.permutations('abcdefg')]
    magic_comb = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg'
    }
    magic_comb_reversed = {v: k for (k, v) in magic_comb.items()}
    all_digits = 0
    for one_line in inp:
        data_in, data_out = one_line.split('|')
        data_in = data_in.split()
        data_out = data_out.split()
        basic_order = 'abcdefg'
        magic_perm = None
        for one_perm in all_perm:
            good_perm = True
            for one_data_in in data_in:
                one_data_in = ''.join(sorted(one_data_in, key=lambda word: [
                                      one_perm.index(c) for c in word[0]]))
                tmp_table = one_data_in.maketrans(one_perm, basic_order)
                one_data_in_trans = one_data_in.translate(tmp_table)
                if one_data_in_trans not in magic_comb_reversed:
                    good_perm = False
                    break
            if good_perm:
                magic_perm = one_perm
                break
        one_number = []
        for one_data_out in data_out:
            one_data_out = ''.join(sorted(one_data_out, key=lambda word: [
                magic_perm.index(c) for c in word[0]]))
            tmp_table = one_data_out.maketrans(magic_perm, basic_order)
            one_data_out_trans = one_data_out.translate(tmp_table)
            one_digit = magic_comb_reversed[one_data_out_trans]
            one_number.append(str(one_digit))
        one_number = int(''.join(one_number))
        all_digits += one_number
    return all_digits


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
