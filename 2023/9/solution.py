""" Advent of code Year 2023 Day 9 solution
Author = Averbea
"""

from utils.tenplateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False).splitlines()
    data = [[int(num) for num in line.split(" ")] for line in file]
    return data


def calc_diffs(line):
    diffs = [line]
    cur = line

    while any([x != 0 for x in cur]):
        cur_diffs = []
        for i in range(len(cur) - 1):
            cur_diffs.append(cur[i + 1] - cur[i])
        diffs.append(cur_diffs)
        cur = cur_diffs
    return diffs


@timeit
def part_one():
    """Solution for Part 1"""
    lines = process_input()
    sum = 0
    for line in lines:
        diffs = calc_diffs(line)

        # extrapolate
        diffs[-1].append(0)
        for i in reversed(range(len(diffs) - 1)):
            diffs[i].append(diffs[i + 1][-1] + diffs[i][-1])
        sum += diffs[0][-1]
    return sum


@timeit
def part_two():
    """Solution for Part 2"""
    lines = process_input()
    sum = 0
    for line in lines:
        diffs = calc_diffs(line)

        # extrapolate
        diffs[-1].insert(0, 0)
        for i in reversed(range(len(diffs) - 1)):
            diffs[i].insert(0, diffs[i][0] - diffs[i + 1][0])
        sum += diffs[0][0]
    return sum


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
