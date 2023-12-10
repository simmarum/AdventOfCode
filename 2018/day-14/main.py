# Used pypy3

def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    recipes_cnt = int(inp[0])
    # recipes_cnt = 2018
    elv_idx_1 = 0
    elv_idx_2 = 1
    all_recipes = [3, 7]
    while len(all_recipes) < recipes_cnt + 10:
        new_solution = (all_recipes[elv_idx_1] + all_recipes[elv_idx_2])
        if new_solution < 10:
            all_recipes.append(new_solution)
        else:
            all_recipes.append(new_solution//10)
            all_recipes.append(new_solution % 10)
        elv_idx_1 = (all_recipes[elv_idx_1]+1+elv_idx_1) % len(all_recipes)
        elv_idx_2 = (all_recipes[elv_idx_2]+1+elv_idx_2) % len(all_recipes)
        # print(all_recipes, elv_idx_1, elv_idx_2)
    return ''.join(map(str, all_recipes[recipes_cnt:recipes_cnt+10]))


def part_2(inp):
    recipes_cnt = str(int(inp[0]))
    elv_idx_1 = 0
    elv_idx_2 = 1
    all_recipes = '37'
    while recipes_cnt not in all_recipes[-8:]:
        all_recipes += str(int(all_recipes[elv_idx_1]) +
                           int(all_recipes[elv_idx_2]))
        l_all_recipes = len(all_recipes)
        elv_idx_1 = (
            elv_idx_1 + int(all_recipes[elv_idx_1]) + 1) % l_all_recipes
        elv_idx_2 = (
            elv_idx_2 + int(all_recipes[elv_idx_2]) + 1) % l_all_recipes
    return all_recipes.index(recipes_cnt)


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
