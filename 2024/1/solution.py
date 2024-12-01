""" Advent of code Year 2024 Day 1 solution
Link to task: https://adventofcode.com/2024/day/1
Author = Averbea
Date = December 2024
"""
import re

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file()
    numbers = re.findall(r"\d+", file)
    # every second number is in the other list
    leftlist, rightlist = [], []
    for i, number in enumerate(numbers):
        if i % 2 == 0:
            leftlist.append(int(number))
        else:
            rightlist.append(int(number))
    return leftlist, rightlist


@timeit
def part_one():
    """Solution for Part 1"""
    left, right = process_input()
    left.sort()
    right.sort()

    result = 0
    for i in range(len(left)):
        result += abs(left[i] - right[i])
    return result


@timeit
def part_two():
    """Solution for Part 2"""
    left, right = process_input()
    occurences_in_right = {}

    for n in right:
        if n in occurences_in_right:
            occurences_in_right[n] += 1
        else:
            occurences_in_right[n] = 1
    similarity_score = 0
    for n in left:
        similarity_score += n * occurences_in_right.get(n, 0)
    return similarity_score


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
