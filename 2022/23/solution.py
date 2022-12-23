""" Advent of code Year 2022 Day 23 solution
Author = Averbea
Date = December 2022
"""


from collections import defaultdict
import os
from time import time


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read().splitlines()

    elve_positions = set()
    for row, line in enumerate(inputs):
        for column, char in enumerate(line):
            if char == '#':
                elve_positions.add((row, column))

    return elve_positions


def calc_round(elves, directions):
    """calculate a round given elves and directions. Return elves and if any elf moved"""
    any_elf_moved = False
    # proposed[(row, column)] stores all elves that want to move there
    proposed = defaultdict(list)
    for (row, col) in elves:

        has_neighbor = False
        for diff_row in [-1, 0, 1]:
            for diff_col in [-1, 0, 1]:
                if (diff_row != 0 or diff_col != 0) and (row + diff_row, col + diff_col) in elves:

                    has_neighbor = True

        if not has_neighbor:
            # do nothing
            continue
        for direction in directions:
            if direction == 'N' and \
            (row - 1, col - 1) not in elves and \
            (row - 1, col) not in elves and \
            (row - 1, col + 1) not in elves:
                proposed[(row-1, col)].append((row, col))
                break
            elif direction == 'S' and \
            (row + 1, col - 1) not in elves and \
            (row + 1, col) not in elves and \
            (row + 1, col + 1) not in elves:
                proposed[(row+1, col)].append((row, col))
                break
            elif direction == 'W' and \
            (row - 1, col - 1) not in elves and \
            (row, col - 1) not in elves and \
            (row + 1, col - 1) not in elves:
                proposed[(row, col - 1)].append((row, col))
                break
            elif direction == 'E' and \
            (row - 1, col + 1) not in elves and \
            (row, col + 1) not in elves and \
            (row + 1, col + 1) not in elves:
                proposed[(row, col+1)].append((row, col))
                break

    for key, val in proposed.items():
        if len(val) == 1:
            any_elf_moved = True
            elves.discard(val[0])
            elves.add(key)

    return elves, any_elf_moved


def print_grid(elves: set[tuple]):
    """print the grid"""
    min_row = min(row for (row, col) in elves)
    max_row = max(row for (row, col) in elves)
    min_col = min(col for (row, col) in elves)
    max_col = max(col for (row, col) in elves)

    print("min_r", min_row, "max_row", max_row)
    print("min_c", min_col, "max_c", max_col)
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if (row, col) in elves:
                print('#', end="")
            else:
                print('.', end="")
        print("")
    print("")


def sum_free(elves):
    """calculate the sum of free fields"""
    min_row = min(row for (row, col) in elves)
    max_row = max(row for (row, col) in elves)
    min_col = min(col for (row, col) in elves)
    max_col = max(col for (row, col) in elves)
    to_ret = 0
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if (row, col) not in elves:
                to_ret += 1
    return to_ret


def part_one():
    """Solution for Part 1"""
    elves = parse_input()
    # print("== INITIAL STATE ==")
    # print_grid(elves)

    directions = ['N', 'S', 'W', 'E']
    for _ in range(1, 11):
        elves, _ = calc_round(elves, directions)
        directions = directions[1:] + [directions[0]]
        # print("== End of Round ", i, "==")
        # print_grid(elves)

    return sum_free(elves)


def part_two():
    """Solution for Part 2"""
    elves = parse_input()
    directions = ['N', 'S', 'W', 'E']
    any_moved = True
    planting_round = 0
    while any_moved:
        planting_round += 1
        elves, any_moved = calc_round(elves, directions)
        directions = directions[1:] + [directions[0]]
        # print("== End of Round ", i, "==")
        # print_grid(elves)

    return planting_round


def main():
    """main method"""
    time_needed, result = measure_timing(part_one)

    print("Part One : " + str(result))
    print("time elapsed: " + str(time_needed))

    time_needed, result = measure_timing(part_two)
    print("\nPart Two : " + str(result))
    print("time elapsed: " + str(time_needed))


if __name__ == "__main__":
    main()
