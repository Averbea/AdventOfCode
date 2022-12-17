""" Advent of code Year 2022 Day 17 solution
Author = Averbea
Date = December 2022
"""


from collections import defaultdict
import os
from time import time


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read()
    return inputs


def visualize(blocked, falling_rock):
    """visualize the data"""
    max_height = max_blocked_height(blocked) + 10

    for y_pos in reversed(range(max_height)):
        if y_pos == 0:
            print("+-------+")
            continue
        line = '|'
        for x_pos in range(7):
            if (x_pos, y_pos) in blocked:
                line = line + '#'
            elif (x_pos, y_pos) in falling_rock:
                line = line + '@'
            else:
                line = line + '.'
        line = line + '|'
        print(line)


def get_rock_at_tick(tick):
    """get the rock at tick and next tick"""
    rocks = [
        # the minus rock
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        # the plus rock
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        # the l rock
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        # the i rock
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        # the square rock
        [(0, 0), (1, 0), (0, 1), (1, 1)],
    ]
    return rocks[tick % len(rocks)], (tick+1) % len(rocks)


def get_push_dir_at_tick(tick: int, data):
    """get push direction at tick. Also return new tick"""
    return -1 if data[tick % len(data)] == "<" else 1, (tick+1) % len(data)


def get_all_at_height(blocked, height):
    """get a list of all blocks at given height"""
    return list(filter(lambda x: x[1] == height, blocked))


def max_blocked_height(blocked):
    """get max height in blocked"""
    return max(blocked, key=lambda x: x[1])[1]


def move(rock: list[tuple[int, int]], dir_x=0, dir_y=0):
    """move given rock according to dir_x, dir_y"""
    new_positions = []
    for pos in rock:
        new_positions.append((pos[0] + dir_x, pos[1] + dir_y))
    return new_positions


def collides(blocked: set[tuple[int, int]], rock: list[tuple[int, int]]):
    """check if rock collides with border or other blocks"""
    for pos in rock:
        if pos in blocked:
            return True
        if pos[0] < 0:
            return True
        if pos[0] >= 7:
            return True
    return False


def solve(data, iterations):
    """solve the problem with given data and iterations"""

    blocked = set([(x, int(0)) for x in range(7)])

    seen = defaultdict()

    cur_iteration = 0

    next_gas_tick = 0
    next_rock_tick = 0

    while cur_iteration < iterations:
        # simulate rock

        new_rock_offsets, next_rock_tick = get_rock_at_tick(next_rock_tick)
        max_height = max_blocked_height(blocked)

        if len(get_all_at_height(blocked, max_height)) == 7:
            # the last row is fully blocked (this pattern repeats throughout the iterations)
            key = str(next_rock_tick) + "_" + str(next_gas_tick)
            entry = seen.get(key)
            if entry is not None:
                # if this entry has been seen calc diff in iteration and height
                iter_dif = cur_iteration - entry["iteration"]
                heihgt_dif = max_height - entry["height"]
                # calculate how many times this would repeat
                iterations_to_go = iterations - cur_iteration
                times_fit_in = iterations_to_go // iter_dif

                # update max height and cur_iteration
                max_height += heihgt_dif * times_fit_in
                cur_iteration += iter_dif * times_fit_in
                # add a row at new max_height to blocked
                row = [(x, max_height) for x in range(7)]
                blocked.update(row)
            else:
                # remember this state
                seen[key] = {"height": max_height,
                               "iteration": cur_iteration}


        start_pos = (2, max_height + 4)

        rock_positions = []
        for offset in new_rock_offsets:
            rock_positions.append(
                (start_pos[0] + offset[0], start_pos[1] + offset[1]))

        # visualize(blocked, rock_positions)
        while True:
            # _______________push by gas vents_________________________
            push_dir, next_gas_tick = get_push_dir_at_tick(next_gas_tick, data)

            new_rock_positions = move(rock_positions, dir_x=push_dir)

            if collides(blocked, new_rock_positions):
                # we would go into the wall. Use old positions
                new_rock_positions = rock_positions

            # ________________Move down ______________________________
            fallen_rock_positions = move(new_rock_positions, dir_y=-1)

            if collides(blocked, fallen_rock_positions):
                blocked.update(new_rock_positions)
                break

            rock_positions = fallen_rock_positions

        cur_iteration += 1
    # visualize(blocked, [])
    return max_blocked_height(blocked)


def part_one():
    """Solution for Part 1"""
    data = parse_input()

    return solve(data, 2022)


def part_two():
    """Solution for Part 2"""
    data = parse_input()

    return solve(data, 1000000000000)


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
