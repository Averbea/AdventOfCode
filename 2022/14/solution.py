""" Advent of code Year 2022 Day 14 solution
Author = Averbea
Date = December 2022
"""


import os
import re
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

    paths = []
    for line in inputs:
        items = re.findall(r"(\d*),(\d*)", line)
        items = list(map(lambda item: (int(item[0]), int(item[1])), items))
        paths.append(items)

    return paths


def get_all_positions(path: list[tuple[int, int]]) -> set[tuple[int, int]]:
    """get all elements for given path as set"""
    positions = set()
    index = 1
    while index < len(path):
        cur_x, cur_y = path[index]
        prev_x, prev_y = path[index-1]

        start_x = prev_x
        end_x = cur_x
        start_y = prev_y
        end_y = cur_y

        if start_x > end_x:
            start_x, end_x = end_x, start_x
        if start_y > end_y:
            start_y, end_y = end_y, start_y

        for y_pos in range(start_y, end_y + 1):
            for x_pos in range(start_x, end_x+1):
                positions.add((x_pos, y_pos))
        index += 1
    return positions


def get_new_sand(blocked: set[tuple[int, int]], sand_start: tuple[int, int], max_y: int, block_on_floor=False) -> tuple[int, int]:
    """get new sand positions considering blocked positions

    sand is starting from sand_start, max_y is lowest blocked
    """
    x_pos, y_pos = sand_start
    while y_pos < max_y:
        if (x_pos, y_pos + 1) not in blocked:
            if y_pos+1 == max_y:
                break
            y_pos += 1
            continue

        if (x_pos - 1, y_pos + 1) not in blocked:
            y_pos += 1
            x_pos -= 1
            continue

        if (x_pos+1, y_pos+1) not in blocked:
            y_pos += 1
            x_pos += 1
            continue

        # every way is blocked
        return (x_pos, y_pos)

    if block_on_floor:
        return (x_pos, y_pos)


def get_max_y(stones, there_is_a_floor: bool):
    """get the maximum y position

        if there is a floor return floor y position, else the position of the rock with highest y position
    """
    max_y = 0
    for _, stone_y in stones:
        max_y = max(max_y, stone_y)

    if there_is_a_floor:
        return max_y + 2
    return max_y


def part_one():
    """Solution for Part 1"""
    paths = parse_input()

    sand = set()
    stones = set()

    for path in paths:
        positions = get_all_positions(path)
        stones.update(positions)

    max_y = get_max_y(stones, False)
    # there will be nothing to block sand with y > max_y

    sand_start = (500, 0)
    while True:
        new_sand = get_new_sand(stones.union(sand), sand_start, max_y)
        if new_sand is None:
            break
        sand.add(new_sand)
    print_sand(stones, sand, 480, 510, 0, 20)
    return len(sand)


def print_sand(stones, sand, start_x, end_x, start_y, end_y, block_bottom=False):
    """visualize stones and sand in frame start_x, start_y to end_x, end_y

    if block_bottom is set draw a bottom """
    for y_pos in range(start_y, end_y+1):
        line = ""
        for x_pos in range(start_x, end_x + 1):
            if (x_pos, y_pos) in stones:
                line = line + "#"
            elif (x_pos, y_pos) in sand:
                line = line + "O"
            else:
                line = line + "."
        print(line)
    if block_bottom:
        print('#' * (end_x - start_x))


def part_two():
    """Solution for Part 2"""
    paths = parse_input()

    sand = set()
    stones = set()

    for path in paths:
        positions = get_all_positions(path)
        stones.update(positions)

    max_y = get_max_y(stones, True)
    # there will be nothing to block sand with y > max_y

    sand_start = (500, 0)
    while True:
        new_sand = get_new_sand(stones.union(sand), sand_start, max_y, True)
        if new_sand == sand_start:
            # sand output is blocked
            sand.add(new_sand)
            break
        elif new_sand is None:
            # sand is in abyss
            break
        sand.add(new_sand)
    print_sand(stones, sand, 470, 530, 0, 20, True)
    return len(sand)


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
