""" Advent of code Year 2024 Day 14 solution
Link to task: https://adventofcode.com/2024/day/14
Author = Averbea
Date = 14/12/2024
"""
import re

from tqdm import trange

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    numbers = []
    for line in input_data.splitlines():
        # p=80,58 v=-80,-45
        numbers += [list(map(int, re.findall(r"[-\d]+", line)))]
    return numbers

TEST = False


def positions_after_seconds(robots, seconds, width, height):
    new_positions = []
    for start_x, start_y, vel_x, vel_y in robots:
        new_x = (start_x + vel_x * seconds) % width
        new_y = (start_y + vel_y * seconds) % height
        new_positions.append((new_x, new_y))
    return new_positions

@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    robots = process_input(input_data)
    seconds = 100
    width = 11 if TEST else 101
    height = 7 if TEST else 103
    new_positions = positions_after_seconds(robots, seconds, width, height)

    quadrants = [0, 0, 0, 0]

    middle_col = width // 2
    middle_row = height // 2
    for new_pos in new_positions:
        x, y = new_pos
        if x < middle_col and y < middle_row:
            quadrants[0] += 1
        elif x > middle_col and y < middle_row:
            quadrants[1] += 1
        elif x < middle_col and y > middle_row:
            quadrants[2] += 1
        elif x > middle_col and y > middle_row:
            quadrants[3] += 1
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

def print_image(positions, width, height):
    image = [["." for _ in range(width)] for _ in range(height)]
    for x, y in positions:
        image[y][x] = "#"
    for row in image:
        print("".join(row))

@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    robots = process_input(input_data)

    width = 11 if TEST else 101
    height = 7 if TEST else 103
    # I am guessing that in the Easter egg image the robots will be in a row next to each other,
    # so I will iterate over the seconds and check if there are at least 10 robots in a row next to each other

    for i in trange(10000):
        new_positions = set(positions_after_seconds(robots, i, width, height))
        # if there are at least 10 positions in one row next to each other , print the image.
        for y in range(height):
            for x in range(width - 9):
                if all((x + i, y) in new_positions for i in range(10)):
                    print("After", i, "seconds:")
                    print_image(new_positions, width, height)
                    return i
    return -1


if __name__ == "__main__":
    file_content = read_input_file(test=TEST)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

