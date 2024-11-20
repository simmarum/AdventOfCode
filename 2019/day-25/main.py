import random
from itertools import chain, combinations
import re


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def infinite_zeros():
    while True:
        yield 0


INPUTS = infinite_zeros()


def search_droid(int_code):

    def _mode_dec_r(int_code, mode, value, relative_base):
        if mode == '0':
            return int_code[value]
        elif mode == '1':
            return value
        elif mode == '2':
            return int_code[value + relative_base]
        else:
            raise RuntimeError(f"Wrong {mode=}")

    def _mode_dec_w(mode, value, relative_base):
        if mode == '0':
            return value
        elif mode == '2':
            return value + relative_base
        else:
            raise RuntimeError(f"Wrong {mode=}")

    relative_base = 0
    ip = 0
    while True:
        opp_code = int_code[ip]
        opp_code_str = f"{opp_code:05d}"
        opp_code = int(opp_code_str[-2:])
        ip_inc = 0
        if opp_code == 1:
            a, b, c = int_code[ip + 1], int_code[ip + 2], int_code[ip + 3]
            ip_inc = 4
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            p3 = _mode_dec_w(opp_code_str[-5], c, relative_base)
            int_code[p3] = p1 + p2
        elif opp_code == 2:
            a, b, c = int_code[ip + 1], int_code[ip + 2], int_code[ip + 3]
            ip_inc = 4
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            p3 = _mode_dec_w(opp_code_str[-5], c, relative_base)
            int_code[p3] = p1 * p2
        elif opp_code == 3:
            a = int_code[ip + 1]
            ip_inc = 2
            p1 = _mode_dec_w(opp_code_str[-3], a, relative_base)
            int_code[p1] = next(INPUTS)
        elif opp_code == 4:
            a = int_code[ip + 1]
            ip_inc = 2
            yield _mode_dec_r(int_code, opp_code_str[-3], a, relative_base), int_code
        elif opp_code == 5:
            a, b = int_code[ip + 1], int_code[ip + 2]
            ip_inc = 3
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            if p1 != 0:
                ip = p2
                ip_inc = 0
        elif opp_code == 6:
            a, b = int_code[ip + 1], int_code[ip + 2]
            ip_inc = 3
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            if p1 == 0:
                ip = p2
                ip_inc = 0
        elif opp_code == 7:
            a, b, c = int_code[ip + 1], int_code[ip + 2], int_code[ip + 3]
            ip_inc = 4
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            p3 = _mode_dec_w(opp_code_str[-5], c, relative_base)
            int_code[p3] = int(p1 < p2)
        elif opp_code == 8:
            a, b, c = int_code[ip + 1], int_code[ip + 2], int_code[ip + 3]
            ip_inc = 4
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            p2 = _mode_dec_r(int_code, opp_code_str[-4], b, relative_base)
            p3 = _mode_dec_w(opp_code_str[-5], c, relative_base)
            int_code[p3] = int(p1 == p2)
        elif opp_code == 9:
            a = int_code[ip + 1]
            ip_inc = 2
            p1 = _mode_dec_r(int_code, opp_code_str[-3], a, relative_base)
            relative_base += p1

        elif opp_code == 99:
            ip_inc = 1
            # raise StopIteration()
            break
        else:
            raise RuntimeError(f"Found new {opp_code=}")
        ip += ip_inc


def create_ship_map(ship_map, msg, curr_pos):
    useless_msgs = [
        "You can't go that way.",
        "Items in your inventory",
        "You aren't carrying any items",
        "You can't move!!"
    ]

    if any(m in msg for m in useless_msgs):
        return ship_map
    if "You take the" in msg:
        msg = msg.strip().split("\n\n")
        item_name = msg[0][13:-1].strip()
        ship_map[curr_pos]['item_name'].remove(item_name)
        return ship_map
    if "==" in msg:
        msg = msg.strip().split("\n\n")
        room_name, room_description = msg[0].split("\n")
    item_name = None
    if len(msg) == 4:
        item_name = [i[2:] for i in msg[2].strip().split("\n")[1:]]
    if curr_pos not in ship_map:
        ship_map[curr_pos] = {
            'room_code': chr(len(ship_map) + ord('A')),
            'room_name': room_name,
            'room_description': room_description,
            'item_name': item_name,
        }
    else:
        ship_map[curr_pos] = {
            'room_code': ship_map[curr_pos]['room_code'],
            'room_name': room_name,
            'room_description': room_description,
            'item_name': item_name,
        }

    return ship_map


