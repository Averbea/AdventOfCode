""" Advent of code Year 2022 Day 22 solution
Author = Averbea
Date = December 2022
"""


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

    grid, instructions = inputs.split("\n\n")
    grid = grid.splitlines()

    max_len = 0
    for line in grid:
        max_len = max(len(line), max_len)

    for i, line in enumerate(grid):
        if len(line) < max_len:
            new_line = line + ' ' * (max_len - len(line))
            grid[i] = new_line

    nums = re.findall(r"\d+", instructions)
    nums = list(map(int, nums))
    dirs = re.findall(r"[LR]", instructions)

    instruction_result = [None]*(len(nums)+len(dirs))
    instruction_result[::2] = nums
    instruction_result[1::2] = dirs
    return grid, instruction_result


def move_part1(grid: list[str], pos: tuple[int, int], dir_index: int):
    """make a move according to rules in part 1"""
    y_size = len(grid)
    x_size = len(grid[0])

    y_pos, x_pos = pos
    y_dir, x_dir = DIRS[dir_index]
    while True:
        y_pos = (y_pos + y_dir) % y_size
        x_pos = (x_pos + x_dir) % x_size
        if grid[y_pos][x_pos] != ' ':
            break
    return (y_pos, x_pos)



def move_part2(pos: tuple[int, int], dir_index: int):
    """move according to rules of part 3"""
    y_pos, x_pos = pos
    y_dir, x_dir = DIRS[dir_index]

    new_y_pos = y_pos + y_dir
    new_x_pos = x_pos + x_dir

    row = new_y_pos + 1
    column = new_x_pos + 1
    new_row = row
    new_column = column
    new_dir = dir_index

    # check if at edge of cube and update row, column and direction
    if 0 <= row <= 50 and column < 51 and x_dir == -1:
        new_row = 150 - row + 1
        new_column = 1
        new_dir = 0
    elif 0 <= row <= 50 and column > 150 and x_dir == 1:
        new_row = 150 - row + 1
        new_column = 100
        new_dir = 2
    elif 51 <= row <= 100 and column < 51 and x_dir == -1:
        new_row = 101
        new_column = row - 50
        new_dir = 1
    elif 51 <= row <= 100 and column > 100 and x_dir == 1:
        new_row = 50
        new_column = row - 50 + 100
        new_dir = 3
    elif 101 <= row <= 150 and column < 1 and x_dir == -1:
        new_row = 50 - (row - 101)
        new_column = 51
        new_dir = 0
    elif 101 <= row <= 150 and column > 100 and x_dir == 1:
        new_row = 50 - (row - 101)
        new_column = 150
        new_dir = 2
    elif 151 <= row <= 200 and column < 1 and x_dir == -1:
        new_row = 1
        new_column = 51 + (row - 151)
        new_dir = 1
    elif 151 <= row <= 200 and column > 50 and x_dir == 1:
        new_row = 150
        new_column = 51 + (row - 151)
        new_dir = 3

    elif 51 <= column <= 100 and row < 1 and y_dir == -1:
        new_row = 151 + (column - 51)
        new_column = 1
        new_dir = 0
    elif 101 <= column <= 150 and row < 1 and y_dir == -1:
        new_row = 200
        new_column = 1 + (column - 101)
        new_dir = 3
    elif 101 <= column <= 150 and row > 50 and y_dir == 1:
        new_row = 51 + (column - 101)
        new_column = 100
        new_dir = 2
    elif 1 <= column <= 50 and row < 101 and y_dir == -1:
        new_row = 51 + (column - 1)
        new_column = 51
        new_dir = 0
    elif 51 <= column <= 100 and row > 150 and y_dir == 1:
        new_row = 151 + (column - 51)
        new_column = 50
        new_dir = 2
    elif 1 <= column <= 50 and row > 200 and y_dir == 1:
        new_row = 1
        new_column = 101 + (column - 1)
        new_dir = 1

    new_y_pos = new_row - 1
    new_x_pos = new_column - 1

    return (new_y_pos, new_x_pos), new_dir


def is_wall(grid, position):
    """check if position is wall in grid"""
    y_pos, x_pos = position
    y_len = len(grid)
    x_len = len(grid[0])

    return grid[y_pos % y_len][x_pos % x_len] == '#'


def score(row_index, col_index, dir_index):
    """calculate the score for given row, col and direction index"""
    return 1000 * (row_index + 1) + 4 * (col_index + 1) + dir_index


def print_grid(grid: list[str], moves: list[list]):
    """print the grid with moves"""
    dirs = ">v<^"
    for line_index, line in enumerate(grid):
        for column_index, column in enumerate(line):
            dir_index = -1
            for _, element in enumerate(moves):

                if element[0] == (line_index, column_index):
                    dir_index = element[1]
                    # print(dir_index)
                    break

            if dir_index != -1:
                print(dirs[dir_index], end="")
            else:
                print(column, end="")

        print("")


# dirs = right, down, left, up
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part_one():
    """Solution for Part 1"""
    grid, instructions = parse_input()

    cur_dir_index = 0
    position = move_part1(grid, (0, 0), cur_dir_index)
    positions = []
    for instruction in instructions:
        if isinstance(instruction, int):
            for _ in range(instruction):
                positions.append([position, cur_dir_index])
                new_position = move_part1(grid, position, cur_dir_index)
                if is_wall(grid, new_position):
                    break
                position = new_position
        elif instruction == 'L':
            cur_dir_index = (cur_dir_index - 1) % len(DIRS)
        elif instruction == 'R':
            cur_dir_index = (cur_dir_index + 1) % len(DIRS)
    positions.append([position, cur_dir_index])
    # print_grid(grid, positions)

    # print("end_row", position[0] + 1)
    # print("end_row", position[1] + 1)
    # print("dir_index", cur_dir_index)

    return score(position[0], position[1], cur_dir_index)


def part_two():
    """Solution for Part 2"""
    grid, instructions = parse_input()
    positions = []
    position = (199, 0)

    cur_dir_index = 0
    position = move_part1(grid, (0, 0), cur_dir_index)
    positions = []
    for instruction in instructions:
        if isinstance(instruction, int):
            for _ in range(instruction):
                positions.append([position, cur_dir_index])
                new_position, new_dir_index = move_part2(
                    position, cur_dir_index)
                if is_wall(grid, new_position):
                    break
                position = new_position
                cur_dir_index = new_dir_index
        elif instruction == 'L':
            cur_dir_index = (cur_dir_index - 1) % len(DIRS)
        elif instruction == 'R':
            cur_dir_index = (cur_dir_index + 1) % len(DIRS)
    positions.append([position, cur_dir_index])

    # print_grid(grid, positions)
    return score(position[0], position[1], cur_dir_index)


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
