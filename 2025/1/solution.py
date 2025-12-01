""" Advent of code Year 2025 Day 1 solution
Link to task: https://adventofcode.com/2025/day/1
Author = Averbea
Date = 01/12/2025
"""

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str) -> list[tuple[str, int]]:
    """parses the input file and returns the result"""
    input_data = input_data.splitlines()

    result:list[tuple[str, int]] = []
    for line in input_data:
        direction = line[0]
        value = int(line[1:])

        result.append((direction, value))

    return result


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    data = process_input(input_data)

    count_zeros = 0

    current = 50
    for direction, value in data:

        if direction == "R":
            current += value
        elif direction == "L":
            current -= value
        else:
            raise ValueError(f"Unknown direction {direction}")
        current %= 100
        if current == 0:
            count_zeros += 1
    return count_zeros


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    data = process_input(input_data)

    count_zeros = 0

    current = 50
    for direction, value in data:
        for _ in range(value):
            if direction == "R":
                current += 1
            elif direction == "L":
                current -= 1
            else:
                raise ValueError(f"Unknown direction {direction}")
            current %= 100
            if current == 0:
                count_zeros += 1
    return count_zeros

if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

