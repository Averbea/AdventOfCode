""" Advent of code Year 2022 Day 5 solution
Author = Averbea
Date = December 2022
"""


import os
import re
from time import time


def measure_timing( func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result

def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) +"/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read()

    # Stacks and moves are seperated by an empty line
    inputs = inputs.split("\n\n")

    ## Inital stack
    stacks = []
    inputs[0] = inputs[0].split("\n")

    stack_lines = inputs[0][::-1]
    stack_number_line = stack_lines[0]
    number_of_stacks = int(re.findall(r"(\d*)\s$", stack_number_line)[0])

    for i, line in enumerate(stack_lines):
        for number in range(number_of_stacks):
            if i == 0:
                stacks.append([])
                continue
            element = line[1+4*number]
            if element != " ":
                stacks[number].append(element)

    ## Moves
    moves = inputs[1].split("\n")
    crane_moves = []
    for action in moves:
        move, move_from, move_to = re.match(r"move (\d+) from (\d+) to (\d+)", action).groups()
        crane_moves.append({"move": int(move), "from": int(move_from), "to":int(move_to)})
    return stacks, crane_moves


def get_upper_elements(stacks):
    """returns the top elements of the given stacks as a string"""
    upper_elements = ""
    for stack in stacks:
        upper_elements += stack[-1]
    return upper_elements

def part_one():
    """Solution for Part 1"""
    stacks, crane_moves = parse_input()
    for action in crane_moves:
        for i in range(action["move"]):
            element = stacks[action["from"]-1].pop()
            stacks[action["to"] -1].append(element)
    return get_upper_elements(stacks)

def part_two():
    """Solution for Part 2"""
    stacks, crane_moves = parse_input()
    for action in crane_moves:
        elements = []
        for i in range(action["move"]):
            elements.append(stacks[action["from"]-1].pop())
        for element in elements[::-1]:
            stacks[action["to"] -1].append(element)
    return get_upper_elements(stacks)



def main():
    """main method"""
    time_needed, result = measure_timing(part_one)

    print("Part One : "+ str(result))
    print("time elapsed: " + str(time_needed))

    time_needed, result = measure_timing(part_two)
    print("\nPart Two : "+ str(part_two()))
    print("time elapsed: " + str(time_needed))


if __name__ == "__main__":
    main()
