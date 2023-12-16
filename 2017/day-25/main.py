import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def parse_input(inp):
    state = None
    checksum_step = 0
    last_state = None
    last_val = None
    states = {}
    for line in inp:
        m = re.match("Begin in state (.+)\\.", line)
        if m:
            state = m.group(1)
        m = re.match(
            "Perform a diagnostic checksum after (\\d+) steps\\.",
            line)
        if m:
            checksum_step = int(m.group(1))
        m = re.match("In state (.+):", line)
        if m:
            last_state = m.group(1)
            states[last_state] = {}
        m = re.match("  If the current value is (\\d):", line)
        if m:
            last_val = int(m.group(1))
            states[last_state][last_val] = {}
        m = re.match("    - Write the value (\\d).", line)
        if m:
            val = int(m.group(1))
            states[last_state][last_val]['write'] = val
        m = re.match("    - Move one slot to the (.*)\\.", line)
        if m:
            val = m.group(1)
            if val == 'left':
                states[last_state][last_val]['next_slot'] = -1
            if val == 'right':
                states[last_state][last_val]['next_slot'] = 1
        m = re.match("    - Continue with state (.+)\\.", line)
        if m:
            val = m.group(1)
            states[last_state][last_val]['next_state'] = val
    return state, checksum_step, states


def print_tape(step, tape, idx):
    print(f"step: {step} ", end='')
    [print(f' {str(c)} ', end='') if i != idx else print(f'[{str(c)}]', end='')
     for i, c in enumerate(tape)]
    print()


def part_1(inp):
    state, checksum_step, states = parse_input(inp)
    tape = [0 for _ in range(checksum_step + 4)]
    idx = checksum_step // 2
    for step in range(1, 1 + checksum_step):
        new_val = states[state][tape[idx]]['write']
        diff_idx = states[state][tape[idx]]['next_slot']
        state = states[state][tape[idx]]['next_state']
        tape[idx] = new_val
        idx += diff_idx

    return sum(tape)


def part_2(inp):
    return None


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
