""" Advent of code Year 2024 Day 9 solution
Link to task: https://adventofcode.com/2024/day/9
Author = Averbea
Date = 09/12/2024
"""


from utils.templateutils import timeit, read_input_file


def process_input(input_data):
    """parses the input file and returns the result"""
    decompressed = []
    for i, c in enumerate(input_data):

        if i % 2 == 0:
            file_id = i // 2

            decompressed += [file_id] * int(c)
        else:
            decompressed += ["."] * int(c)


    return decompressed


@timeit
def part_one(input_data):
    """Solution for Part 1"""
    data = process_input(input_data)
    left = 0
    right = len(data) - 1

    while left < right:
        if data[left] != ".":
            left += 1
            continue
        if data[right] == ".":
            right -= 1
            continue

        data[left] = data[right]
        data[right] = "."


    checksum = 0
    for i,c in enumerate(data):
        if c == ".":
            continue
        checksum += i * int(c)
    return checksum
@timeit
def part_two(input_data):
    """Solution for Part 2"""
    data = process_input(input_data)

    return 0


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

