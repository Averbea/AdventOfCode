""" Advent of code Year 2024 Day 7 solution
Link to task: https://adventofcode.com/2024/day/7
Author = Averbea
Date = 07/12/2024
"""
import re

from utils.templateutils import timeit, read_input_file


def process_input(input_data):
    """parses the input file and returns the result"""
    results = []
    for line in input_data.splitlines():
        matches = re.findall(r"(\d+)", line)
        results.append([int(x) for x in matches])
    return results


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def concat(a, b):
    return int(str(a) + str(b))

def tryout(data, target_val, operators_to_try):
    if len(data) == 2:
        if any([op(data[0], data[1]) == target_val for op in operators_to_try]):
            return True
        else:
            return False

    for op in operators_to_try:
        result = op(data[0], data[1])
        if tryout([result] + data[2:], target_val, operators_to_try):
            return True
    return False



def solve(data, operators_to_try):
    calibration_result = 0
    for line in data:
        result = line[0]
        numbers = line[1:]
        valid = tryout(numbers, result, operators_to_try)
        if valid:
            calibration_result += result

    return calibration_result


@timeit
def part_one(input_data):
    """Solution for Part 1"""
    data = process_input(input_data)
    return solve(data, [add, multiply])


@timeit
def part_two(input_data):
    """Solution for Part 2"""
    data = process_input(input_data)
    return solve(data, [add, multiply, concat])


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

