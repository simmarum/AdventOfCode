from itertools import accumulate


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def fft_slow(signal, base_pattern, max_phase):
    signal_len = len(signal)
    for _ in range(1, max_phase + 1):
        signal = [abs(sum(((e * base_pattern[(i // s_id) %
                                             4]) for i, e in enumerate(signal, 1)))) %
                  10 for s_id in range(1, signal_len + 1)]
    return ''.join((str(c) for c in signal[:8]))


def part_1(inp):
    signal = [int(c) for c in inp[0]]
    base_pattern = [0, 1, 0, -1]
    max_phase = 100
    new_signal_8 = fft_slow(signal, base_pattern, max_phase)
    return new_signal_8


def fft_fast_last_quarter(signal, message_offset, max_phase):
    # Works only with base pattern equal [0,1,0,-1]
    # To cumulative sum works we need to do it from the end
    signal_with_offset = list(reversed(signal[message_offset:]))

    for _ in range(1, max_phase + 1):
        # We can just add values and do modulo 10
        # All numbers should be negative (-1 from pattern)
        # But then we could extract before bracket this -1 and apply to final
        # value so it does not matter
        signal_with_offset = list(
            accumulate(
                signal_with_offset, lambda a, b: (
                    a + b) %
                10))
    return ''.join((str(c) for c in reversed(signal_with_offset[-8:])))


def part_2(inp):
    signal = [int(c) for c in inp[0]] * 10000
    singal_len = len(signal)
    max_phase = 100
    message_offset = int(''.join((str(c) for c in signal[:7])))
    message_location_percentage = message_offset / singal_len
    if message_location_percentage < 0.75:
        raise RuntimeError(
            f"{message_location_percentage=} is less than 75% - so current solution will not work")
    # Assume that message offset is in last quarter
    # Then we can do cumulative sums and last quarter of data
    # Because of base_pattern = [0,1,0,-1] we always multiplicate all numbers
    # by -1 in last quarter
    new_signal_8 = fft_fast_last_quarter(signal, message_offset, max_phase)
    return new_signal_8


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
