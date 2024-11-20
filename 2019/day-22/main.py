def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def shuffle_card(deck, instructions):
    deck_size = len(deck)
    for instr in instructions:
        instr_arr = instr.split()
        if instr.startswith("deal with increment"):
            incr = int(instr_arr[-1])
            deck_prev = deck.copy()
            for deck_pos, curr_pos in enumerate(
                    range(0, incr * deck_size, incr)):
                deck[curr_pos % deck_size] = deck_prev[deck_pos]
        if instr.startswith("deal into new stack"):
            deck = deck[::-1]
        if instr.startswith("cut"):
            cut = int(instr_arr[-1])
            deck = deck[cut:] + deck[:cut]
    return deck


def part_1(inp):
    deck_size = 10007
    deck = list(range(deck_size))
    deck = shuffle_card(deck, inp)
    return deck.index(2019)


def simulate_shuffle_card_for_position(
        deck_size, position, instructions):
    curr_pos = position
    for instr in reversed(instructions):
        instr_arr = instr.split()
        if instr.startswith("deal with increment"):
            incr = int(instr_arr[-1])
            curr_pos = pow(incr, -1, deck_size) * curr_pos % deck_size
        if instr.startswith("deal into new stack"):
            curr_pos = deck_size - 1 - curr_pos
        if instr.startswith("cut"):
            cut = int(instr_arr[-1])
            curr_pos = (curr_pos + cut + deck_size) % deck_size
    return curr_pos


def part_2(inp):
    deck_size = 119315717514047
    repeats = 101741582076661
    position = 2020
    position_1 = simulate_shuffle_card_for_position(
        deck_size=deck_size,
        position=position,
        instructions=inp
    )
    position_2 = simulate_shuffle_card_for_position(
        deck_size=deck_size,
        position=position_1,
        instructions=inp
    )
    a = (position_1 - position_2) * pow(position - position_1 + deck_size, -1, deck_size) % deck_size  # noqa
    b = (position_1 - a * position) % deck_size
    res = (pow(a, repeats, deck_size) * position + (pow(a, repeats,
           deck_size) - 1) * pow(a - 1, -1, deck_size) * b) % deck_size

    return res


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
