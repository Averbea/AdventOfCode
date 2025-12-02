""" Advent of code Year 2024 Day 9 solution
Link to task: https://adventofcode.com/2024/day/9
Author = Averbea
Date = 09/12/2024
"""
from tqdm import tqdm, trange

from utils.templateutils import timeit, read_input_file


def process_input(input_data):
    """parses the input file and returns the result"""
    free_spaces = []
    files = {}
    index = 0
    end_index = 0
    for i, c in enumerate(input_data):
        start = index
        end = index + int(c) - 1
        index = end + 1
        end_index = end
        if i % 2 == 0:
            files[i // 2] = (start, end)
        else:
            free_spaces.append((start, end))
    return files, free_spaces, end_index


def decompress_input_data(input_data):
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
    data = decompress_input_data(input_data)
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
    for i, c in enumerate(data):
        if c == ".":
            continue
        checksum += i * int(c)
    return checksum


def print_it(files, free_spaces, end_index):
    for i in range(end_index + 1):
        for key, value in files.items():
            if value[0] <= i <= value[1]:
                print(key, end="")
                break
        for space in free_spaces:
            if space[0] <= i <= space[1]:
                print(".", end="")
                break
    print()


@timeit
def part_two(input_data):
    """Solution for Part 2"""
    files, free_spaces, end_index = process_input(input_data)

    for key in tqdm(reversed(files.keys()), total=len(files)):

        file_start, file_end = files[key]
        file_size = file_end - file_start + 1

        # find the first space that fits the file
        for i, space in enumerate([space for space in free_spaces if space[0] < file_start]):
            space_start, space_end = space
            space_size = space_end - space_start + 1
            if space_size >= file_size:
                # move the file to the space

                files[key] = (space_start, space_start + file_size - 1)
                if space_size > file_size:
                    free_spaces[i] = (space_start + file_size, space_end)
                else:
                    free_spaces.pop(i)
                new_free_space = (file_start, file_end)
                free_spaces.append(new_free_space)

                break

    checksum = 0
    for file_id, position in files.items():
        for i in range(position[0], position[1] + 1):
            checksum += i * file_id

    return checksum


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))
