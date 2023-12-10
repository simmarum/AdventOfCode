from collections import defaultdict


def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).replace('\n', '') for line in f.readlines()]


def part_1(inp):
    data = list(map(int, inp[0].split()))

    def get_node(data, idx):
        curr_idx = idx
        children_cnt = data[curr_idx]
        curr_idx += 1
        metadata_cnt = data[curr_idx]
        children = []
        all_meta = []
        for _ in range(children_cnt):
            child, new_idx, new_meta = get_node(data, curr_idx + 1)
            children.append(child)
            all_meta.extend(new_meta)
            curr_idx = new_idx
        if metadata_cnt > 0:
            metadata = data[curr_idx + 1:curr_idx + metadata_cnt + 1]
            all_meta.extend(metadata)
        return [children_cnt, children, metadata_cnt,
                metadata], curr_idx + metadata_cnt, all_meta

    nodes, _, all_meta = get_node(data, 0)
    return sum(all_meta)


def part_2(inp):
    data = list(map(int, inp[0].split()))

    def get_node(data, idx):
        curr_idx = idx
        children_cnt = data[curr_idx]
        curr_idx += 1
        metadata_cnt = data[curr_idx]
        children = []
        node_value = 0
        if children_cnt > 0:
            for _ in range(children_cnt):
                child, new_idx = get_node(data, curr_idx + 1)
                children.append(child)
                curr_idx = new_idx
            for meta_idx in data[curr_idx + 1:curr_idx + metadata_cnt + 1]:
                if meta_idx - 1 < len(children):
                    node_value += children[meta_idx - 1]
        else:
            node_value = sum(data[curr_idx + 1:curr_idx + metadata_cnt + 1])

        return node_value, curr_idx + metadata_cnt

    node_value, _ = get_node(data, 0)
    return node_value


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
