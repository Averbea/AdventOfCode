""" Advent of code Year 2024 Day 8 solution
Link to task: https://adventofcode.com/2024/day/8
Author = Averbea
Date = 08/12/2024
"""
from collections import defaultdict

from utils.templateutils import timeit, read_input_file


def process_input(input_data):
    """parses the input file and returns the result"""

    antennas = defaultdict(list)
    input_data = input_data.splitlines()
    max_x = len(input_data[0]) - 1
    max_y = len(input_data) - 1
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            if char != ".":
                antennas[char].append((x, y))
    return antennas, max_x, max_y


def get_all_pairs(antennas):
    pairs = []
    for i, a in enumerate(antennas):
        for b in antennas[i + 1:]:
            pairs.append((a, b))
    return pairs


@timeit
def part_one(input_data):
    """Solution for Part 1"""
    antennas, max_x, max_y = process_input(input_data)

    antinode_locations = set()
    for frequency in antennas:
        # all combinations of antennas at frequency
        pairs = get_all_pairs(antennas[frequency])

        for a, b in pairs:
            diff = (b[0] - a[0], b[1] - a[1])

            # calc all points that are twice as far from one antenna to the other
            x, y = b[0] + diff[0], b[1] + diff[1]
            if 0 <= x <= max_x and 0 <= y <= max_y:
                antinode_locations.add((x, y))
            x, y = a[0] - diff[0], a[1] - diff[1]
            if 0 <= x <= max_x and 0 <= y <= max_y:
                antinode_locations.add((x, y))

    return len(antinode_locations)


@timeit
def part_two(input_data):
    """Solution for Part 2"""
    antennas, max_x, max_y = process_input(input_data)

    antinode_locations = set()
    for frequency in antennas:
        pairs = get_all_pairs(antennas[frequency])

        for a, b in pairs:
            diff = (b[0] - a[0], b[1] - a[1])
            # calc all points that are twice as far from one antenna to the other
            x, y = b[0], b[1]  # the antenna itself and all nodes in line are antinodes
            while 0 <= x <= max_x and 0 <= y <= max_y:
                antinode_locations.add((x, y))
                x += diff[0]
                y += diff[1]

            x, y = a[0], a[1]  # the antenna itself and all nodes in line are antinodes
            while 0 <= x <= max_x and 0 <= y <= max_y:
                antinode_locations.add((x, y))
                x -= diff[0]
                y -= diff[1]

    return len(antinode_locations)


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))
