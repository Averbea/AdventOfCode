""" Advent of code Year 2025 Day 9 solution
Link to task: https://adventofcode.com/2025/day/9
Author = Averbea
Date = 09/12/2025
"""
from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    return [tuple(map(int,l.split(","))) for l in input_data.splitlines()]


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    data = process_input(input_data)
    max_area = 0
    for point in data:
        for other_point in data:
            area = (abs(point[0]-other_point[0])+1) * (abs(point[1]-other_point[1])+1)
            max_area = max(area, max_area)
    return max_area


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    points = process_input(input_data)
    outline = set()



    for idx, p in enumerate(points):
        next_point = points[(idx+1)%len(points)]
        min_x = min(p[0], next_point[0])
        max_x = max(p[0], next_point[0])
        min_y = min(p[1], next_point[1])
        max_y = max(p[1], next_point[1])

        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                outline.add((x,y))

    max_area = 0
    for x,y in points:
        for x1, y2 in points:
            current_area = (abs(x1 - x) + 1) * (abs(y2 - y) + 1)
            if current_area <= max_area:
                continue

            min_x = min(x, x1)
            max_x = max(x, x1)
            min_y = min(y, y2)
            max_y = max(y, y2)

            # check if outline is in rectangle
            for ox, oy in outline:
                if min_x < ox < max_x and min_y < oy < max_y:
                    # outline is in rectangle
                    break
            else:
                max_area = current_area
    return max_area







if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

