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
    # TODO parse input into correct data structure
    return inputs




def part_one():
    """Solution for Part 1"""
    # data = parse_input()
    return 0

def part_two():
    """Solution for Part 2"""
    # data = parse_input()
    return 0




def main():
    """main method"""
    time_needed, result = measure_timing(part_one)

    print("Part One : "+ str(result))
    print("time elapsed: " + str(time_needed))

    time_needed, result = measure_timing(part_two)
    print("\nPart Two : "+ str(part_two()))
    print("time elapsed: " + str(time_needed))


if __name__ == "__main__":
    main()
