def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line).strip() for line in f.readlines()]


def part_1(inp):
    image = inp[0]
    area = 25 * 6
    if len(image) % area != 0:
        raise RuntimeError(f"Size of image is wrong! ({len(image) % area=})")
    layers_cnt = len(image) // area
    layers_details = {}
    for layer_id in range(layers_cnt):
        layer = image[layer_id * area:layer_id * area + area]
        layers_details[layer_id] = (
            layer.count('0'),
            layer.count('1') * layer.count('2')
        )
    return min(layers_details.values())[1]


def part_2(inp):
    image = inp[0]
    area = 25 * 6
    decoded_image = ['2'] * area
    for p_idx, pixel in enumerate(image):
        if decoded_image[p_idx % area] == '2':
            decoded_image[p_idx % area] = pixel

    print_lookup = {
        '2': '?',
        '1': '#',
        '0': ' '
    }
    msg = ''
    for p_idx, pixel in enumerate(decoded_image):
        if p_idx % 25 == 0:
            msg += f'\n{print_lookup[pixel]}'
        else:
            msg += print_lookup[pixel]
    return msg


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
