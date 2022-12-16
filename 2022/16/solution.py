""" Advent of code Year 2022 Day 16 solution
Author = Averbea
Date = December 2022
"""


from collections import defaultdict
from copy import deepcopy
import dataclasses
import math
import os
import re
from time import time
from turtle import distance
from typing import DefaultDict


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result


@dataclasses.dataclass
class Valve:
    """dataclass representing a valve"""
    name: str
    flow_rate: int
    to: list[str]


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read().splitlines()
    valves = defaultdict()

    for line in inputs:
        matches = re.match(
            r"Valve (\w*) has flow rate=(\d*); tunnels? leads? to valves? (.*)", line)
        if not matches:
            exit(-1)
        groups = matches.groups()
        valve = groups[0]
        flow_rate = int(groups[1])
        edges = groups[2].split(", ")
        cur_valve = Valve(valve, flow_rate, edges)
        valves[cur_valve.name] = cur_valve
    return valves


def try_all(rounds_left: int, cur_valve: Valve, valves_not_open: list[Valve], distances: dict[str, dict[str, int]]):
    """try all combinations of opening valves recursively"""
    if rounds_left <= 0:
        return 0
    score = 0
    for i, to_open in enumerate(valves_not_open):
        cur_not_open = valves_not_open[:i] + valves_not_open[i+1:]

        cur_rounds_left = rounds_left - distances[cur_valve.name][to_open.name] - 1
        if cur_rounds_left <= 0:
            continue
        cur_pres_rel = try_all(cur_rounds_left, to_open, cur_not_open, distances)
        score = max(score, to_open.flow_rate * cur_rounds_left +  cur_pres_rel)
    return score

def get_distances(valves: DefaultDict):
    distances = {}
    for valve1 in valves.values():
        distances[valve1.name] = {
            valve2.name: math.inf for valve2 in valves.values()}

        # init distance to self with 0, distance to neighboring valves with 1
        distances[valve1.name][valve1.name] = 0
        for neighbor in valve1.to:
            distances[valve1.name][neighbor] = 1
    # find all distances
    # TODO this should probably use BFS but it seems to work (nodes have a max difference of 2)
    for valve1 in valves.values():
        for valve2 in valves.values():
            for valve3 in valves.values():
                distances[valve2.name][valve3.name] = min(
                    distances[valve2.name][valve3.name], distances[valve2.name][valve1.name] + distances[valve1.name][valve3.name])

    return distances

def part_one():
    """Solution for Part 1"""
    valves = parse_input()
    distances = get_distances(valves)

    valves_unopened = [valve for valve in valves.values() if valve.name != "AA" and valve.flow_rate > 0]
    max_pressure_released = try_all(30, valves["AA"],valves_unopened , distances)

    return max_pressure_released

def try_all_together(
    remaining_time: int,
    e_travel_length: int, 
    p_travel_length: int, 
    e_cur_valve: Valve,
    p_cur_valve: Valve,
    unopened_valves: list[Valve],
    distances: dict[str, dict[str, int]]
    ):
    # TODO this is way to slow.....
    water_released = 0
       
    if p_travel_length == e_travel_length == 0:
        # both are not travelling
        for e_next_valve in unopened_valves: 
            for p_next_valve in unopened_valves:
                if e_next_valve == p_next_valve: 
                    # do not go to the same valve
                    continue
                # copy unopened values and remove both new valves
                tmp_unopened_valves = deepcopy(unopened_valves)
                tmp_unopened_valves.remove(p_next_valve)
                tmp_unopened_valves.remove(e_next_valve)

                new_water_released = try_all_together(remaining_time -1, distances[e_cur_valve.name][e_next_valve.name], distances[p_cur_valve.name][p_next_valve.name], e_next_valve, p_next_valve, tmp_unopened_valves, distances)
                water_released = max(water_released, new_water_released)
    elif p_travel_length == 0:
        water_released += p_cur_valve.flow_rate * (remaining_time-1)
        for p_next_valve in unopened_valves:
            tmp_unopened_valves = deepcopy(unopened_valves)
            tmp_unopened_valves.remove(p_next_valve)
            new_water_released = try_all_together(remaining_time-1, e_travel_length-1, distances[p_cur_valve.name][p_next_valve.name], e_cur_valve, p_next_valve, tmp_unopened_valves, distances)
            water_released = max(water_released, new_water_released)
        # elephant is still traveling
    elif e_travel_length == 0:
        water_released += e_cur_valve.flow_rate * (remaining_time-1)
        for e_next_valve in unopened_valves:
            tmp_unopened_valves = deepcopy(unopened_valves)
            tmp_unopened_valves.remove(e_next_valve)
            new_water_released = try_all_together(remaining_time-1, distances[e_cur_valve.name][e_next_valve.name], p_travel_length-1, e_next_valve, p_cur_valve, tmp_unopened_valves, distances)
            water_released = max(water_released, new_water_released)
        # p is still traveling
    else: 
        # both are still traveling
        water_released =  try_all_together(remaining_time-1, e_travel_length-1, p_travel_length-1, e_cur_valve, p_cur_valve, unopened_valves, distances)
  

    return water_released

def part_two():
    """Solution for Part 2"""
    valves = parse_input()

    distances = get_distances(valves)
    valves_unopened = [valve for valve in valves.values() if valve.name != "AA" and valve.flow_rate > 0]
    
    tmp = try_all_together(26, 0,0, valves["AA"], valves["AA"], valves_unopened, distances )
    return 0


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

