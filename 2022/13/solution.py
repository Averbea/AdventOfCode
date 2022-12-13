""" Advent of code Year 2022 Day 13 solution
Author = Averbea
Date = December 2022
"""


from functools import cmp_to_key
import json
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
        inputs = input_file.read()
    inputs = inputs.split("\n\n")

    pairs = []
    for group in inputs:
        pair = group.splitlines()
        new_data = [json.loads(pair[0]), json.loads(pair[1])]
        pairs.append(new_data)
    return pairs


def compare(left, right, prefix="") -> int:
    """compares left  item to right item.

        Return -1 if left < right
        Return 0 if left = right
        Return 1 if left > right"""
    # print(prefix + "- Compare ", left, "vs", right)

    # if both are ints compare them
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        if left == right:
            return 0
        if left > right:
            return 1

    # if one iem is an int and the other a list, convert the type and compare again
    if isinstance(left, int) and isinstance(right, list):
        # print(prefix + " - Mixed Types")
        converted = [left]
        return compare(converted, right, prefix+"  ")
    if isinstance(left, list) and isinstance(right, int):
        # print(prefix + " - Mixed Types")
        converted = [right]
        return compare(left, converted, prefix + " ")

    # if both are lists compare each item in the list
    index = 0
    while index < len(left) and index < len(right):
        res = compare(left[index], right[index], prefix+"  ")
        if res != 0:
            return res
        index += 1

    if index == len(left) == len(right):
        # both lists are equal in length
        return 0
    if index == len(left):
        # left side ran out of items
        return -1
    if index == len(right):
        # right side ran out of items
        return 1


def part_one():
    """Solution for Part 1"""
    pairs = parse_input()

    indices_correct = []
    for index, pair in enumerate(pairs, start=1):
        left, right = pair
        res = compare(left, right)
        if res == -1:
            indices_correct.append(index)

    return sum(indices_correct)


def part_two():
    """Solution for Part 2"""
    groups = parse_input()

    all_packets = []
    for left, right in groups:
        all_packets.append(left)
        all_packets.append(right)

    divider6 = [[6]]
    divider2 = [[2]]

    all_packets.append(divider2)
    all_packets.append(divider6)

    all_packets.sort(key=cmp_to_key(compare))
    # first packet should be equal to 1
    return (all_packets.index(divider2) + 1) * (all_packets.index(divider6) + 1)


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
