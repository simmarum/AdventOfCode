import re
from collections import defaultdict, Counter


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    chron_list = sorted(inp)
    collected_data = defaultdict(list)
    for line in chron_list:
        m = re.match(
            "\\[(\\d+\\-\\d+\\-\\d+) (\\d+):(\\d+)\\] Guard #(\\d+) begins shift",
            line)
        if m:
            guard_id = m.group(4)
        m = re.match(
            "\\[(\\d+\\-\\d+\\-\\d+) (\\d+):(\\d+)\\] falls asleep",
            line)
        if m:
            sleep_minute = m.group(3)
        m = re.match("\\[(\\d+\\-\\d+\\-\\d+) (\\d+):(\\d+)\\] wakes up", line)
        if m:
            wake_minute = m.group(3)
            collected_data[guard_id].extend(
                range(int(sleep_minute), int(wake_minute)))

    max_asleep = -1
    guard_most_asleep = None
    most_asleep_minute = None
    for k, v in collected_data.items():
        if len(v) > max_asleep:
            max_asleep = len(v)
            guard_most_asleep = k
            most_asleep_minute = Counter(v).most_common()[0][0]
    return int(guard_most_asleep) * int(most_asleep_minute)


def part_2(inp):
    chron_list = sorted(inp)
    collected_data = defaultdict(list)
    for line in chron_list:
        m = re.match(
            "\\[(\\d+\\-\\d+\\-\\d+) (\\d+):(\\d+)\\] Guard #(\\d+) begins shift",
            line)
        if m:
            guard_id = m.group(4)
        m = re.match(
            "\\[(\\d+\\-\\d+\\-\\d+) (\\d+):(\\d+)\\] falls asleep",
            line)
        if m:
            sleep_minute = m.group(3)
        m = re.match("\\[(\\d+\\-\\d+\\-\\d+) (\\d+):(\\d+)\\] wakes up", line)
        if m:
            wake_minute = m.group(3)
            collected_data[guard_id].extend(
                range(int(sleep_minute), int(wake_minute)))

    max_asleep_in_minutes = -1
    guard_most_asleep = None
    most_asleep_minute = None
    for k, v in collected_data.items():
        c = Counter(v).most_common()[0]
        if c[1] > max_asleep_in_minutes:
            max_asleep_in_minutes = c[1]
            guard_most_asleep = k
            most_asleep_minute = c[0]
    return int(guard_most_asleep) * int(most_asleep_minute)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
