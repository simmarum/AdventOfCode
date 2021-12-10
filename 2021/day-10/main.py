import queue


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    quotes = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    bad_endings = []
    for one_line in inp:
        q = queue.LifoQueue()
        for c in one_line:
            if c in quotes.keys():
                q.put(c)
            elif c in quotes.values():
                qc = q.get()
                if c != quotes[qc]:
                    bad_endings.append(c)
                    # print(f"Expected '{quotes[qc]}' got '{c}'!")
                    break
    bad_endings = [points[c] for c in bad_endings]
    return sum(bad_endings)


def part_2(inp):
    quotes = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    missing_scores = []
    for one_line in inp:
        q = queue.LifoQueue()
        bad_line = False
        for c in one_line:
            if c in quotes.keys():
                q.put(c)
            elif c in quotes.values():
                qc = q.get()
                if c != quotes[qc]:
                    bad_line = True
                    break
        if (bad_line is False) and (not q.empty()):
            missing_endings = [quotes[q.get()] for _ in range(q.qsize())]
            # print(f"There are some missing characters: {missing_endings}")
            line_score = 0
            for one_missing_char in missing_endings:
                line_score = (line_score * 5) + points[one_missing_char]
            missing_scores.append(line_score)
    missing_scores = sorted(missing_scores)

    return missing_scores[int(len(missing_scores)/2)]


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
