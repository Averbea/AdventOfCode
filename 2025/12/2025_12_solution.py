""" Advent of code Year 2025 Day 12 solution
Link to task: https://adventofcode.com/2025/day/12
Author = Averbea
Date = 13/12/2025
"""
import re

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    forms = re.findall(r"\d:\n([#.]*)\n([#.]*)\n([#.]*)", input_data)
    lines = re.findall(r"(\d+)x(\d+): ([\d+\s]*)\n", input_data)
    lines = [[(int(line[0]), int(line[1])),  list(map(int, line[2].split(" ")))] for line in lines]
    return forms, lines


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    forms, lines = process_input(input_data)
    can_fit = 0
    for (dimx, dimy), counts in lines:
        total_space_needed = sum(counts) * 9
        space_present = dimx * dimy
        if total_space_needed > space_present:
            continue
        can_fit += 1

    return can_fit


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""

    # No part 2 for this day :)
    return 0


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

