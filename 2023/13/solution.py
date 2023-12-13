""" Advent of code Year 2023 Day 13 solution
Author = Averbea
Date = December 2022
"""

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    patterns = file.split("\n\n")
    return [pattern.split("\n") for pattern in patterns]


def find_symmetry_row(pattern):
    for to_top in range(1, len(pattern)):
        to_bottom = len(pattern) - to_top
        amount_to_check = min(to_top, to_bottom)

        for i in range(amount_to_check):
            if pattern[to_top - i - 1] != pattern[to_top + i]:
                break
        else:
            return to_top


def find_diff_count_one(pattern):
    for to_top in range(1, len(pattern)):
        diffs = 0
        to_bottom = len(pattern) - to_top
        amount_to_check = min(to_top, to_bottom)

        for i in range(amount_to_check):
            diffs += sum(c1 != c2 for c1, c2 in zip(pattern[to_top - i - 1], pattern[to_top + i]))
            if diffs > 1:
                break
        if diffs == 1:
            return to_top


@timeit
def part_one():
    """Solution for Part 1"""
    patterns = process_input()
    sum_of_all = 0
    for pattern in patterns:
        to_top_of_symmetry = find_symmetry_row(pattern)
        inverted = list(zip(*pattern))
        to_left_of_symmetry = find_symmetry_row(inverted)
        if to_left_of_symmetry:
            sum_of_all += to_left_of_symmetry
        else:
            sum_of_all += to_top_of_symmetry * 100

    return sum_of_all


@timeit
def part_two():
    """Solution for Part 2"""
    patterns = process_input()
    sum_of_all = 0
    for pattern in patterns:
        to_top_of_symmetry = find_diff_count_one(pattern)
        inverted = list(zip(*pattern))
        to_left_of_symmetry = find_diff_count_one(inverted)

        if to_left_of_symmetry:
            sum_of_all += to_left_of_symmetry
        else:
            sum_of_all += to_top_of_symmetry * 100
    return sum_of_all


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
