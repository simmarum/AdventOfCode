from math import prod  # used in exec # noqa: F401


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def _parse_packet(packet, i):
    parse_data = []
    version_sum = 0
    packet_ver, packet = int(packet[:3], 2), packet[3:]
    version_sum += packet_ver
    packet_id, packet = int(packet[:3], 2), packet[3:]
    if packet_id == 4:
        literal_val = ''
        last_val = False
        while not last_val:
            lit_val, packet = packet[:5], packet[5:]
            if lit_val[0] == '0':
                last_val = True
            literal_val += lit_val[1:]
        literal_val = int(literal_val, 2)
        parse_data.append(literal_val)
    else:
        len_type, packet = packet[:1], packet[1:]
        if len_type == '0':
            len_subpack, packet = int(
                packet[:15], 2), packet[15:]
            subpack_data, packet = packet[:len_subpack], packet[len_subpack:]
            more_data = True
            subpack_val = []
            while more_data:
                if len(subpack_data) >= 11:
                    lit_val, subpack_version, subpack_data = _parse_packet(
                        subpack_data, i + 1)
                    version_sum += subpack_version
                    subpack_val.append(lit_val)
                else:
                    more_data = False
        else:
            num_subpack, packet = int(
                packet[:11], 2), packet[11:]
            subpack_val = []
            while num_subpack > 0:
                lit_val, subpack_version, packet = _parse_packet(
                    packet, i + 1)
                num_subpack -= 1
                version_sum += subpack_version
                subpack_val.append(lit_val)

        parse_data.append(subpack_val)

    if packet and int(packet, 2) == 0:
        return parse_data, version_sum, ''
    return parse_data, version_sum, packet


def part_1(inp):
    data = inp[0]
    data_bin = bin(int(data, 16))[2:]
    num_bits = len(data_bin) if len(
        data_bin) % 4 == 0 else 4 * (len(data_bin) // 4 + 1)
    data_bin = data_bin.zfill(num_bits)

    lit_val = []
    while data_bin:
        lit_val, version_sum, data_bin = _parse_packet(data_bin, 0)

    return version_sum


def _parse_packet_2(packet, i):
    parse_data = []
    version_sum = 0
    packet_ver, packet = int(packet[:3], 2), packet[3:]
    version_sum += packet_ver
    packet_id, packet = int(packet[:3], 2), packet[3:]
    if packet_id == 4:
        literal_val = ''
        last_val = False
        while not last_val:
            lit_val, packet = packet[:5], packet[5:]
            if lit_val[0] == '0':
                last_val = True
            literal_val += lit_val[1:]
        literal_val = int(literal_val, 2)
        parse_data.extend([packet_id, literal_val])
    else:
        len_type, packet = packet[:1], packet[1:]
        if len_type == '0':
            len_subpack, packet = int(
                packet[:15], 2), packet[15:]
            subpack_data, packet = packet[:len_subpack], packet[len_subpack:]
            more_data = True
            subpack_val = []
            while more_data:
                if len(subpack_data) >= 11:
                    lit_val, subpack_version, subpack_data = _parse_packet_2(
                        subpack_data, i + 1)
                    version_sum += subpack_version
                    subpack_val.append(lit_val)
                else:
                    more_data = False
        else:
            num_subpack, packet = int(
                packet[:11], 2), packet[11:]
            subpack_val = []
            while num_subpack > 0:
                lit_val, subpack_version, packet = _parse_packet_2(
                    packet, i + 1)
                num_subpack -= 1
                version_sum += subpack_version
                subpack_val.append(lit_val)

        parse_data.append([packet_id, subpack_val])
    if packet and int(packet, 2) == 0:
        return parse_data, version_sum, ''
    return parse_data, version_sum, packet


def _compute_res(lit_val):
    calcs = {
        0: 'sum(({x}))',
        1: 'prod(({x}))',
        2: 'min(({x}))',
        3: 'max(({x}))',
        4: '{x}',
        5: 'int(({x})>({y}))',
        6: 'int(({x})<({y}))',
        7: 'int(({x})==({y}))'
    }
    res = ''
    for v in lit_val:
        if isinstance(v[0], list):
            tr = f'\n({_compute_res(v[1])})'
            res += tr
        elif v[0] in (5, 6, 7):
            tr = f'\n({calcs[v[0]].format(x=_compute_res([v[1][0]]), y=_compute_res([v[1][1]]))}),'  # noqa
            res += tr
        elif isinstance(v[1], int):
            tr = f'\n({calcs[v[0]].format(x=v[1])}),'
            res += tr
        else:
            if isinstance(v[1][0], list):
                tr = f'\n({calcs[v[0]].format(x=_compute_res(v[1]))}),'
            else:
                tr = f'\n({calcs[v[0]].format(x=_compute_res([v[1]]))}),'
            res += tr
    return res


def unlevel(obj):
    while isinstance(obj, list) and len(obj) == 1:
        obj = obj[0]
    if isinstance(obj, list):
        return [unlevel(item) for item in obj]
    else:
        return obj


def part_2(inp):
    data = inp[0]
    data_bin = bin(int(data, 16))[2:]
    num_bits = len(data_bin) if len(
        data_bin) % 4 == 0 else 4 * (len(data_bin) // 4 + 1)
    data_bin = data_bin.zfill(num_bits)

    lit_val = []
    while data_bin:
        lit_val, version_sum, data_bin = _parse_packet_2(data_bin, 0)
    lit_val = list([unlevel(lit_val)])
    res = _compute_res(lit_val)
    loc = {}
    exec(f'a = \\{res}', globals(), loc)
    return loc['a']


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
