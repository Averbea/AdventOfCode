""" Advent of code Year 2022 Day 8 solution
Author = Averbea
Date = December 2022
"""


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
        inputs = input_file.read().split("\n")

    to_ret = list(map(lambda row: list(map(int, row)), inputs))
    return to_ret


def in_bounds(x_pos, y_pos, width, height):
    """checks if x_pos and y_pos is in the boundaries"""
    return 0 <= x_pos < width and 0 <= y_pos < height


def check_visibility(forest, direction):
    """
    check the visibility of trees in forest looking in direction and returns visible trees as set
    """
    initial_x, initial_y = 0, 0
    step_horizontal = True
    height, width = len(forest), len(forest[0])

    match direction:
        case "up":
            initial_y = height - 1
            step_horizontal = False
        case "down":
            step_horizontal = False
        case "left":
            initial_x = width - 1

    visible = set()
    iterate_size = height if step_horizontal else width

    for index in range(iterate_size):
        # in each row/column x_pos and y_pos have to be reset
        x_pos, y_pos = initial_x, initial_y
        # reset the max_height
        prev_max_height = -1

        if step_horizontal:
            y_pos = index  # iterate over rows (y)
        else:
            x_pos = index  # iterate over columns (x)

        while in_bounds(x_pos, y_pos, width, height):
            cur_height = forest[y_pos][x_pos]
            if cur_height > prev_max_height:
                # the current tree is visible
                visible.add((y_pos, x_pos))
                prev_max_height = cur_height
            # do a step in direction
            x_pos, y_pos = step(x_pos, y_pos, direction)

    return visible


def part_one():
    """Solution for Part 1"""
    forest = parse_input()

    visible = set()

    directions = ["left", "right", "up", "down"]
    for directory in directions:
        cur_direction_visible = check_visibility(forest, directory)
        visible.update(cur_direction_visible)

    return len(visible)


def step(x_pos, y_pos, direction):
    """returns x and y while stepping one step into direction from x_pos, y_pos"""
    match direction:
        case "right":
            return x_pos+1, y_pos
        case "left":
            return x_pos-1, y_pos
        case "up":
            return x_pos, y_pos-1
        case "down":
            return x_pos, y_pos+1
    return -1, -1


def get_view_dist(forest, y_pos, x_pos, direction):
    """return the view distance in forest from a position looking into direction"""
    height = len(forest)
    width = len(forest[0])

    cur_height = forest[y_pos][x_pos]
    view_dist = 0
    x_pos, y_pos = step(x_pos, y_pos, direction)
    while in_bounds(x_pos, y_pos, width, height):
        new_tree_height = forest[y_pos][x_pos]
        if new_tree_height < cur_height:
            # we can still see something: increase viewdistance and do a step
            view_dist += 1
            x_pos, y_pos = step(x_pos, y_pos, direction)
        elif new_tree_height >= cur_height:
            # the cur tree is bigger or equal to the origin tree
            return view_dist + 1
    # the edge is reached
    return view_dist


def calc_scenic_score(forest, y_pos, x_pos):
    """calculate the scenic score at a given position"""
    directions = ["left", "right", "up", "down"]
    scenic_score = 1
    # scenic score is equal to view distance in every direction multiplied
    for directory in directions:
        view_dist = get_view_dist(forest, y_pos, x_pos, directory)
        scenic_score *= view_dist
    return scenic_score


def part_two():
    """Solution for Part 2"""
    forest = parse_input()

    max_score = 0
    for y_pos, row in enumerate(forest):
        for x_pos, _ in enumerate(row):
            # find the maximum scenic score in forest
            cur_score = calc_scenic_score(forest, y_pos, x_pos)
            max_score = max(cur_score, max_score)

    return max_score


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
