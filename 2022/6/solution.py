""" Advent of code Year 2022 Day 6 solution
Author = Averbea
Date = December 2022
"""


import os
from time import time


def measure_timing( func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result

def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) +"/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read()
    return inputs


def has_multiples(s: str):
    """Checks if the chars of the given string are present multiple times"""
    for char in s:
        if s.count(char) != 1:
            return True
    return False

def parse_substrings(data: str, substring_length: int):
    """parses data for all substrings witih length substring_length. Returns a generator"""
    for index in range(substring_length, len(data)+1):
        substring = data[index-substring_length: index]
        yield index, substring

def part_one():
    """Solution for Part 1"""
    data = parse_input()
    for index, last_four in parse_substrings(data, 4):
        if not has_multiples(last_four):
            return index
    return 0

def part_two():
    """Solution for Part 2"""
    data = parse_input()
    for index, last_fourteen in parse_substrings(data, 14):
        if not has_multiples(last_fourteen):
            return index
    return 0




def main():
    """main method"""
    time_needed, result = measure_timing(part_one)

    print("Part One : "+ str(result))
    print("time elapsed: " + str(time_needed))

    time_needed, result = measure_timing(part_two)
    print("\nPart Two : "+ str(part_two()))
    print("time elapsed: " + str(time_needed))
    print()

if __name__ == "__main__":
    main()
