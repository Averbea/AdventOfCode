""" Advent of code Year 2024 Day 12 solution
Link to task: https://adventofcode.com/2024/day/12
Author = Averbea
Date = 12/12/2024
"""
from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    return input_data.splitlines()


def find_regions(garden):
    regions = set()
    for row, line in enumerate(garden):
        for column, plot in enumerate(line):
            # if this plot is in any of the regions, skip htis
            if any((column, row) in area for area in regions):
                continue
            # explore the area
            new_region = set()
            to_explore = {(column, row)}
            while to_explore:
                c, r = to_explore.pop()
                if (c, r) in new_region:
                    continue
                new_region.add((c, r))
                # check the neighbors
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(garden) and 0 <= nc < len(garden[0]) and garden[nr][nc] == plot:
                        to_explore.add((nc, nr))
            regions.add(frozenset(new_region))
    return regions

@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    garden = process_input(input_data)
    regions = find_regions(garden)

    total_price = 0
    for region in regions:
        borders = set()
        for c, r in region:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nc, nr) not in region:
                    borders.add((c,r, dc, dr))

        area = len(region)
        perimeter = len(borders)
        price = area * perimeter
        total_price += price

    return total_price


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    garden = process_input(input_data)
    regions = find_regions(garden)

    total_price = 0
    for region in regions:
        borders = set()
        for c, r in region:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nc, nr) not in region:
                    borders.add((c, r, dc, dr))

        side_count = 0

        for border in borders:
            c, r, dc, dr = border
            if dc == 1:
                if (c, r+1, dc, dr) not in borders:
                    side_count += 1
            if dc == -1:
                if (c, r-1, dc, dr) not in borders:
                    side_count += 1
            if dr == 1:
                if (c+1, r, dc, dr) not in borders:
                    side_count += 1
            if dr == -1:
                if (c-1, r, dc, dr) not in borders:
                    side_count += 1

        area = len(region)
        #print(garden[r][c], "Area", area, "Side count", side_count)

        price = area * side_count
        total_price += price

    return total_price


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

