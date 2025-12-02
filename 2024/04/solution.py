""" Advent of code Year 2024 Day 4 solution
Link to task: https://adventofcode.com/2024/day/4
Author = Averbea
Date = 04/12/2024
"""
import re

from utils.templateutils import timeit, read_input_file


def process_input(input_data):
    """parses the input file and returns the result"""
    return input_data.splitlines()



@timeit
def part_one(input_data):
    """Solution for Part 1"""
    data = process_input(input_data)

    # get all positions of x with index
    x_positions = set()

    for lineidx, line in enumerate(data):
        positions = [m.start() for m in re.finditer('X', line)]
        for pos in positions:
            x_positions.add((lineidx, pos))

    # for each X Position check every direction for XMAS
    xmas_count = 0
    max_col = len(data[0]) -1
    max_row = len(data) -1
    for (row, col) in x_positions:
        # right check
        if col <= max_col - 3 and data[row][col] == "X" and data[row][col + 1] == "M" and data[row][col + 2] == "A" and data[row][col + 3] == "S":
            xmas_count += 1
        # left check
        if col >= 3 and data[row][col] == "X" and data[row][col - 1] == "M" and data[row][col - 2] == "A" and data[row][col - 3] == "S":
            xmas_count += 1
        # down check
        if row <= max_row - 3 and data[row][col] == "X" and data[row + 1][col] == "M" and data[row + 2][col] == "A" and data[row + 3][col] == "S":
            xmas_count += 1
        # up check
        if row >= 3 and data[row][col] == "X" and data[row - 1][col] == "M" and data[row - 2][col] == "A" and data[row - 3][col] == "S":
            xmas_count += 1
        # diagonal down right
        if row <= max_row - 3 and col <= max_col - 3 and data[row][col] == "X" and data[row + 1][col + 1] == "M" and data[row + 2][col + 2] == "A" and data[row + 3][col + 3] == "S":
            xmas_count += 1
        # diagonal up right
        if row >= 3 and col <= max_col - 3 and data[row][col] == "X" and data[row - 1][col + 1] == "M" and data[row - 2][col + 2] == "A" and data[row - 3][col + 3] == "S":
            xmas_count += 1
        # diagonal down left
        if row <= max_row - 3 and col >= 3 and data[row][col] == "X" and data[row + 1][col - 1] == "M" and data[row + 2][col - 2] == "A" and data[row + 3][col - 3] == "S":
            xmas_count += 1
        # diagonal up left
        if row >= 3 and col >= 3 and data[row][col] == "X" and data[row - 1][col - 1] == "M" and data[row - 2][col - 2] == "A" and data[row - 3][col - 3] == "S":
            xmas_count += 1


    return xmas_count


@timeit
def part_two(input_data):
    """Solution for Part 2"""
    data = process_input(input_data)
    a_positions = set()
    for lineidx, line in enumerate(data):
        positions = [m.start() for m in re.finditer('A', line)]
        for pos in positions:
            a_positions.add((lineidx, pos))

    max_col = len(data[0]) -1
    max_row = len(data) -1
    x_mas_found = 0
    for (row, col) in a_positions:
        if 0 < row < max_row and 0 < col < max_col:
            # count how many diagonals say MAS at given position.
            # this can be a maximum of two
            tmp_count = 0
            # bottom left to top right
            if data[row -1][col-1] == "M" and data[row+1][col+1] == "S":
                tmp_count += 1
            # top right to bottom left
            elif data[row - 1][col - 1] == "S" and data[row + 1][col + 1] == "M":
                tmp_count += 1
            # bottom right to top left
            if data[row-1][col +1] == "M" and data[row+1][col-1] == "S":
                tmp_count += 1
            # top left to bottom right
            elif data[row - 1][col + 1] == "S" and data[row + 1][col - 1] == "M":
                tmp_count += 1

            if tmp_count ==2:
                x_mas_found += 1

    return x_mas_found



if __name__ == "__main__":
    file_content = read_input_file()
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))
