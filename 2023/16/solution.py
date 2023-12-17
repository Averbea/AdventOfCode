""" Advent of code Year 2023 Day 16 solution
Author = Averbea
Date = December 2022
"""

from utils.templateutils import timeit, read_input_file
from tqdm import tqdm

def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    return [[c for c in line] for line in file.splitlines()]


DIRS = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0)
}


def is_in_bounds(grid, pos):
    return 0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0])


def above(cur_pos):
    return cur_pos[0], cur_pos[1] - 1


def below(cur_pos):
    return cur_pos[0], cur_pos[1] + 1


def left(cur_pos):
    return cur_pos[0] - 1, cur_pos[1]


def right(cur_pos):
    return cur_pos[0] + 1, cur_pos[1]


def energy_level(starting_beam, grid):
    seen_beams = set()
    energized = set()
    beams = [starting_beam]
    while beams:
        beam = beams.pop()
        if beam in seen_beams:
            continue
        seen_beams.add(beam)
        cur_pos, cur_dir = beam
        if not is_in_bounds(grid, cur_pos):
            continue
        energized.add(cur_pos)

        continued_pos = (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1])

        cur_symbol = grid[cur_pos[1]][cur_pos[0]]
        match cur_symbol:
            case '.':
                beams.append((continued_pos, cur_dir))
            case '|':
                if cur_dir == (0, 1) or cur_dir == (0, -1):
                    beams.append((continued_pos, cur_dir))
                else:
                    beams.append((above(cur_pos), DIRS['up']))
                    beams.append((below(cur_pos), DIRS['down']))
            case '-':
                if cur_dir == (1, 0) or cur_dir == (-1, 0):
                    beams.append((continued_pos, cur_dir))
                else:
                    beams.append((right(cur_pos), DIRS['right']))
                    beams.append((left(cur_pos), DIRS['left']))
            case '/':
                if cur_dir == (0, 1):
                    beams.append((left(cur_pos), DIRS['left']))
                elif cur_dir == (0, -1):
                    beams.append((right(cur_pos), DIRS['right']))
                elif cur_dir == (1, 0):
                    beams.append((above(cur_pos), DIRS['up']))
                elif cur_dir == (-1, 0):
                    beams.append((below(cur_pos), DIRS['down']))
            case '\\':
                if cur_dir == (0, 1):
                    beams.append((right(cur_pos), DIRS['right']))
                elif cur_dir == (0, -1):
                    beams.append((left(cur_pos), DIRS['left']))
                elif cur_dir == (1, 0):
                    beams.append((below(cur_pos), DIRS['down']))
                elif cur_dir == (-1, 0):
                    beams.append((above(cur_pos), DIRS['up']))
    return len(energized)


@timeit
def part_one():
    """Solution for Part 1"""
    grid = process_input()

    return energy_level(((0, 0), (1, 0)), grid)


@timeit
def part_two():
    """Solution for Part 2"""
    grid = process_input()

    starting_beams = [((i, 0), DIRS['down']) for i in range(len(grid[0]))]
    starting_beams += [((0, i), DIRS['right']) for i in range(len(grid))]
    starting_beams += [((len(grid[0]) - 1, i), DIRS['left']) for i in range(len(grid))]
    starting_beams += [((i, len(grid) - 1), DIRS['up']) for i in range(len(grid[0]))]
    max_energy = 0
    for beam in tqdm(starting_beams):
        max_energy = max(max_energy, energy_level(beam, grid))
    return max_energy


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
