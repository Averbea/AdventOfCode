""" Advent of code Year 2023 Day 5 solution
Author = Averbea
Date = December 2023
"""
import math
import os
from time import time


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end - time_start, result


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read().split('\n\n')

    seeds, *maps = inputs
    # find all numbers in seeds
    seeds = [int(s) for s in seeds.split(' ') if s.isdigit()]

    maps = [m.split('\n')[1:] for m in maps]
    maps = [[list(map(int, line.split(' '))) for line in m] for m in maps]

    return seeds, maps


def convert(source, map):
    target = source
    for idx, num in enumerate(source):
        for dest_range_start, source_range_start, range_length in map:
            delta = dest_range_start - source_range_start
            if source_range_start <= num < source_range_start + range_length:
                target[idx] = num + delta
                break
    return target


def part_one():
    """Solution for Part 1"""
    seeds, maps = parse_input()
    values = [seed for seed in seeds]
    for map in maps:
        values = convert(values, map)
    return min(values)


def convert2(ranges, map):
    target = []
    for range in ranges:
        for dest_frst, src_first, map_rng_lngth in map:
            src_last = src_first + map_rng_lngth - 1
            dest_last = dest_frst + map_rng_lngth - 1
            delta = dest_frst - src_first

            is_right_in_rng = src_first <= range[-1] <= src_last
            is_left_in_rng = src_first <= range[0] <= src_last

            if is_right_in_rng and is_left_in_rng:
                target.append([range[0] + delta, range[-1] + delta])
                break

            if is_left_in_rng:
                target.append([range[0] + delta, dest_last])
                ranges.append([src_last + 1, range[-1]])
                break

            if is_right_in_rng:
                target.append([dest_frst, range[-1] + delta])
                ranges.append([range[0], src_first - 1])
                break

            if range[0] < src_first and range[-1] > src_last:
                target.append([dest_frst, dest_last])
                ranges.append([range[0], src_first - 1])
                ranges.append([src_last + 1, range[-1]])
        else:
            target.append(range)

    return target


def part_two():
    """Solution for Part 2"""
    seed_line, maps = parse_input()

    # split seeds into pairs of two
    seed_ranges = [seed_line[i:i + 2] for i in range(0, len(seed_line), 2)]
    ranges = [[seed_range[0], seed_range[0] + seed_range[1] - 1] for seed_range in seed_ranges]
    print("seeds", ranges)
    for map in maps:
        ranges = convert2(ranges, map)
        print(ranges)

    minimum = math.inf
    for lower, _ in ranges:
        minimum = min(lower, minimum)

    return minimum


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
