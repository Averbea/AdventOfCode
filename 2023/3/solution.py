""" Advent of code Year 2023 Day 3 solution
Author = Averbea
Date = December 2023
"""

import os
import re
from time import time


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end - time_start, result


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read()
    return inputs.splitlines()


def is_adjacent_to_symbol(engine_schematic, line_idx, start_col_idx, end_col_idx):
    line_length = len(engine_schematic[line_idx])
    for x in range(max(start_col_idx - 1, 0), min(end_col_idx + 2, line_length)):
        if line_idx > 0 and isSymbol(engine_schematic[line_idx - 1][x]):
            return True
        if line_idx < len(engine_schematic) - 1 and isSymbol(engine_schematic[line_idx + 1][x]):
            return True
    if start_col_idx > 0 and isSymbol(engine_schematic[line_idx][start_col_idx - 1]):
        return True

    if end_col_idx < line_length - 1 and isSymbol(engine_schematic[line_idx][end_col_idx + 1]):
        return True
    return False


def isSymbol(x):
    return x != '.' and not x.isdigit()


def get_adjacent_symbols(engine_schematic, line_idx, number):
    line_length = len(engine_schematic[line_idx])
    start_col_idx = engine_schematic[line_idx].find(number)
    end_col_idx = start_col_idx + len(number) - 1
    adjacent_symbols = []
    for x in range(max(start_col_idx - 1, 0), min(end_col_idx + 2, line_length)):
        if line_idx > 0 and isSymbol(engine_schematic[line_idx - 1][x]):
            adjacent_symbols.append(engine_schematic[line_idx - 1][x])
        if line_idx < len(engine_schematic) - 1 and isSymbol(engine_schematic[line_idx + 1][x]):
            adjacent_symbols.append(engine_schematic[line_idx + 1][x])
    if start_col_idx > 0 and isSymbol(engine_schematic[line_idx][start_col_idx - 1]):
        adjacent_symbols.append(engine_schematic[line_idx][start_col_idx - 1])
    if end_col_idx < line_length - 1 and isSymbol(engine_schematic[line_idx][end_col_idx + 1]):
        adjacent_symbols.append(engine_schematic[line_idx][end_col_idx + 1])
    return adjacent_symbols


def part_one():
    """Solution for Part 1"""
    engine_schematic = parse_input()
    part_numbers = []
    for line_idx, line in enumerate(engine_schematic):
        numbers = re.finditer(r'\d+', line)
        for number in numbers:
            if is_adjacent_to_symbol(engine_schematic, line_idx, number.start(), number.end() - 1):
                part_numbers.append(int(number.group()))
    return sum(part_numbers)


def get_adjacent_numbers(engine_schematic, line_idx, col_idx):
    adjacent_numbers = []
    for line in range(max(0, line_idx-1), min(line_idx + 1, len(engine_schematic))+1):
        numbers = re.finditer(r'\d+', engine_schematic[line])
        for number in numbers:
            if col_idx in range(number.start()-1, number.end()+1):
                adjacent_numbers.append(int(number.group()))
    return adjacent_numbers


def part_two():
    """Solution for Part 2"""
    engine_schematic = parse_input()
    sum_of_gear_ratios = 0
    for line_idx, line in enumerate(engine_schematic):
        for col_idx, col in enumerate(line):
            if col == '*':
                adjacent_nums = get_adjacent_numbers(engine_schematic, line_idx, col_idx)
                if len(adjacent_nums) == 2:
                    gear_ratio = adjacent_nums[0] * adjacent_nums[1]
                    sum_of_gear_ratios += gear_ratio
    return sum_of_gear_ratios


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
