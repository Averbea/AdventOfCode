""" Advent of code Year 2023 Day 6 solution
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
        inputs = input_file.read().splitlines()

    times = [int(n) for n in inputs[0].split(' ') if n.isdigit()]
    distances = [int(n) for n in inputs[1].split(' ') if n.isdigit()]

    return times, distances


def solve(times, distances):
    """solves the puzzle"""
    margin_of_error = 1
    for time, distance in zip(times, distances):
        count_win = 0
        for hold_time in range(time + 1):
            my_distance = hold_time * (time - hold_time)
            if my_distance > distance:
                count_win += 1
        margin_of_error *= count_win
    return margin_of_error


def part_one():
    """Solution for Part 1"""
    times, distances = parse_input()
    return solve(times, distances)


def part_two():
    """Solution for Part 2"""
    times, distances = parse_input()
    # join times to a big number
    times = [int(''.join([str(n) for n in times]))]
    distances = [int(''.join([str(n) for n in distances]))]
    return solve(times, distances)


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
