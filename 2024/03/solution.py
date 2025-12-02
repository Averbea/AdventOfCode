""" Advent of code Year 2024 Day 3 solution
Link to task: https://adventofcode.com/2024/day/3
Author = Averbea
Date = 03/12/2024
"""
import re

from utils.templateutils import timeit, read_input_file


def process_input(input_data):
    """parses the input file and returns the result"""
    return input_data


@timeit
def part_one(input_data):
    """Solution for Part 1"""
    memory = process_input(input_data)
    matches = re.findall(r"mul\(\d*,\d*\)", memory)
    result = 0
    for match in matches:
        a, b = re.findall(r"\d+", match)
        result += int(a) * int(b)

    return result


@timeit
def part_two(input_data):
    """Solution for Part 2"""
    memory = process_input(input_data)
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
    file_content = read_input_file()
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

