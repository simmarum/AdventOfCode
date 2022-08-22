from collections import Counter
import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    sum_sector_id = 0
    for line in inp:
        m = re.search('(.*)-(\\d+)\\[(.*)\\]', line)
        room = m.group(1).replace('-', '')
        sector_id = int(m.group(2))
        checksum = m.group(3)

        room_cnt = Counter(room)
        room_cnt_sorted = sorted(
            room_cnt.items(), key=lambda item: (-item[1], item[0]))[0:5]
        checksum_calc = ''.join([c[0] for c in room_cnt_sorted])

        if checksum == checksum_calc:
            sum_sector_id += sector_id

    return sum_sector_id


def part_2(inp):
    target_sector_id = None
    for line in inp:
        m = re.search('(.*)-(\\d+)\\[(.*)\\]', line)
        room = m.group(1)
        sector_id = int(m.group(2))
        checksum = m.group(3)

        room_cnt = Counter(room.replace('-', ''))
        room_cnt_sorted = sorted(
            room_cnt.items(), key=lambda item: (-item[1], item[0]))[0:5]
        checksum_calc = ''.join([c[0] for c in room_cnt_sorted])
        if checksum == checksum_calc:
            shift_num = sector_id % 26
            decrypt = ''
            for c in room:
                if c == '-':
                    decrypt += ' '
                else:
                    decrypt += chr((ord(c) + shift_num - 97) % 26 + 97)
            if decrypt == 'northpole object storage':
                target_sector_id = sector_id
                break
    return target_sector_id


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
