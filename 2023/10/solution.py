""" Advent of code Year 2023 Day 10 solution
Author = Averbea
Date = December 2023
"""

from utils.tenplateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False).splitlines()
    return [[c for c in line] for line in file]


def next_direction(symbol, from_dir):
    lookup = {
        '|': ['above', 'below'],
        '-': ['left', 'right'],
        'L': ['above', 'right'],
        'J': ['above', 'left'],
        '7': ['below', 'left'],
        'F': ['below', 'right'],
    }
    adjacent = lookup[symbol]
    if from_dir not in adjacent:
        raise ValueError(f"from_dir {from_dir} not in adjacent {adjacent}")
    return adjacent[0] if adjacent[0] != from_dir else adjacent[1]


def next_position(grid, pos, previous):
    """returns the next position"""
    dirs = {
        'above': (0, -1),
        'below': (0, 1),
        'left': (-1, 0),
        'right': (1, 0),
    }
    # calculate offset of pos from previous
    offset = tuple(map(lambda x, y: y - x, pos, previous))
    from_dir = [k for k, v in dirs.items() if v == offset][0]

    cur_symbol = grid[pos[1]][pos[0]]
    next_dir = next_direction(cur_symbol, from_dir)
    next_pos = tuple(map(lambda x, y: x + y, pos, dirs[next_dir]))
    return next_pos


def find_loop(grid):
    start_position = [(j, i) for i, row in enumerate(grid) for j, c in enumerate(row) if c == "S"][0]
    cur_position = (start_position[0], start_position[1] + 1)
    loop_positions = [start_position, cur_position]
    while cur_position != start_position:
        cur_position = next_position(grid, cur_position, loop_positions[-2])
        loop_positions.append(cur_position)
    loop_positions = loop_positions[:-1]  # start position is repeated at the end
    return loop_positions


@timeit
def part_one():
    """Solution for Part 1"""
    grid = process_input()
    loop = find_loop(grid)
    return len(loop)


@timeit
def part_two():
    """Solution for Part 2"""
    grid = process_input()
    loop = find_loop(grid)
    count = 0
    # iterate through 2d grid
    for y, row in enumerate(grid):
        inside = False
        start_wall_up = False
        start_wall_down = False
        for x, symbol in enumerate(row):
            if (x, y) in loop:
                # one has to differentiate between F J  or 7 L (counts as wall) and F7 or LJ (does not count as wall)
                match symbol:
                    case '|':
                        inside = not inside
                    case 'L':
                        start_wall_up = True
                    case 'F':
                        start_wall_down = True
                    case 'S':  # this has been looked up in input data manually
                        start_wall_down = True
                    case 'J':
                        if start_wall_up:
                            start_wall_up = False
                        if start_wall_down:
                            start_wall_down = False
                            inside = not inside
                    case '7':
                        if start_wall_up:
                            start_wall_up = False
                            inside = not inside
                        if start_wall_down:
                            start_wall_down = False
            elif inside:
                # all elements enclosed by loop that are not part of main loop can be counted as inside
                count += 1
    return count


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