def run_search_droid_part_1(
        source_code_orig, max_iter):
    global INPUTS
    search_droid_instance = search_droid(source_code_orig[:])
    int_code = source_code_orig[:]
    room_name = None
    bad_item = [
        "giant electromagnet",
        "molten lava",
        "escape pod",
        "infinite loop",
        "photons",
    ]
    good_item = [
        'klein bottle',
        'cake',
        'monolith',
        'fuel cell',
        'astrolabe',
        'dark matter',
        'tambourine',
        'mutex'
    ]
    have_all_items = False
    inventory = []
    msg = ""
    for iter in range(max_iter):
        try:
            while True:
                status, int_code = next(search_droid_instance)
                msg += chr(status)
                if msg.endswith('Command?\n'):
                    break
            # print(msg)
            msg_arr = msg.strip().splitlines()
            if " =" in msg_arr[0]:
                room_name = msg_arr[0].strip(" =")

            room_doors = []
            try:
                room_doors_idx = msg_arr.index("Doors here lead:") + 1
                while True:
                    room_door = msg_arr[room_doors_idx].strip("- ")
                    if room_door:
                        room_doors.append(room_door)
                    else:
                        break
                    room_doors_idx += 1
            except ValueError:
                pass

            room_items = []
            try:
                room_items_idx = msg_arr.index("Items here:") + 1
                while True:
                    room_item = msg_arr[room_items_idx].strip("- ")
                    if room_item:
                        if room_item not in bad_item:
                            room_items.append(room_item)
                    else:
                        break
                    room_items_idx += 1
            except ValueError:
                pass

            try:
                taken_room_item = [
                    s for s in msg_arr if s.startswith("You take the ")]
                if taken_room_item:
                    taken_room_item = taken_room_item[0][13:-1]
                    room_items.remove(taken_room_item)
                    inventory.append(taken_room_item)
                    if len(inventory) == len(good_item):
                        have_all_items = True
            except ValueError:
                pass

            if room_name == 'Security Checkpoint':
                if not have_all_items:
                    room_doors = ['east']
                else:
                    # print("Have all items - try every combination....")
                    previous_items_to_drop = []
                    for items_to_drop in chain(*map(lambda x: combinations(inventory, x), range(0, len(inventory) + 1))):  # noqa
                        for item_to_take in previous_items_to_drop:
                            tmp_input_str = f"take {item_to_take}\n"
                            INPUTS = (ord(c) for c in tmp_input_str)
                            msg = ""
                            while True:
                                status, _ = next(search_droid_instance)
                                msg += chr(status)
                                if msg.endswith('Command?\n'):
                                    break

                        for item_to_drop in items_to_drop:
                            tmp_input_str = f"drop {item_to_drop}\n"
                            INPUTS = (ord(c) for c in tmp_input_str)
                            msg = ""
                            while True:
                                status, _ = next(search_droid_instance)
                                msg += chr(status)
                                if msg.endswith('Command?\n'):
                                    break

                        previous_items_to_drop = items_to_drop

                        tmp_input_str = "north\n"
                        INPUTS = (ord(c) for c in tmp_input_str)
                        msg = ""
                        while True:
                            status, _ = next(search_droid_instance)
                            msg += chr(status)
                            if msg.endswith('Command?\n'):
                                break
                            if msg.endswith(
                                    'the keypad at the main airlock."\n'):
                                break
                        if "Alert!" not in msg:
                            return re.findall(
                                r'get in by typing (\d+) on the keypad at the main airlock', msg)[0]
                    return []
            tmp_input_str = ""
            take_item = False
            for room_item in room_items:
                take_item = True
                tmp_input_str += f"take {room_item}\n"
            if tmp_input_str == "":
                next_dir = random.choice(room_doors)
                tmp_input_str += f"{next_dir}\n"

            INPUTS = (ord(c) for c in tmp_input_str)
            if not take_item:
                msg = ""
        except StopIteration:
            return None
    return inventory


def part_1(inp):
    source_code_orig = list(map(int, inp[0].split(','))) + [0] * 5000
    max_iter = 10000
    password = run_search_droid_part_1(source_code_orig, max_iter)
    return password


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
