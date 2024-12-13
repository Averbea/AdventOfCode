""" Advent of code Year 2024 Day 13 solution
Link to task: https://adventofcode.com/2024/day/13
Author = Averbea
Date = 13/12/2024
"""
import math
import re

from tqdm import tqdm, trange

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    blocks = input_data.split("\n\n")
    machines = []
    for block in blocks:
        a_x, a_y, b_x, b_y, price_x, price_y = re.findall(r"\d+", block)
        machines.append((int(a_x), int(a_y), int(b_x), int(b_y), int(price_x), int(price_y)))
    return machines

PRICE_FOR_PUSHING_A = 3
PRICE_FOR_PUSHING_B = 1




@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    machines = process_input(input_data)
    total_cost = 0
    for a_x, a_y, b_x, b_y, price_x, price_y  in machines:
        # try out all combinations of as and bs to get to price_x, price_y with max 100 presses per button
        min_price = math.inf
        for i_a in range(100):
            for i_b in range(100):
                if i_a * a_x + i_b * b_x == price_x and i_a * a_y + i_b * b_y == price_y:
                    current_cost = i_a * PRICE_FOR_PUSHING_A + i_b * PRICE_FOR_PUSHING_B
                    min_price = min(min_price, current_cost)
        if min_price == math.inf:
            continue
        total_cost += min_price
    return total_cost


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    machines = process_input(input_data)
    total_cost = 0
    for a_x, a_y, b_x, b_y, price_x, price_y in machines:
        price_x += 10000000000000
        price_y += 10000000000000
        # solve the following system of equations
        # a_x * a_i + b_x * b_i = price_x
        # a_y * a_i + b_y * b_i = price_y
        i_a = (price_x * b_y - price_y * b_x) / (a_x * b_y - a_y * b_x)
        i_b = (price_x * a_y - price_y * a_x) / (b_x * a_y - b_y * a_x)

        if i_a % 1 != 0 or i_b % 1 != 0:
            continue # no integer solution, so we can't solve this
        total_cost += int(i_a * PRICE_FOR_PUSHING_A + i_b * PRICE_FOR_PUSHING_B)
    return total_cost


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

