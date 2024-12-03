""" Advent of code Year 2024 Day 3 solution
Link to task: https://adventofcode.com/2024/day/3
Author = Averbea
Date = 03/12/2024
"""
import re

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file()
    return file


@timeit
def part_one():
    """Solution for Part 1"""
    memory = process_input()
    matches = re.findall(r"mul\(\d*,\d*\)", memory)
    result = 0
    for match in matches:
        a, b = re.findall(r"\d+", match)
        result += int(a) * int(b)

    return result


@timeit
def part_two():
    """Solution for Part 2"""
    memory = process_input()
    matches = re.findall(r"mul\(\d*,\d*\)|do\(\)|don't\(\)", memory)
    result = 0
    enabled = True
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            a, b = re.findall(r"\d+", match)
            result += int(a) * int(b)

    return result


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
