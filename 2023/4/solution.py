""" Advent of code Year 2023 Day 4 solution
Author = Averbea
Date = December 2023
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
        inputs = input_file.read().splitlines()

    scratchcards = []
    for line in inputs:
        line = line.split(':')[1]
        numbers, winning = line.split('|')
        numbers = [int(number) for number in numbers.split(' ') if number.isdigit()]
        winning = [int(number) for number in winning.split(' ') if number.isdigit()]
        scratchcards.append((numbers, winning))

    return scratchcards


def part_one():
    """Solution for Part 1"""
    scratchcards = parse_input()
    total_points = 0
    for numbers, winning in scratchcards:
        points = 0
        for num in numbers:
            if num in winning:
                points = 1 if points == 0 else points * 2
        total_points += points

    return total_points


def part_two():
    """Solution for Part 2"""
    scratchcards = parse_input()
    count = [1 for card in scratchcards]
    for idx, card in enumerate(scratchcards):
        numbers, winning = card
        points = 0
        for num in numbers:
            if num in winning:
                points += 1
        for i in range(points):
            count[idx + i + 1] += count[idx]

    return sum(count)


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
