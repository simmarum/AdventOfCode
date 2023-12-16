import numpy as np
from scipy import signal


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    serial_number = int(inp[0])
    screen_size = 300
    screen = np.empty((screen_size, screen_size), dtype=np.int8)
    for iy, ix in np.ndindex(screen.shape):
        screen[iy, ix] = (
            (((((ix + 10) * iy) + serial_number) * (ix + 10)) // 100) % 10) - 5

    new_screen = signal.convolve2d(screen, np.ones((3, 3)), mode='valid')
    return ','.join([
        str(int(p))
        for p in (np.unravel_index(new_screen.argmax(), new_screen.shape))[::-1]
    ])


def part_2(inp):
    serial_number = int(inp[0])
    # serial_number = 18
    screen_size = 300
    screen = np.empty((screen_size, screen_size), dtype=np.int8)
    for iy, ix in np.ndindex(screen.shape):
        screen[iy, ix] = (
            (((((ix + 10) * iy) + serial_number) * (ix + 10)) // 100) % 10) - 5
    max_fuel = 0
    max_fuel_idx = (None, None)
    max_fuel_size = 0

    for window_size in range(1, 40 + 1):
        new_screen = signal.convolve2d(screen, np.ones(
            (window_size, window_size)), mode='valid')
        tmp_idx = (np.unravel_index(new_screen.argmax(), new_screen.shape))
        tmp_max = new_screen[tmp_idx]
        if tmp_max > max_fuel:
            max_fuel = tmp_max
            max_fuel_idx = tmp_idx
            max_fuel_size = window_size
    return ','.join([str(int(p))
                    for p in max_fuel_idx[::-1]] + [str(max_fuel_size)])


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
