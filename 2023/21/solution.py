""" Advent of code Year 2023 Day 21 solution
Author = Averbea
Date = December 2023
"""

from utils.templateutils import timeit, read_input_file
from tqdm import tqdm




def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=True).splitlines()

    starting_pos = [(idx, line.index('S')) for idx, line in enumerate(file) if 'S' in line][0]
    return file, starting_pos



@timeit
def part_one():
    """Solution for Part 1"""
    grid, starting_pos = process_input()
    steps = 64

    reached_in_steps = {s: set() for s in range(steps+1)}
    reached_in_steps[0].add(starting_pos)
    for step in range(1,steps+1):
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for pos in reached_in_steps[step-1]:
                new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                if new_pos[0] < 0 or new_pos[0] >= len(grid) or new_pos[1] < 0 or new_pos[1] >= len(grid[0]):
                    continue
                if grid[new_pos[0]][new_pos[1]] == '#':
                    continue
                reached_in_steps[step].add(new_pos)
    return len(reached_in_steps[steps])


@timeit
def part_two():
    """Solution for Part 2"""
    grid, starting_pos = process_input()
    steps = 1000

    reached_in_steps = {s: set() for s in range(steps+1)}
    reached_in_steps[0].add(starting_pos)
    for step in tqdm(range(1, steps+1)):
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for pos in reached_in_steps[step-1]:
                new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                if grid[new_pos[0] % len(grid)][new_pos[1]%len(grid[0])] == '#':
                    continue
                reached_in_steps[step].add(new_pos)


    return len(reached_in_steps[steps])


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
