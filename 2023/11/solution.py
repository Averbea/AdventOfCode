""" Advent of code Year 2023 Day 11 solution
Author = Averbea
Date = December 2023
"""


from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False).splitlines()
    return [[i for i in line] for line in file]


def calc_sum_of_distances(distance_of_empty, data):
    empty_rows = [i for i, row in enumerate(data) if row.count('.') == len(row)]
    empty_cols = [i for i, col in enumerate(zip(*data)) if col.count('.') == len(col)]
    galaxies = [(i, j) for i, row in enumerate(data) for j, col in enumerate(row) if col == '#']

    pairs = [(galaxies[i], galaxies[j]) for i in range(len(galaxies)) for j in range(i+1, len(galaxies))]
    sum_of_distances = 0
    for a, b in pairs:
        lower_row = min(a[0], b[0])
        upper_row = max(a[0], b[0])
        lower_col = min(a[1], b[1])
        upper_col = max(a[1], b[1])
        count_empty_rows = sum([1 for i in range(lower_row, upper_row+1) if i in empty_rows])
        count_empty_cols = sum([1 for i in range(lower_col, upper_col+1) if i in empty_cols])

        # -1 because one row / col is already in grid
        row_distance = upper_row - lower_row + count_empty_rows * (distance_of_empty-1)
        col_distance = upper_col - lower_col + count_empty_cols * (distance_of_empty-1)
        sum_of_distances += row_distance + col_distance
    return sum_of_distances


@timeit
def part_one():
    """Solution for Part 1"""
    data = process_input()
    return calc_sum_of_distances(2, data)


@timeit
def part_two():
    """Solution for Part 2"""
    data = process_input()
    return calc_sum_of_distances(1000000, data)


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
