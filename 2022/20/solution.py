""" Advent of code Year 2022 Day 20 solution
Author = Averbea
Date = December 2022
"""


from collections import deque
from functools import reduce
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

    return list(map(int, inputs))


def mix(input_data, times):
    """mix input data according to the rules. Do this the specified times"""
    data = deque()
    for start_index, value in enumerate(input_data):
        data.append([start_index, value])
    # print([d[1] for d in data])
    for i in range(times):
        print("iteration", i)
        for index in range(len(data)):
            while data[0][0] != index:
                data.append(data.popleft())

            cur = data.popleft()
            number_to_pop = cur[1] % len(data)
            assert 0 <= number_to_pop < len(data)
            for _ in range(number_to_pop):
                data.append(data.popleft())
            data.append(cur)
            # print([d[1] for d in data])
        tmp_index = 0
        while data[tmp_index][1] != 0:
            data.append(data.popleft())
    return [d[1] for d in data]


def part_one():
    """Solution for Part 1"""
    data = parse_input()
    data = mix(data, 1)
    nums = [1000, 2000, 3000]
    result = reduce(lambda a, b: a + data[b % len(data)], nums, 0)
    return result


def part_two():
    """Solution for Part 2"""
    data = parse_input()
    decryption_key = 811589153
    data = list(map(lambda el: el * decryption_key, data))
    data = mix(data, 10)
    nums = [1000, 2000, 3000]
    result = reduce(lambda a, b: a + data[b % len(data)], nums, 0)
    return result


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
