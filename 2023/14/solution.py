""" Advent of code Year 2023 Day 14 solution
Author = Averbea
Date = December 2023
"""
from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False).splitlines()
    # get coordinates of all fixed (#) in file
    fixed = frozenset([(x, y) for y, line in enumerate(file) for x, c in enumerate(line) if c == "#"])
    loose = frozenset([(x, y) for y, line in enumerate(file) for x, c in enumerate(line) if c == "O"])
    grid_size = len(file)
    return fixed, loose, grid_size


def print_grid(fixed, loose, grid_size):
    for line in range(grid_size):
        print("".join(["#" if (x, line) in fixed else "O" if (x, line) in loose else "." for x in range(grid_size)]))


def is_inside_grid(pos, grid_size):
    return 0 <= pos[0] < grid_size and 0 <= pos[1] < grid_size


def step_in_dir(pos, direction):
    return pos[0] + direction[0], pos[1] + direction[1]


def get_load_for_grid(loose, grid_size):
    return sum(grid_size - y for x, y in loose)


def rotate(fixed, loose, grid_size):
    new_fixed = set()
    for f in fixed:
        new_fixed.add((grid_size - 1 - f[1], f[0]))
    new_loose = set()
    for l in loose:
        new_loose.add((grid_size - 1 - l[1], l[0]))
    return frozenset(new_fixed), frozenset(new_loose)


def tilt(fixed, loose, grid_size):
    new_loose = set()
    for y in range(grid_size):
        for x in range(grid_size):
            if y == 0 or (x, y - 1) in fixed:
                next_stone_pos = (x, y)
                cur_pos = (x, y)
                while is_inside_grid(cur_pos, grid_size):
                    if cur_pos in fixed:
                        break
                    if cur_pos in loose:
                        new_loose.add(next_stone_pos)
                        next_stone_pos = step_in_dir(next_stone_pos, (0, 1))

                    cur_pos = step_in_dir(cur_pos, (0, 1))
    return frozenset(new_loose)


@timeit
def part_one():
    """Solution for Part 1"""
    [fixed, loose, grid_size] = process_input()
    loose = tilt(fixed, loose, grid_size)
    # print_grid(fixed, loose, grid_size)
    return get_load_for_grid(loose, grid_size)




@timeit
def part_two():
    """Solution for Part 2"""
    [fixed, loose, grid_size] = process_input()

    seen = {}
    i = 0
    while i < 1_000_000_000:
        if ((fixed, loose) in seen):
            print("found duplicate at " + str(i))
            print("old value : " + str(seen[(fixed, loose)]))
            diff = i - seen[(fixed, loose)]
            print("diff is " + str(diff))
            i += diff * ((1_000_000_000 - i) // diff)
            print("new i is " + str(i))
            seen.clear()

        seen[(fixed, loose)] = i

        i += 1
        for j in range(4):
            loose = tilt(fixed, loose, grid_size)
            [fixed, loose] = rotate(fixed, loose, grid_size)
    return get_load_for_grid(loose, grid_size)


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
