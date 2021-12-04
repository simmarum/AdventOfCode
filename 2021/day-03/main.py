from operator import itemgetter


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    inp_array = [list(x) for x in inp]
    transpose_inp = list(map(list, zip(*inp_array)))
    counts = [(x.count('0'), x.count('1')) for x in transpose_inp]
    gamma = ''
    epsilon = ''
    for one_char in counts:
        if one_char[0] > one_char[1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)


def part_2(inp):
    inp_array = [list(x) for x in inp]
    transpose_inp = list(map(list, zip(*inp_array)))
    index_left_oxygen = list(range(0, len(transpose_inp[0])))
    index_left_scrubber = list(range(0, len(transpose_inp[0])))
    magic_oxygen = ''
    magic_scrubber = ''
    for one_index in transpose_inp:
        if len(index_left_oxygen) > 1:
            cox0 = itemgetter(*index_left_oxygen)(one_index).count('0')
            cox1 = itemgetter(*index_left_oxygen)(one_index).count('1')
            if cox0 > cox1:
                magic_oxygen += '0'
            else:
                magic_oxygen += '1'
            oxygen_good = [i for i, x in enumerate(
                one_index) if x != magic_oxygen[-1]]
            index_left_oxygen = [
                x for x in index_left_oxygen if x not in oxygen_good]
        else:
            magic_oxygen += one_index[index_left_oxygen[0]]

        if len(index_left_scrubber) > 1:
            csc0 = itemgetter(*index_left_scrubber)(one_index).count('0')
            csc1 = itemgetter(*index_left_scrubber)(one_index).count('1')
            if csc0 > csc1:
                magic_scrubber += '1'
            else:
                magic_scrubber += '0'
            scrubber_good = [i for i, x in enumerate(
                one_index) if x != magic_scrubber[-1]]
            index_left_scrubber = [
                x for x in index_left_scrubber if x not in scrubber_good]
        else:
            magic_scrubber += one_index[index_left_scrubber[0]]

    return int(magic_oxygen, 2) * int(magic_scrubber, 2)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
