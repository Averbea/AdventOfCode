""" Advent of code Year 2025 Day 2 solution
Link to task: https://adventofcode.com/2025/day/2
Author = Averbea
Date = 02/12/2025
"""


from utils.templateutils import timeit, read_input_file


def process_input(input_data: str) -> list[tuple[int, int]]:
    """parses the input file and returns the result"""
    ranges = input_data.split(",")

    return [tuple(map(int, r.split("-"))) for r in ranges]


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    ranges = process_input(input_data)
    total = 0
    for start, end in ranges:
        for number in range(start, end + 1):
            numstr = str(number)
            num_len = len(numstr)
            if numstr[:num_len // 2] == numstr[num_len // 2:]:
                total += number
    return total


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    ranges = process_input(input_data)
    total = 0
    for start, end in ranges:
        for number in range(start, end + 1):
            numstr = str(number)
            num_len = len(numstr)
            divisors = [i for i in range(1,num_len) if num_len % i == 0]
            for d in divisors:

                if all(numstr[i] == numstr[i + d] for i in range(num_len - d)):
                    total += number
                    break
    return total


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

