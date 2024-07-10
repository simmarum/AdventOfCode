from copy import deepcopy
from collections import deque
import math


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def get_rules(inp):
    rules = {}
    for line in inp:
        if not line:
            continue
        name, dest = line.split(">")
        name = name[:-1].strip()
        dest = [c.strip() for c in dest.strip().split(",")]
        rules[name] = dest
    return rules


def get_initial_state(rules):
    states = {}
    for k in rules.keys():
        if k.startswith("%"):
            states[k[1:]] = False
        if k.startswith("&"):
            tmp_input = {}
            for k1, v1 in rules.items():
                if k[1:] in v1:
                    tmp_input.update({k1[1:]: False})
            states[k[1:]] = tmp_input
    return states


def send_pulse(rules, button_click, cycle_max_len):
    initial_states = get_initial_state(rules)
    curr_state = get_initial_state(rules)
    cycle_len = None
    signal_cnt = {True: 0, False: 0}
    signal_cnt_cycle = {}
    for i in range(1, cycle_max_len):
        stack = [(str("button"), bool(False), str("broadcaster"))]
        while stack:
            source, signal, dest = stack.pop(0)
            signal_cnt[signal] += 1
            if dest == 'broadcaster':
                for r in rules[dest]:
                    stack.append((dest, signal, r))
            elif f"%{dest}" in rules:
                pulse = None
                if not signal and curr_state[dest]:
                    pulse = False
                    curr_state[dest] = False
                elif not signal and not curr_state[dest]:
                    pulse = True
                    curr_state[dest] = True
                if pulse is not None:
                    for r in rules[f"%{dest}"]:
                        stack.append((dest, pulse, r))
            elif f"&{dest}" in rules:
                curr_state[dest][source] = signal
                pulse = not all(list(curr_state[dest].values()))
                for r in rules[f"&{dest}"]:
                    stack.append((dest, pulse, r))
        signal_cnt_cycle[i] = deepcopy(signal_cnt)
        if initial_states == curr_state:
            cycle_len = i
            break
    signal_cnt_cycle[0] = {True: 0, False: 0}
    if cycle_len:
        full_cycle_cnt = button_click // cycle_len
        part_cycle_cnt = button_click % cycle_len
    else:
        full_cycle_cnt = 0
        part_cycle_cnt = button_click
    signals_true = (
        full_cycle_cnt * signal_cnt[True]) + (signal_cnt_cycle[part_cycle_cnt][True])
    signals_false = (
        full_cycle_cnt * signal_cnt[False]) + (signal_cnt_cycle[part_cycle_cnt][False])
    return signals_true * signals_false


def how_many_clicks_for_rx(inp, max_button_push):
    graph = {}
    flip_flop = {}
    memory = {}
    for line in inp:
        if not line:
            continue
        source, destinations = line.split(' -> ')
        destinations = destinations[:-1].split(', ')
        graph[source.lstrip('%&')] = destinations
        if source.startswith('%'):
            flip_flop[source[1:]] = False
        elif source.startswith('&'):
            memory[source[1:]] = {}

    for conjunction in memory.keys():
        for source, dest in graph.items():
            if conjunction in dest:
                memory[conjunction][source] = False

    final_layer = [m1 for m1 in graph if 'rx' in graph[m1]]
    assert len(
        final_layer) == 1, "Assumption #1: There is only 1 module pointing to rx"
    assert final_layer[0] in memory, "Assumption #2: The final module before rx is a conjunction"

    semi_final_layer = set(
        module for module in graph if final_layer[0] in graph[module])
    # Assumption #3: The modules on semi_final_layer signal high in regular
    # intervals / cycles
    cycle_lengths = []
    for button_push in range(1, max_button_push):
        queue = deque([(str('broadcaster'), False, in_module)
                      for in_module in graph['broadcaster']])
        while queue:
            out_module, signal, in_module = queue.popleft()

            if in_module in flip_flop and signal == 0:
                flip_flop[in_module] = not flip_flop[in_module]
                out_signal = flip_flop[in_module]

            elif in_module in memory:
                memory[in_module][out_module] = signal
                out_signal = not all(list(memory[in_module].values()))
                if in_module in semi_final_layer and out_signal:
                    cycle_lengths.append(button_push)
                    semi_final_layer.remove(in_module)
            else:
                continue

            queue.extend([(in_module, out_signal, nxt)
                         for nxt in graph[in_module]])

        if not semi_final_layer:
            break
    return math.lcm(*cycle_lengths)


def part_1(inp):
    rules = get_rules(inp)
    return send_pulse(rules, 1000, 1010)


def part_2(inp):
    return how_many_clicks_for_rx(inp, 10_000)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
