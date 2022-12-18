""" Advent of code Year 2022 Day 18 solution
Author = Averbea
Date = December 2022
"""


import os
from time import time
from turtle import right
from typing import Callable

from traitlets import Bool


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = [tuple(map(int, x.split(",")))
                  for x in input_file.read().splitlines()]
    return inputs


OFFSETS = [
    (-1, 0, 0),   # left
    (0, 1, 0),    # up
    (1, 0, 0),    # right
    (0, -1, 0),   # down
    (0, 0, 1),    # front
    (0, 0, -1)    # back
]


def get_outside_checker(blocks) -> Callable[[tuple[int, int, int]], bool]:
    """closure returning a function which chekces """

    # memorize blocks that can / cannot reach outside
    cannot_reach_outside = set()
    can_reach_outside = set()

    # these are the first blocks of air top, left, bottom right, front and back
    # These are definetly not inside
    lower_border = min(blocks, key=lambda x: x[1])[1] - 1
    upper_border = max(blocks, key=lambda x: x[1])[1] + 1
    left_border = min(blocks, key=lambda x: x[0])[0] - 1
    right_border = max(blocks, key=lambda x: x[0])[0] + 1
    front_border = max(blocks, key=lambda x: x[2])[2] + 1
    back_border = min(blocks, key=lambda x: x[2])[2] - 1

    def reaches_outside(block_to_check: tuple[int, int, int]) -> bool:
        """check if the block_to_check can reach outside"""
        # store elements that were checked to memorize them later
        now_checked = set()

        # queue stores elements to explore
        queue = [block_to_check]
        while len(queue) > 0:
            cur = queue.pop(0)

            if cur in blocks:  # cur is not air
                continue
            if cur in can_reach_outside:
                # cur has already been memorized as can reach outside
                # checked items can also not reach outside
                can_reach_outside.update(now_checked)
                return True
            if cur in cannot_reach_outside:
                # cur has already been memorized as can not reach outside
                # checked items can also reach outside
                cannot_reach_outside.update(now_checked)
                return False

            now_checked.add(cur)

            # if cur is outside of the borders it can obviously reach outside
            if cur[1] < lower_border or cur[1] > upper_border or \
                    cur[0] < left_border or cur[0] > right_border or \
                    cur[2] < back_border or cur[2] > front_border:
                can_reach_outside.update(now_checked)
                return True

            # explore in every direction
            for off_x, off_y, off_z in OFFSETS:
                new_to_check = (cur[0] + off_x, cur[1] + off_y, cur[2] + off_z)

                # if the new block has already been checked, is not air or is already queued
                # it does not need to be checked again
                if new_to_check in now_checked or new_to_check in blocks or new_to_check in queue:
                    continue

                queue.append(new_to_check)
        # if there are no elements to be explored and we have not reached outside by now
        # this block is inside
        cannot_reach_outside.update(now_checked)
        return False

    return reaches_outside


def part_one():
    """Solution for Part 1"""
    blocks = parse_input()

    count_faces = 0
    # for all blocks check all directions if there is a block
    # if there is air update count
    for block_x, block_y, block_z in blocks:
        for x_offset, y_offset, z_offset in OFFSETS:
            to_check = (block_x + x_offset, block_y +
                        y_offset, block_z + z_offset)
            if to_check not in blocks:
                count_faces += 1
    return count_faces


def part_two():
    """Solution for Part 2"""
    blocks = parse_input()

    reaches_outside = get_outside_checker(blocks)
    count_faces = 0
    # for all blocks check all directions if there is a block
    # if there is air also check if this has an outside connection then update count
    for block_x, block_y, block_z in blocks:
        for x_offset, y_offset, z_offset in OFFSETS:
            to_check = (block_x + x_offset, block_y +
                        y_offset, block_z + z_offset)
            if to_check not in blocks:
                if reaches_outside(to_check):
                    count_faces += 1
    return count_faces


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
