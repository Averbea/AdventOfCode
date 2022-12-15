""" Advent of code Year 2022 Day 15 solution
Author = Averbea
Date = December 2022
"""


from collections import defaultdict
import os
import re
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

    tmp = re.findall(
        r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)", inputs)
    data = list(map(
        lambda item: (
            (int(item[0]), int(item[1])), (int(item[2]), int(item[3]))
    ), tmp))
    return data


def manhattan_distance(point_a: tuple[int, int], point_b: tuple[int, int]):
    """return manhattan distance betweeen to points"""
    return sum(abs(val1-val2) for val1, val2 in zip(point_a, point_b))


def merge_ranges(ranges: list):
    """merge overlapping ranges in the list"""
    if len(ranges) == 1:
        return ranges
    ranges.sort(key=lambda x: x[0])
    new_ranges = [ranges[0]]
    i = 0
    while i < len(ranges)-1:
        i += 1
        cur = ranges[i]
        prev = new_ranges[-1]

        if cur[0] <= prev[1]:
            # these overlap on left of cur
            if cur[1] <= prev[1]:
                # this range is already in the list
                continue
            else:
                # expand the previous range
                new_ranges[-1][1] = cur[1]
        else:
            new_ranges.append(cur)

    return new_ranges

def get_row_block(data: list[tuple[tuple[int,int], tuple[int,int]]], row):
    """get ranges which are blocked in given row row"""
    blocked_ranges = []
    for sensor, beacon in data:
        distance = manhattan_distance(sensor, beacon)
        dist_to_row = abs(sensor[1] - row)
        if distance < dist_to_row:
            continue
        x_range = distance - dist_to_row
        cur_blocked = [sensor[0] - x_range, sensor[0] + x_range]
        blocked_ranges.append(cur_blocked)
        blocked_ranges = merge_ranges(blocked_ranges)
    return blocked_ranges


def part_one():
    """Solution for Part 1"""
    data = parse_input()
    blocked_ranges = get_row_block(data, 2000000)
    sum_blocked = 0
    for rang in blocked_ranges:
        sum_blocked += (rang[1] - rang[0])
    return sum_blocked


def part_two():
    """Solution for Part 2"""
    data = parse_input()
    for y_pos in range(4000000):
        print(y_pos, round(y_pos/4000000 * 100,2), "%",' '*30, end="\r")
        row_blocks = get_row_block(data, y_pos)
        if len(row_blocks) > 1:
            x_pos = row_blocks[0][1]+1
            return 4000000 * x_pos + y_pos


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
