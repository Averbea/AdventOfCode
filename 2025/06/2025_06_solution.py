""" Advent of code Year 2025 Day 6 solution
Link to task: https://adventofcode.com/2025/day/6
Author = Averbea
Date = 06/12/2025
"""
import re
from functools import reduce

from utils.templateutils import timeit, read_input_file

OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def process_input_p1(input_data):
    lines = input_data.splitlines()
    result = []
    for line in lines[:-1]:
        line = re.split(r'\s+', line.strip())
        result.append(list(map(int, line)))

    result.append(re.split('\s+', lines[-1]))

    return result


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    # get ever spalte from table
    data = process_input_p1(input_data)
    columns = []
    for i in range(len(data[0])):
        column = [row[i] for row in data]
        columns.append(column)
    total = 0
    for c in columns:
        result = reduce(OPERATIONS[c[-1]], c[1:-1], c[0])
        total += result

    return total


def process_input_p2(input_data: str):
    result = []
    lines = input_data.splitlines()
    prev_i = 0
    for i in range(len(lines[0])):
        if all(c[i] == ' ' for c in lines):
            # split here
            result.append([line[prev_i:i] for line in lines])
            prev_i = i + 1

    last_line = [line[prev_i:] for line in lines]
    longest = max(len(l) for l in last_line)
    for i in range(len(last_line)):
        last_line[i] = last_line[i].ljust(longest)

    result.append(last_line)

    return result


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    data = process_input_p2(input_data)
    total = 0
    for d in data:
        op = OPERATIONS[d[-1].strip()]
        d = d[:-1]
        numbers = []
        for i in range(len(d[0])):
            column = [row[i] for row in d]
            column = reduce(lambda a, b: a + b, column, '')
            numbers.append(int(column))

        result = reduce(op, numbers)
        total += result
    return total


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))
