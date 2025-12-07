""" Advent of code Year 2025 Day 7 solution
Link to task: https://adventofcode.com/2025/day/7
Author = Averbea
Date = 07/12/2025
"""
import re
from collections import defaultdict

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    lines = input_data.splitlines()
    start = lines[0].index("S")
    return start, [[s.start() for s in re.finditer("\^", line)] for line in lines[1:]  ]



@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    start, lines = process_input(input_data)
    beams = {start}
    times_split = 0
    for line in lines:
        new_beams = set()
        for beam in beams:
            if beam in line:
                times_split += 1
                new_beams.add(beam-1)
                new_beams.add(beam+1)
            else:
                new_beams.add(beam)
        beams = new_beams


    return times_split


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    start, lines = process_input(input_data)

    timelines = defaultdict(int)
    timelines[start] = 1
    for line in lines:
        new_timelines = defaultdict(int)
        for beam in timelines:
            if beam in line:
                new_timelines[beam-1] += timelines[beam]
                new_timelines[beam+1] += timelines[beam]
            else:
                new_timelines[beam] += timelines[beam]
        timelines = new_timelines


    return sum(timelines.values())


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

