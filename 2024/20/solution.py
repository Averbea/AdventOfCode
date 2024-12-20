""" Advent of code Year 2024 Day 20 solution
Link to task: https://adventofcode.com/2024/day/20
Author = Averbea
Date = 20/12/2024
"""
from collections import defaultdict
from tqdm import tqdm

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    start = None
    end = None
    path = set()
    walls = set()
    for y, row in enumerate(input_data.splitlines()):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (y, x)
                path.add(start)
            elif cell == 'E':
                end = (y, x)
                path.add(end)
            elif cell == '#':
                walls.add((y, x))
            else:
                path.add((y, x))

    path_in_order = []
    cur_score = 0
    cur = start
    while cur != end:
        path_in_order.append(cur)
        cur_score += 1

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new = (cur[0] + dy, cur[1] + dx)
            if new in path and new not in path_in_order:
                cur = new
                break
        else:
            raise ValueError("No path found")
    path_in_order.append(end)
    path_set = set(path)  # for fast lookup
    path_indices = {p: i for i, p in enumerate(path_in_order)}  # for fast lookup
    return path_in_order, path_set, path_indices, walls


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    path, path_set, path_indices, walls = process_input(input_data)
    cheats = defaultdict(int)
    for i, p in enumerate(path):
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            one_step = (p[0] + d[0], p[1] + d[1])
            two_steps = (p[0] + 2 * d[0], p[1] + 2 * d[1])
            if one_step in walls and two_steps in path_set and path_indices[two_steps] > i:
                index = path_indices[two_steps]
                cheated_secs = index - i - 2  # because it takes two seconds to move
                cheats[cheated_secs] += 1
    return sum(v for k, v in cheats.items() if k >= 100)


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    path, path_set, path_indices, walls = process_input(input_data)
    seconds_to_cheat = 20



    cheats = defaultdict(set)
    for cheat_start_index, cheat_start in enumerate(tqdm(path)):
        for dx in range(-seconds_to_cheat, seconds_to_cheat + 1):
            for dy in range(-seconds_to_cheat, seconds_to_cheat + 1):
                manhattan_distance = abs(dx) + abs(dy)
                if manhattan_distance > seconds_to_cheat:
                    continue

                cheat_end = (cheat_start[0] + dy, cheat_start[1] + dx)
                cheat = (cheat_start, cheat_end)
                if cheat_end in path_set:
                    cheated_secs = path_indices[cheat_end] - cheat_start_index - manhattan_distance
                    if cheated_secs > 0:
                        cheats[cheated_secs].add(cheat)

    return sum(len(v) for k, v in cheats.items() if k >= 100)


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))
