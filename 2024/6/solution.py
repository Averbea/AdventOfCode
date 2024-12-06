""" Advent of code Year 2024 Day 6 solution
Link to task: https://adventofcode.com/2024/day/6
Author = Averbea
Date = 06/12/2024
"""
from utils.templateutils import timeit, read_input_file


def process_input(input_data):
    """parses the input file and returns the result"""

    obstacles = set()
    lines = input_data.splitlines()
    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1
    start_pos = None
    for y, line in enumerate(input_data.splitlines()):
        obstacle_indices = [i for i, c in enumerate(line) if c == "#"]
        if "^" in line:
            start_pos = (line.index("^"), y)

        for x in obstacle_indices:
            obstacles.add((x, y))

    return (max_x, max_y), start_pos, obstacles


DIRECTIONS = {
    "N": (0, -1),
    "S": (0, 1),
    "W": (-1, 0),
    "E": (1, 0)
}


def get_next_direction(cur_dir: str):
    return "NESW"[("NESW".index(cur_dir) + 1) % 4]


def move(cur_pos, direction):
    return cur_pos[0] + DIRECTIONS[direction][0], cur_pos[1] + DIRECTIONS[direction][1]


def simulate_p1(max_x, max_y, start_pos, obstacles):
    cur_pos = start_pos
    direction = "N"

    visited = set()
    while is_in_bounds(cur_pos, max_x, max_y):
        visited.add(cur_pos)
        next_pos = move(cur_pos, direction)
        if next_pos in obstacles:
            # turn instead of moving
            direction = get_next_direction(direction)
        else:
            cur_pos = next_pos
    return visited


@timeit
def part_one(input_data):
    """Solution for Part 1"""
    (max_x, max_y), start_pos, obstacles = process_input(input_data)
    return len(simulate_p1(max_x, max_y, start_pos, obstacles))


def is_in_bounds(pos, max_x, max_y):
    return 0 <= pos[0] <= max_x and 0 <= pos[1] <= max_y


@timeit
def part_two(input_data):
    """Solution for Part 2"""
    (max_x, max_y), start_pos, obstacles = process_input(input_data)

    tiles_on_original_path = simulate_p1(max_x, max_y, start_pos, obstacles)

    obstacles_for_loop = set()
    obstacles_backup = obstacles.copy()

    for (new_obstacle_x, new_obstacle_y) in tiles_on_original_path:
        if (new_obstacle_x, new_obstacle_y) == start_pos:
            continue  # the guard is here, so we can't put an obstacle here

        obstacles = obstacles_backup.copy()
        obstacles.add((new_obstacle_x, new_obstacle_y))

        visited = set()
        cur_pos = start_pos
        direction = "N"
        while is_in_bounds(cur_pos, max_x, max_y):
            visited.add((cur_pos[0], cur_pos[1], direction))
            next_pos = move(cur_pos, direction)

            if (next_pos[0], next_pos[1], direction) in visited:
                # loop detected
                obstacles_for_loop.add((new_obstacle_x, new_obstacle_y))
                break
            if next_pos in obstacles:
                # turn instead
                direction = get_next_direction(direction)
            else:
                cur_pos = next_pos
        else:
            # no loop detected
            pass

    return len(obstacles_for_loop)


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))
