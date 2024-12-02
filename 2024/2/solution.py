""" Advent of code Year 2024 Day 2 solution
Link to task: https://adventofcode.com/2024/day/2
Author = Averbea
Date = 02/12/2024
"""
from sympy import false

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    return  [ [int(a) for a in line.split(" ")] for line in file.splitlines()  ]


def check_if_safe(row):
    issafe = True
    increasing = True if row[0] < row[1] else false
    for i in range(len(row) - 1):
        if increasing and row[i] >= row[i + 1] or not increasing and row[i] <= row[i + 1]:
            issafe = False
            break
        diff = row[i + 1] - row[i]
        if abs(diff) > 3:
            issafe = False
            break
    return issafe
@timeit
def part_one():
    """Solution for Part 1"""
    rows = process_input()
    safe = 0
    for row in rows:
        if check_if_safe(row):
            safe += 1
    return safe


@timeit
def part_two():
    """Solution for Part 2"""
    rows = process_input()
    safe = 0
    for row in rows:
        options = []
        for i in range(len(row)):
            options.append(row[:i] + row[i+1:])
        if any(check_if_safe(option) for option in options):
            safe += 1
    return safe


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
