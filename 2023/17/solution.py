""" Advent of code Year 2023 Day 17 solution
Author = Averbea
Date = December 2023
"""

from utils.templateutils import timeit, read_input_file
from queue import PriorityQueue


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    return [[int(num) for num in line] for line in file.splitlines()]


def is_in_grid(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def print_path(grid, path, with_numbers=False):
    sym = {
        (0, 1): 'v',
        (0, -1): '^',
        (1, 0): '>',
        (-1, 0): '<'
    }
    g = [[str(num) if with_numbers else '.' for num in line] for line in grid]
    for x, y, x_dir, y_dir in path:
        g[y][x] = sym[(x_dir, y_dir)]
    for line in g:
        print(''.join(line))


def solve(grid, max_steps, min_steps):
    open_list = PriorityQueue()
    #           cost, pos, direction, steps moved in that direction
    start_item = (0, 0, 0, 0, 0, 0, [])
    open_list.put(start_item)
    target = (len(grid[0]) - 1, len(grid) - 1)
    seen = set()

    while not open_list.empty():
        heat_loss, x, y, x_dir, y_dir, steps, path = open_list.get()

        if (x, y) == target and steps >= min_steps:
            return heat_loss, path

        if (x, y, x_dir, y_dir, steps) in seen:
            continue
        seen.add((x, y, x_dir, y_dir, steps))

        for new_x_dir, new_y_dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x = x + new_x_dir
            next_y = y + new_y_dir
            if not is_in_grid(next_x, next_y, grid):
                continue
            new_heat_loss = heat_loss + grid[next_y][next_x]
            new_path = path + [(next_x, next_y, new_x_dir, new_y_dir)]

            if new_x_dir == -x_dir and new_y_dir == -y_dir:
                continue
            elif new_x_dir == x_dir and new_y_dir == y_dir:
                if steps < max_steps:
                    open_list.put((new_heat_loss, next_x, next_y, new_x_dir, new_y_dir, steps + 1, new_path))
            else:
                if steps >= min_steps or x_dir == 0 and y_dir == 0:
                    open_list.put((new_heat_loss, next_x, next_y, new_x_dir, new_y_dir, 1, new_path))

    return 0


@timeit
def part_one():
    """Solution for Part 1"""
    grid = process_input()
    heat_loss, path = solve(grid, 3, 1)
    print_path(grid, path)
    return heat_loss


@timeit
def part_two():
    """Solution for Part 2"""
    grid = process_input()
    heat_loss, path = solve(grid, 10, 4)
    print_path(grid, path)
    return heat_loss


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
