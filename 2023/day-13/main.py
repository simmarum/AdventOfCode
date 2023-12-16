from Levenshtein import distance as lev


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace("\n", "") for line in f.readlines()]


def read_patterns(inp):
    patterns = []
    pattern = []
    for line in inp:
        if not line:
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)
    patterns.append(pattern)
    return patterns


def check_palindrom(s, p1=True):
    if p1 is True:
        return s == s[::-1]
    else:
        return sum([lev(p[0], p[1]) for p in zip(s[:len(s) // 2],
                                                 reversed(s[(len(s) + 1) // 2:]))]) == 1


def find_palindromes(input_word, p1=True):
    centers = set()
    n = len(input_word)
    i = 0
    for j in range(n, 1, -1):
        if (j - i) % 2 == 1:
            continue
        if check_palindrom(input_word[i:j], p1):
            centers.add(j // 2)
            break
    j = n
    for i in range(0, n - 1, 1):
        if (j - i) % 2 == 1:
            continue
        if check_palindrom(input_word[i:j], p1):
            centers.add(j - ((j - i) // 2))
            break

    return centers


def part_1(inp):
    magic_sum = 0
    patterns = read_patterns(inp)
    for p in patterns:
        # cols
        pt = [''.join(e) for e in list(map(list, zip(*p)))]
        palindromes = find_palindromes(pt)
        magic_sum += sum([p for p in palindromes])
        # rows
        palindromes = find_palindromes(p)
        magic_sum += sum([p * 100 for p in palindromes])
    return magic_sum


def part_2(inp):
    magic_sum = 0
    patterns = read_patterns(inp)
    for p in patterns:
        # cols
        pt = [''.join(e) for e in list(map(list, zip(*p)))]
        palindromes = find_palindromes(pt, False)
        magic_sum += sum([p for p in palindromes])
        # rows
        palindromes = find_palindromes(p, False)
        magic_sum += sum([p * 100 for p in palindromes])
    return magic_sum


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
