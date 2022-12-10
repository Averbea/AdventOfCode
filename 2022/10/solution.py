""" Advent of code Year 2022 Day 10 solution
Author = Averbea
Date = December 2022
"""


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
    to_ret = []
    for i in inputs:
        to_ret.append(i.split())
    return to_ret


def get_register_cycles():
    """calculate the registers values in each cycle"""
    commands = parse_input()

    register_values = [1]
    for command in commands:
        if command[0] == "noop":
            # no operation: register stays the same
            register_values.append(register_values[-1])
        elif command[0] == "addx":
            # addx takes two cycles
            register_values.append(register_values[-1])
            register_values.append(register_values[-1] + int(command[1]))
    return register_values


def part_one():
    """Solution for Part 1"""
    register_cycles = get_register_cycles()

    cycles_to_get = [20, 60, 100, 140, 180, 220]

    sum_signal_strengths = 0
    for cycle_to_get in cycles_to_get:
        signal_strength = cycle_to_get * register_cycles[cycle_to_get - 1]
        sum_signal_strengths += signal_strength
    return sum_signal_strengths


def part_two():
    """Solution for Part 2"""
    crt_width = 40
    crt_height = 6

    register_cycles = get_register_cycles()

    cycle = 0
    for _ in range(crt_height):
        # new Line
        print("")
        for x_pos in range(1, crt_width + 1):
            sprite_pos = register_cycles[cycle]
            # sprite is 3 pixels wide
            if sprite_pos == x_pos or sprite_pos + 1 == x_pos or sprite_pos + 2 == x_pos:
                # sprite covers currently drawn pixel
                print("#", end="")
            else:
                # sprite does not cover the current pixel
                print(".", end="")
            cycle += 1
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
