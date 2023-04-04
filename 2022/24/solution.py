""" Advent of code Year 2022 Day 24 solution
Author = Averbea
Date = December 2022
"""


from operator import truediv
import os
from time import time


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result


def printGrid(walls, init_blizzards, width, height, points={}, step=0):
    """print the grid with at specified step. optional draw points"""
    print("\n\nstep", step, "\n")
    blizzards = {((x + dx * step) % width, (y + dy * step) % height, dx, dy)
                 for x, y, dx, dy in init_blizzards}
    for y in range(-1, height+1):
        line = []
        for x in range(-1, width+1):
            blizz_icons = []
            if (x, y, 0, 1) in blizzards:
                blizz_icons.append('v')
            if (x, y, 0, -1) in blizzards:
                blizz_icons.append('^')
            if (x, y, -1, 0) in blizzards:
                blizz_icons.append('<')
            if (x, y, 1, 0) in blizzards:
                blizz_icons.append('>')

            if len(blizz_icons) > 1:
                line.append(str(len(blizz_icons)))
            elif len(blizz_icons) == 1:
                line.append(blizz_icons[0])
            elif (x, y) in walls:
                line.append('#')
            elif (x, y) in points:
                line.append("X")
            else:
                line.append('.')

        print(''.join(line))


DIRS = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1)
}
MOVES = {(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)}


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r') as input_file:
        lines = input_file.readlines()
    walls = set()
    blizzards = set()
    empties = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                walls.add((x-1, y-1))
            if char in DIRS:
                blizzards.add((x-1, y-1, *DIRS[char]))
            if char == '.':
                empties.append((x-1, y-1))

    start = empties[0]
    end = empties[-1]
    width = end[0] + 1
    height = end[1]

    return walls, blizzards, empties, start, end, width, height


def part_one():
    """Solution for Part 1"""
    walls, blizzards, empties, start, end, width, height = parse_input()

    walls.add((start[0], start[1] - 1))
    walls.add((end[0], end[1]+1))

    # printGrid(walls, blizzards, width, height)

    result = bfs(blizzards, walls, start, end, width, height, part=1)
    return result


def part_two():
    """Solution for Part 2"""
    walls, blizzards, empties, start, end, width, height = parse_input()

    walls.add((start[0], start[1] - 1))
    walls.add((end[0], end[1]+1))

    # printGrid(walls, blizzards, width, height)

    result = bfs(blizzards, walls, start, end, width, height, part=2)
    return result


def bfs(blizzards, walls, start, end, width, height, part=1):
    if part == 1:
        waypoints = [end]
    else:
        waypoints = [end, start, end]
    step = 0
    points = {start}
    while len(waypoints) > 0:
        step += 1
        move_to = {(x + dx, y + dy) for x, y in points for dx, dy in MOVES}
        new_blizzards = {((x + dx * step) % width, (y + dy * step) % height)
                         for x, y, dx, dy in blizzards}
        points = move_to - new_blizzards - walls
        if waypoints[0] in points:
            points = {waypoints[0]}
            waypoints.pop(0)
    return step


def main():
    """main method"""
    time_needed, result = measure_timing(part_one)

    print("Part One : " + str(result))
    print("time elapsed: " + str(time_needed))

    time_needed, result = measure_timing(part_two)
    print("\nPart Two : " + str(result))
    print("time elapsed: " + str(time_needed))


if __name__ == "__main__":
    main()
