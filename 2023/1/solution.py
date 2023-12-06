""" Advent of code Year 2023 Day 1 solution
Author = Averbea
Date = December 2023
"""

import os
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


def part_one():
    """Solution for Part 1"""
    data = parse_input()

    total = 0
    for line in data:
        number_chars = [item for item in line if item.isdigit()]
        total += int(number_chars[0] + number_chars[-1])
    return total


def part_two():
    """Solution for Part 2"""
    data = parse_input()
    number_dictionary = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    total = 0
    for line in data:
        number_chars = []
        for idx, c in enumerate(line):
            if c.isdigit():
                number_chars.append(c)
            else:
                for key in number_dictionary.keys():
                    if line[idx:].startswith(key):
                        number_chars.append(str(number_dictionary[key]))
                        break
        current_calibration_val = int(number_chars[0] + number_chars[-1])
        total += current_calibration_val
    return total


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
