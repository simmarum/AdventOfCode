from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def get_val(regs, k):
    try:
        return int(k)
    except ValueError:
        return regs[k]


def part_1(inp):
    last_sound_played = None
    regs = defaultdict(int)
    idx = 0
    step = 0
    while idx < len(inp):
        step += 1
        if step > 2650:
            break
        line_spl = inp[idx].split()
        # print(line_spl, regs)
        if line_spl[0] == 'snd':
            last_sound_played = get_val(regs, line_spl[1])
            idx += 1
        elif line_spl[0] == 'set':
            regs[line_spl[1]] = get_val(regs, line_spl[2])
            idx += 1
        elif line_spl[0] == 'add':
            regs[line_spl[1]] += get_val(regs, line_spl[2])
            idx += 1
        elif line_spl[0] == 'mul':
            regs[line_spl[1]] *= get_val(regs, line_spl[2])
            idx += 1
        elif line_spl[0] == 'mod':
            regs[line_spl[1]] %= get_val(regs, line_spl[2])
            idx += 1
        elif line_spl[0] == 'rcv':
            if get_val(regs, line_spl[1]) != 0:
                return last_sound_played
            else:
                idx += 1
        elif line_spl[0] == 'jgz':
            if get_val(regs, line_spl[1]) > 0:
                idx += get_val(regs, line_spl[2])
            else:
                idx += 1
    return regs


def part_2(inp):
    data = {}
    data[0] = {
        'regs': defaultdict(int),
        'idx': 0,
        'box': [],
        'snd_cnt': 0
    }
    data[0]['regs']['p'] = 0
    data[1] = {
        'regs': defaultdict(int),
        'idx': 0,
        'box': [],
        'snd_cnt': 0
    }
    data[1]['regs']['p'] = 1
    is_wait = {
        0: False,
        1: False
    }
    is_finished = {
        0: False,
        1: False
    }

    while True:
        if is_wait[0] and is_wait[1]:
            break
        if is_finished[0] and is_finished[1]:
            break
        for p in [0, 1]:
            if data[p]['idx'] >= len(inp):
                is_finished[p] = True
                break

            line_spl = inp[data[p]['idx']].split()

            if line_spl[0] == 'snd':
                data[(p + 1) %
                     2]['box'].append(get_val(data[p]['regs'], line_spl[1]))
                data[p]['snd_cnt'] += 1
                data[p]['idx'] += 1
            elif line_spl[0] == 'set':
                data[p]['regs'][line_spl[1]] = get_val(
                    data[p]['regs'], line_spl[2])
                data[p]['idx'] += 1
            elif line_spl[0] == 'add':
                data[p]['regs'][line_spl[1]
                                ] += get_val(data[p]['regs'], line_spl[2])
                data[p]['idx'] += 1
            elif line_spl[0] == 'mul':
                data[p]['regs'][line_spl[1]
                                ] *= get_val(data[p]['regs'], line_spl[2])
                data[p]['idx'] += 1
            elif line_spl[0] == 'mod':
                data[p]['regs'][line_spl[1]] %= get_val(
                    data[p]['regs'], line_spl[2])
                data[p]['idx'] += 1
            elif line_spl[0] == 'rcv':
                if data[p]['box']:
                    data[p]['regs'][line_spl[1]] = data[p]['box'].pop(0)
                    data[p]['idx'] += 1
                    is_wait[p] = False
                else:
                    is_wait[p] = True
            elif line_spl[0] == 'jgz':
                if get_val(data[p]['regs'], line_spl[1]) > 0:
                    data[p]['idx'] += get_val(data[p]['regs'], line_spl[2])
                else:
                    data[p]['idx'] += 1
    return data[1]['snd_cnt']


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
