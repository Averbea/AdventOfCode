""" Advent of code Year 2024 Day 16 solution
Link to task: https://adventofcode.com/2024/day/16
Author = Averbea
Date = 16/12/2024
"""
import math
from collections import defaultdict

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    walls = set()
    start, end = None, None
    for y, line in enumerate(input_data.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            if char == "S":
                start = (x, y)
            if char == "E":
                end = (x, y)


    return walls, start, end


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    walls, start, end = process_input(input_data)
    to_explore = [(start, (1,0), 0)]
    visited = defaultdict(int)
    while to_explore:
        pos, facing_dir, score_at_pos = to_explore.pop()

        # turn left and right
        cur_idx = DIRECTIONS.index(facing_dir)
        for new_dir in [DIRECTIONS[(cur_idx -1) % 4], DIRECTIONS[(cur_idx +1)%4]]:
            cur_entry = visited.get((pos, new_dir), math.inf)
            new_score = score_at_pos + 1000
            if cur_entry > score_at_pos + 1000:
                to_explore.append((pos, new_dir, new_score))
                visited[(pos, new_dir)] = new_score

        # move forward
        new_pos = (pos[0] + facing_dir[0], pos[1] + facing_dir[1])
        new_score = score_at_pos + 1
        if new_pos not in walls and visited.get((new_pos, facing_dir), math.inf) > new_score:
            to_explore.append((new_pos, facing_dir, new_score))
            visited[(new_pos, facing_dir)] = new_score

    return min(visited.get((end, d), math.inf) for d in DIRECTIONS)


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    walls, start, end = process_input(input_data)
    to_explore = [((start,), (1, 0), 0)]
    visited = defaultdict(int)
    paths_to_end = set()
    while to_explore:
        path, facing_dir, score_at_pos = to_explore.pop()
        pos = path[-1]

        if pos == end:
            paths_to_end.add((path, score_at_pos))

        # turn left and right
        cur_idx = DIRECTIONS.index(facing_dir)
        for new_dir in [DIRECTIONS[(cur_idx - 1) % 4], DIRECTIONS[(cur_idx + 1) % 4]]:
            cur_entry = visited.get((pos, new_dir), math.inf)
            new_score = score_at_pos + 1000
            if cur_entry >= score_at_pos + 1000:
                to_explore.append((path, new_dir, new_score))
                visited[(pos, new_dir)] = new_score

        # move forward
        new_pos = (pos[0] + facing_dir[0], pos[1] + facing_dir[1])
        new_score = score_at_pos + 1
        if new_pos not in walls and visited.get((new_pos, facing_dir), math.inf) >= new_score:
            to_explore.append((path + (new_pos,), facing_dir, new_score))
            visited[(new_pos, facing_dir)] = new_score

    min_score = min(visited.get((end, d), math.inf) for d in DIRECTIONS)

    all_best_paths = [p for p, s in paths_to_end if s == min_score]

    tiles_at_best_paths = set()
    for path in all_best_paths:
        for pos in path:
            tiles_at_best_paths.add(pos)
    return len(tiles_at_best_paths)


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

