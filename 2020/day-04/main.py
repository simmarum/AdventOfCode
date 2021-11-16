import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return f.read()


def part_1(inp):
    good_pass = 0
    needed_field = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl',
                        'ecl', 'pid'])  # cid optional
    for d in inp.split("\n\n"):
        tmp_data = set()
        d = d.replace("\n", " ")
        d = ' '.join(d.split())
        for one_val in d.split(" "):
            tmp_data.add(one_val.split(":")[0])
        if needed_field.issubset(tmp_data):
            good_pass += 1

    return good_pass


def _check_pass(pass_dict):
    needed_field = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl',
                        'ecl', 'pid'])  # cid optional
    if not needed_field.issubset(set(pass_dict.keys())):
        return False
    if (int(pass_dict['byr']) < 1920) or ((int(pass_dict['byr']) > 2002)):
        return False
    if (int(pass_dict['iyr']) < 2010) or ((int(pass_dict['iyr']) > 2020)):
        return False
    if (int(pass_dict['eyr']) < 2020) or ((int(pass_dict['eyr']) > 2030)):
        return False
    if "in" in pass_dict['hgt']:
        tmp_hgt = int(pass_dict['hgt'].replace("in", ""))
        if (tmp_hgt < 59) or (tmp_hgt > 76):
            return False
    elif "cm" in pass_dict['hgt']:
        tmp_hgt = int(pass_dict['hgt'].replace("cm", ""))
        if (tmp_hgt < 150) or (tmp_hgt > 193):
            return False
    else:
        return False
    p = re.compile(r'^#[0-9a-f]{6}$')
    m = p.match(pass_dict['hcl'])
    if m:
        pass
    else:
        return False
    if pass_dict['ecl'] not in [
            'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    p = re.compile(r'^[0-9]{9}$')
    m = p.match(pass_dict['pid'])
    if m:
        pass
    else:
        return False

    return True


def part_2(inp):
    good_pass = 0
    for d in inp.split("\n\n"):
        tmp_data = {}
        d = d.replace("\n", " ")
        d = ' '.join(d.split())
        for one_val in d.split(" "):
            tmp_data[one_val.split(":")[0]] = one_val.split(":")[1]
        x = _check_pass(tmp_data)
        if x:
            good_pass += 1

    return good_pass


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
