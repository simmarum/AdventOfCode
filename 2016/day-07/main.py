from operator import xor
import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def find_palindrom_4(s):
    for i in range(0, len(s) - 3):
        if (s[i] != s[i + 1]) and (s[i] ==
                                   s[i + 3]) and (s[i + 1] == s[i + 2]):
            return True
    return False


def part_1(inp):
    good_ips = 0
    for line in inp:
        line_words = []
        tmp_word = ''
        for c in line:
            if c == '[':
                line_words.append((True, tmp_word))
                tmp_word = ''
            elif c == ']':
                line_words.append((False, tmp_word))
                tmp_word = ''
            else:
                tmp_word += c
        line_words.append((True, tmp_word))
        new_line_word = []
        for word in line_words:
            has_palindrom = find_palindrom_4(word[1])
            good_combination = not(xor(has_palindrom, word[0]))
            new_line_word.append((word[0], word[1], good_combination))
        if any([word[2] for word in new_line_word if word[0] is True]) and all(
                [word[2] for word in new_line_word if word[0] is False]):
            good_ips += 1

    return good_ips


def find_all_palindrom_3(s):
    palindromes = []
    for i in range(0, len(s) - 2):
        if (s[i] != s[i + 1]) and (s[i] == s[i + 2]):
            palindromes.append(s[i:i + 3])
    return palindromes


def part_2(inp):
    good_ips = 0
    for line in inp:
        line_words = []
        tmp_word = ''
        for c in line:
            if c == '[':
                line_words.append((True, tmp_word))
                tmp_word = ''
            elif c == ']':
                line_words.append((False, tmp_word))
                tmp_word = ''
            else:
                tmp_word += c
        line_words.append((True, tmp_word))
        new_line_word = []
        for word in line_words:
            find_pal = find_all_palindrom_3(word[1])
            new_line_word.append((word[0], word[1], find_pal))
        aba = [word[2] for word in new_line_word if word[0] is True]
        aba = [item for sublist in aba for item in sublist]
        bab = [word[2] for word in new_line_word if word[0] is False]
        bab = [item for sublist in bab for item in sublist]
        has_ssl = False
        for a in aba:
            tmp_aba = a[1] + a[0] + a[1]
            if tmp_aba in bab:
                has_ssl = True
                break
        if has_ssl is True:
            good_ips += 1

    return good_ips


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
