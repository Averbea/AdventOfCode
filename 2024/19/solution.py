""" Advent of code Year 2024 Day 19 solution
Link to task: https://adventofcode.com/2024/day/19
Author = Averbea
Date = 19/12/2024
"""
from tqdm import tqdm

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    data = input_data.split("\n\n")

    return data[0].split(", "), data[1].splitlines()



@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    patterns, displays = process_input(input_data)

    possible = 0
    for display in displays:
        to_test = [("", 0)]
        while to_test:
            cur_test, pos = to_test.pop()
            if cur_test == display:
                possible += 1
                break
            for pattern in patterns:
                if display[pos:pos+len(pattern)] == pattern:
                    to_test.append((cur_test + pattern, pos + len(pattern)))

    return possible


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    data = process_input(input_data)
    return 0


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

