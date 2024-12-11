""" Advent of code Year 2024 Day 11 solution
Link to task: https://adventofcode.com/2024/day/11
Author = Averbea
Date = 11/12/2024
"""
from collections import defaultdict
from functools import lru_cache

from tqdm import trange


from utils.templateutils import timeit, read_input_file


def process_input(input_data):
    """parses the input file and returns the result"""
    return [int(x) for x in input_data.split(" ")]



#    0
# -> 1
# -> 2024
# -> 20 24
# -> 2 0 2 4
# -> 4048 1 4048 8096
# -> 40 48 2024 40 48 80 96



@timeit
def part_one(input_data):
    """Solution for Part 1"""
    stones = process_input(input_data)
    for _ in trange(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones += [1]
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                new_stones += [int(str(stone)[:mid]), int(str(stone)[mid:])]
            else:
                new_stones += [stone * 2024]
        stones = new_stones
    return len(stones)


@timeit
def part_two(input_data):
    """Solution for Part 2"""
    stones = process_input(input_data)
    stone_counts = defaultdict(int)
    for stone in stones:
        stone_counts[stone] += 1

    for _ in trange(75):
        new_stone_counts = defaultdict(int)
        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                new_stone_counts[int(str(stone)[:mid])] += count
                new_stone_counts[int(str(stone)[mid:])] += count
            else:
                new_stone_counts[stone * 2024] += count
        stone_counts = new_stone_counts

    return sum(stone_counts.values())


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

