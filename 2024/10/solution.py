""" Advent of code Year 2024 Day 10 solution
Link to task: https://adventofcode.com/2024/day/10
Author = Averbea
Date = 10/12/2024
"""


from utils.templateutils import timeit, read_input_file


def process_input(input_data):
    """parses the input file and returns the result"""
    the_map = input_data.splitlines()

    trailheads = []
    for y, row in enumerate(the_map):
        for x, char in enumerate(row):
            if char == "0":
                trailheads.append((x, y))
    return the_map, trailheads

def reachable_tops(pos, the_map) -> list[tuple[int,int]]:
    """
    For a given position, returns all the positions that are reachable
    if there are multiple ways to reach a top there will be an entry for this top for each way to reach it
    """
    x, y = pos
    cur_height  = int(the_map[y][x])
    max_y = len(the_map) -1
    max_x = len(the_map[0]) -1
    if cur_height == 9:
        return [pos]

    ways = []
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        next_pos = (x + dx, y + dy)
        if not (0 <= next_pos[0] <= max_x and  0<= next_pos[1] <= max_y):
            continue
        next_height = int(the_map[next_pos[1]][next_pos[0]])
        if next_height == cur_height +1:
            ways += reachable_tops(next_pos, the_map)
    return ways

@timeit
def part_one(input_data):
    """Solution for Part 1"""
    the_map, trailheads = process_input(input_data)
    total_score = 0
    for trailhead in trailheads:
        cur_reachable = reachable_tops(trailhead, the_map)
        distinct_tops_to_reach = list(set(cur_reachable))
        total_score += len(distinct_tops_to_reach)
    return total_score


@timeit
def part_two(input_data):
    """Solution for Part 2"""
    the_map, trailheads = process_input(input_data)
    total_rating = 0
    for trailhead in trailheads:
        cur_reachable = reachable_tops(trailhead, the_map)
        total_rating += len(cur_reachable)
    return total_rating


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

