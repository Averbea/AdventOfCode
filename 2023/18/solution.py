""" Advent of code Year 2023 Day 18 solution
Author = Averbea
Date = December 2023
"""

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    lines = file.splitlines()
    # splitte jede linie in lines (R 11 (#00b1d2)) in 3 teile (string, int, string
    splitted = [[line.split(' ')[0], int(line.split(' ')[1]), line.split(' ')[2][2:-1]] for line in lines]
    return splitted


def fill_trench(trench: set, definetly_inside):
    """fills trench using flood fill algorithm"""
    to_fill = [definetly_inside]

    while to_fill:
        x, y = to_fill.pop()
        if (x, y) in trench:
            continue
        trench.add((x, y))
        to_add = [
            (x, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x, y + 1),
        ]

        for a in to_add:
            to_fill.append(a)


def print_trench(trench):
    min_x = min([x[0] for x in trench])
    max_x = max([x[0] for x in trench])
    min_y = min([x[1] for x in trench])
    max_y = max([x[1] for x in trench])

    print('    ', [i for i in range(min_x, max_x)])
    for y in range(min_y, max_y + 1):
        print(y, '  ', end='')
        for x in range(min_x, max_x + 1):
            if (x, y) in trench:
                print('#', end='')
            else:
                print('.', end='')
        print('')


def dig_trench(data) -> set[tuple[int, int]]:
    pos = (0, 0)
    trench = set()
    trench.add(pos)
    for line in data:
        direction, steps, color = line

        for i in range(steps):
            match direction:
                case 'R':
                    pos = (pos[0] + 1, pos[1])
                case 'L':
                    pos = (pos[0] - 1, pos[1])
                case 'U':
                    pos = (pos[0], pos[1] + 1)
                case 'D':
                    pos = (pos[0], pos[1] - 1)
            trench.add(pos)

    return trench


@timeit
def part_one():
    """Solution for Part 1"""
    data = process_input()
    trench = dig_trench(data)
    fill_trench(trench, (2, -8))
    # print_trench(trench)
    return len(trench)


def get_trench_corners(data, use_color=False):
    circumference = 0
    pos = (0, 0)
    trench_corners = [pos]
    for line in data:
        direction, steps, color = line
        if use_color:
            match color[-1]:
                case '0':
                    direction = 'R'
                case '1':
                    direction = 'D'
                case '2':
                    direction = 'L'
                case '3':
                    direction = 'U'

            steps = int(color[:-1], 16)

        match direction:
            case 'R':
                pos = (pos[0] + steps, pos[1])
            case 'L':
                pos = (pos[0] - steps, pos[1])
            case 'U':
                pos = (pos[0], pos[1] + steps)
            case 'D':
                pos = (pos[0], pos[1] - steps)
        trench_corners.append(pos)
        circumference += steps
    return trench_corners, circumference


def area_inside(corners):
    """area inside polygon -> shoelace formula"""
    area = 0
    for i, corner in enumerate(corners):
        area += corner[0] * (
                corners[(i + 1) % len(corners)][1] - corners[(i - 1) % len(corners)][1])
    area //= 2
    return abs(area)


@timeit
def part_two():
    """Solution for Part 2"""
    data = process_input()
    trench_corners, circumference = get_trench_corners(data, use_color=True)
    area = area_inside(trench_corners)
    # picks theorem: A = i + b/2 - 1     i = points inside, b = boundary points, A = area
    # A + b = i + b/2 + 1
    return area + circumference / 2 + 1


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
