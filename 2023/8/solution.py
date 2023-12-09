""" Advent of code Year 2023 Day 8 solution
Author = Averbea
"""
import re

from utils.math import kgv
from utils.tenplateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    file = file.split("\n")
    instructions = file[0]

    directions = {src: (left, right) for line in file[2:] for src, left, right in [re.findall(r'\w+', line)]}
    return instructions, directions


def find_min_steps(src, destinations, graph, instructions, initial_steps=0):
    location = src
    i = initial_steps
    instructions_length = len(instructions)
    while location not in destinations:
        if instructions[i % instructions_length] == 'R':
            location = graph[location][1]
        else:
            location = graph[location][0]
        i += 1
    return i


@timeit
def part_one():
    """Solution for Part 1"""
    instructions, directions = process_input()
    return find_min_steps('AAA', 'ZZZ', directions, instructions)


@timeit
def part_two():
    """Solution for Part 2"""
    instructions, directions = process_input()
    locations = [key for key in directions.keys() if key.endswith('A')]
    destinations = [key for key in directions.keys() if key.endswith('Z')]
    cycles = []
    for loc in locations:
        cycle = []
        step_count = 0
        while len(cycle) < 3:
            steps_to_next_dest = find_min_steps(loc, destinations, directions, instructions, step_count) - step_count
            cycle.append(steps_to_next_dest)
        cycles.append(cycle)
    print(cycles)
    # as it always takes the same steps to get to end state as it does to get from end state to next end state
    # we can just take the first step count of each cycle and calculate the kgv of those
    return kgv([cycle[0] for cycle in cycles])


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
