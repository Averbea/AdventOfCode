""" Advent of code Year 2022 Day 19 solution
Author = Averbea
Date = December 2022
"""


from copy import copy
from dataclasses import dataclass
import os
from time import time


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result


@dataclass
class RobotType:
    """represents a Robot
    """
    name: str
    ore_cost: int
    clay_cost: int
    obsidian_cost: int


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read().splitlines()

    data = []
    for line in inputs:
        words = line.split()
        ore_cost = int(words[6])
        clay_cost = int(words[12])
        obsidian_cost_ore, obsidian_cost_clay = int(words[18]), int(words[21])
        geode_cost_ore, geode_cost_obsidian = int(words[27]), int(words[30])

        ore_robot = RobotType("ore", ore_cost, 0, 0)
        clay_robot = RobotType("clay", clay_cost, 0, 0)
        obsidian_robot = RobotType(
            "obsidian", obsidian_cost_ore, obsidian_cost_clay, 0)
        geode_robot = RobotType("geode", geode_cost_ore,
                                0, geode_cost_obsidian)

        data.append([ore_robot, clay_robot, obsidian_robot, geode_robot])

    return data


def step_time(ores, robots):
    """make a time step"""
    new_ores = copy(ores)
    for i in range(4):
        new_ores[i] += robots[i]
    return new_ores


def can_buy_robot(ores, robot_type: RobotType):
    """check if given robot type can be bought"""
    if ores[0] >= robot_type.ore_cost and \
            ores[1] >= robot_type.clay_cost and \
            ores[2] >= robot_type.obsidian_cost:
        return True
    return False


def buy_robot(old_ores, old_robots, robot: RobotType):
    """buy given robot and return new ores and robots array"""
    ores = copy(old_ores)
    ores[0] -= robot.ore_cost
    ores[1] -= robot.clay_cost
    ores[2] -= robot.obsidian_cost
    assert ores[0] >= 0
    assert ores[1] >= 0
    assert ores[2] >= 0

    robots = copy(old_robots)
    indizes = ["ore", "clay", "obsidian", "geode"]
    robots[indizes.index(robot.name)] += 1

    return ores, robots


def dfs(robot_types: list[RobotType], cache: dict, time_amount: int, ores, robots, max_ore_cost, max_clay_cost, max_obsidian_cost):
    """depth first search to find solution"""
    assert time_amount >= 0
    # print(robots)
    max_geodes = ores[3]

    if time_amount == 0:
        return max_geodes
    key = tuple([time_amount, *ores, *robots])

    if key in cache.keys():
        return cache[key]

    for robot in robot_types:
        if robot.name == "ore" and robots[0] >= max_ore_cost:
            continue
        if robot.name == "clay" and robots[1] >= max_clay_cost:
            continue
        if robot.name == "obsidian" and robots[2] >= max_clay_cost:
            continue
        new_ores = copy(ores)
        new_robots = copy(robots)
        new_time = time_amount
        if can_buy_robot(new_ores, robot):
            new_ores, new_robots = buy_robot(new_ores, new_robots, robot)
        else:
            while new_time > 1 and not can_buy_robot(new_ores, robot):
                new_ores = step_time(new_ores, new_robots)
                new_time -= 1
            if can_buy_robot(new_ores, robot):
                new_ores, new_robots = buy_robot(new_ores, new_robots, robot)

        new_ores = step_time(new_ores, robots)
        new_time = new_time - 1
        result = dfs(robot_types, cache, new_time, new_ores,
                     new_robots, max_ore_cost, max_clay_cost, max_obsidian_cost)
        max_geodes = max(max_geodes, result)

    cache[key] = max_geodes
    return max_geodes


def solve(max_time, part2):
    """solve the problem for given time"""
    blueprints = parse_input()
    sum_quality_levels = 0
    product_opened_geodes = 1
    for i, blueprint in enumerate(blueprints, start=1):
        if part2 and i > 3:
            continue
        print("Blueprint", i)
        max_ore_cost = 0
        max_clay_cost = 0
        max_obsidian_cost = 0
        for robot in blueprint:
            max_ore_cost = max(max_ore_cost, robot.ore_cost)
            max_clay_cost = max(max_clay_cost, robot.clay_cost)
            max_obsidian_cost = max(max_obsidian_cost, robot.obsidian_cost)

        initial_ores = [0, 0, 0, 0]
        initial_robots = [1, 0, 0, 0]
        opened_geodes = dfs(blueprint, {}, max_time, initial_ores,
                            initial_robots, max_ore_cost, max_clay_cost, max_obsidian_cost)
        product_opened_geodes *= opened_geodes
        sum_quality_levels += opened_geodes * i
        print("\tcan open up to", opened_geodes, "geodes")
    return product_opened_geodes if part2 else sum_quality_levels


def part_one():
    """Solution for Part 1"""
    return solve(24, False)


def part_two():
    """Solution for Part 2"""
    # data = parse_input()
    return solve(32, True)


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
