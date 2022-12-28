""" Advent of code Year 2022 Day 25 solution
Author = Averbea
Date = December 2022
"""


from lib2to3.pytree import convert
import math
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
    return inputs


def snafu_to_dec(snafu_str: str):
    snafu_lookup = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2
    }
    decimal = 0
    base = 1
    for char in reversed(snafu_str):
        decimal += base * snafu_lookup[char]
        base *= 5
    return decimal


def dec_to_snafu(remaining: int):
    """convert dec to snafu"""
    # build number up from right
    # snafu is base 5. Last digit can be calculated by n % 5

    #   Decimal          SNAFU
    #     0              0
    #     1              1
    #     2              2
    #     3             1=   carry 1 to next position
    #     4             1-   carry 1 to next position
    #     5             10   repeats from here (with carry)
    #     6             11
    #     7             12
    #     8             2=
    #     9             2-
    #    10             2
    # 0

    lookup = "012=-"    # according to order above
    
    output = ""

    while remaining:
        rest = remaining % 5 # get last d
        remaining //= 5     # the remaining amount to calculate for more left digits

        output = lookup[rest] + output
        if rest > 2:
            # carry to next position
            remaining += 1
    return output


def part_one():
    """Solution for Part 1"""
    snafu_numbers = parse_input()
    sum_in_dec = 0
    for snafu_number in snafu_numbers:
        sum_in_dec += snafu_to_dec(snafu_number)
    sum_in_snafu = dec_to_snafu(sum_in_dec)
    return sum_in_snafu


def part_two():
    """Solution for Part 2"""
    # data = parse_input()
    return 0


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
