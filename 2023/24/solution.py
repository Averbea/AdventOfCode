""" Advent of code Year 2023 Day 24 solution
Author = Averbea
Date = December 2023
"""

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    toRet = []
    for line in file.splitlines():
        coords, dirs = line.split('@')
        coords = [int(x) for x in coords.split(',')]
        dirs = [int(x) for x in dirs.split(',')]

        toRet.append(coords + dirs)
    return toRet


def x_is_in_past(x, start_x, dx):
    if dx > 0:
        return x < start_x
    else:
        return x > start_x


@timeit
def part_one():
    """Solution for Part 1"""
    data = process_input()
    equations = []
    for x, y, z, dx, dy, dz in data:
        a = dy / dx
        b = y - a * x
        equations.append((a, b))

    count = 0
    # for each pair in equations, check their intersection
    for i in range(len(equations)):
        x1, y1, z1, dx1, dy1, dz1 = data[i]
        a1, b1 = equations[i]
        for j in range(i + 1, len(equations)):
            a2, b2 = equations[j]
            x2, y2, z2, dx2, dy2, dz2 = data[j]

            if a1 == a2:  # parallel
                continue
            x = (b2 - b1) / (a1 - a2)
            y = a1 * x + b1

            if x_is_in_past(x, x1, dx1) or x_is_in_past(x, x2, dx2):
                # if x_is_in_past(y, y1, dy1) and x_is_in_past(y, y2, dy2):
                #     print("in past for both")
                # elif x_is_in_past(y, y1, dy1):
                #     print("in past for 1")
                # else:
                #     print("in past for 2")
                continue

            # test uses other nums
            lower = 200000000000000  # test uses 7
            upper = 400000000000000  # test uses 27
            if lower <= x <= upper and lower <= y <= upper:
                count += 1
    return count


@timeit
def part_two():
    """Solution for Part 2"""
    data = process_input()
    return 0


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
