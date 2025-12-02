""" Advent of code Year 2022 Day 4 solution
Author = Averbea
Date = December 2022
"""


import os
import re
from time import time

start = time()

with open(os.path.dirname(__file__) +"/input.txt", 'r', encoding="UTF-8") as inputFile:
    inputs = inputFile.read()

inputs = inputs.split()
RANGES = []
for i in inputs:
    numbers = re.match(r"(\d*)-(\d*),(\d*)-(\d*)", i)
    start_first, end_first, start_second, end_second = numbers.groups()
    first_range = list(range(int(start_first), int(end_first)+1))
    second_range = list(range(int(start_second), int(end_second)+1))
    RANGES.append([first_range, second_range])


def range_contains(range1:list[int], range2:list[int]):
    """ check if range1 is in range2

    Returns:
        bool_: range2 contains range1
    """
    # for entry in range1:
    #     if entry not in range2:
    #         return False
    # return True
    return set(range1).issubset(set(range2))

def ranges_overlap(range1:list[int], range2:list[int]):
    """check if ranges overlap

    Returns:
        bool: ranges overlap
    """
    # for entry in range1:
    #     if entry in range2:
    #         return True
    # return False
    return  set(range1).intersection(set(range2)) != set()

def part_one():
    """solution for part one

    Returns:
        int: count of assignments in which one section contains the other
    """
    count = 0
    for rang in RANGES:
        if range_contains(rang[0], rang[1]) or range_contains(rang[1], rang[0]):
            count += 1
    return count

def part_two():
    """solution for part two

    Returns:
        int: count of assignments in which the sections overlap
    """
    count = 0
    for rang in RANGES:
        if ranges_overlap(rang[0], rang[1]):
            count += 1
    return count

print("Part One : "+ str(part_one()))

print("Part Two : "+ str(part_two()))

print("time elapsed: " + str(time() - start))
