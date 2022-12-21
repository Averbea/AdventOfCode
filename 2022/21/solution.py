""" Advent of code Year 2022 Day 21 solution
Author = Averbea
Date = December 2022
"""


from collections import defaultdict
from copy import deepcopy
from math import floor
import os
from time import time

from matplotlib.dates import num2date


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
    data = defaultdict()
    for line in inputs:
        name, rest = line.split(": ")
        try:
            value = int(rest)
        except ValueError:
            value = rest.split(" ")

        data[name] = value
    return data


def solve(data: dict, name: str):
    """solve it"""
    cur_element = data[name]
    if isinstance(cur_element, int):
        return cur_element

    name1, operator, name2 = cur_element
    num1 = solve(data, name1)
    num2 = solve(data, name2)

    result = 0
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 / num2
    return result


def part_one():
    """Solution for Part 1"""
    data = parse_input()

    result = solve(data, "root")
    return result


def part_two():
    """Solution for Part 2"""
    data = parse_input()
    
    lower_limit = 0
    upper_limit = int(1e30)

    root1, _, root2 = data["root"]
    target_element = root1 # root1 changes when changing data["humn"]
    

    target_value = solve(data, root2)

    upper = 1e20
    lower  = 0
    while True: 
        mid = int((upper+lower) // 2)
        data["humn"] = mid
        result = solve(data, target_element)
        diff = target_value - result
        if diff < 0:
            lower = mid
        elif diff > 0:
            upper = mid
        else: 
            return mid



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
