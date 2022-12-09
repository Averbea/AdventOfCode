""" Advent of code Year 2022 Day 9 solution
Author = Averbea
Date = December 2022
"""


import os
import re
from time import time

from numpy import sign


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

    return re.findall(r"(\w) (\d*)", inputs)


DIRECTIONS = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}


def get_new_knot_pos(prev_knot: tuple, cur_knot: tuple):
    """Caluclate the new position of cur_knot given the position of prev_knot """

    cur_x, cur_y = cur_knot
    prev_x, prev_y = prev_knot

    diff_x = prev_x - cur_x
    diff_y = prev_y - cur_y

    if abs(diff_x) <= 1 and abs(diff_y) <= 1:
        # the tail is adjacent to or under head. No need to update tail pos
        return cur_knot

    new_x = cur_x
    new_y = cur_y
    if diff_x == 0:
        # The tail is placed horizontal relative to head
        new_y = cur_y + int(diff_y/2)
    elif diff_y == 0:
        # The tail is placed vertical relative to head
        new_x = cur_x + int(diff_x/2)
    else:
        # tail is not in same row or same column. Move diagonally
        new_x = cur_x + sign(diff_x)
        new_y = cur_y + sign(diff_y)

    return (new_x, new_y)

def part_one():
    """Solution for Part 1"""
    steps = parse_input()

    head = tail = (0, 0)

    all_tail_positions = set()
    all_tail_positions.add(tail)

    for direction, amount in steps:
        for _ in range(int(amount)):
            move_x, move_y = DIRECTIONS[direction]
            head = (head[0] + move_x, head[1] + move_y)
            # get new tail pos
            tail = get_new_knot_pos(head, tail)
            # add tail pos to set
            all_tail_positions.add(tail)

    return len(all_tail_positions)


def part_two():
    """Solution for Part 2"""
    steps = parse_input()

    knots = [(0, 0) for _ in range(10)]

    all_tail_positions = set()
    all_tail_positions.add(knots[-1])

    for direction, amount in steps:
        move_x, move_y = DIRECTIONS[direction]
        for _ in range(int(amount)):
            # move the first knot in the direction
            knots[0] = (knots[0][0] + move_x, knots[0][1] + move_y)

            # for every following knot, calculate the new position
            for i in range(1, len(knots)):
                knots[i] = get_new_knot_pos(knots[i-1], knots[i])
                # add the last knots' position to the set
                all_tail_positions.add(knots[-1])

    return len(all_tail_positions)


def main():
    """main method"""

    # print(get_new_tail((3,3), (2,1)))
    time_needed, result = measure_timing(part_one)

    print("Part One : " + str(result))
    print("time elapsed: " + str(time_needed))

    time_needed, result = measure_timing(part_two)
    print("\nPart Two : " + str(result))
    print("time elapsed: " + str(time_needed))


if __name__ == "__main__":
    main()
