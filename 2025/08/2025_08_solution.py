""" Advent of code Year 2025 Day 8 solution
Link to task: https://adventofcode.com/2025/day/8
Author = Averbea
Date = 08/12/2025
"""
from collections import defaultdict
from functools import reduce
from math import sqrt

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    lines = input_data.splitlines()
    lines = [line.split(",") for line in lines]
    lines = [tuple(map(int, line)) for line in lines]
    return set(lines)


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    points = process_input(input_data)

    distances = defaultdict(tuple)
    seen = set()
    for d in points:
        seen.add(d)
        for other in points - seen:
            distance = get_distance(d, other)
            distances[distance] = tuple([d,other])


    circuits = []
    sorted_keys = sorted(distances.keys())
    rng = 10 if TEST else 1000
    for i in range(rng):
        minimal_key = sorted_keys.pop(0)
        a, b = distances[minimal_key]

        as_circuit = None
        bs_circuit = None
        for c in circuits:
            if a in c:
                as_circuit = c
            if b in c:
                bs_circuit = c
        if as_circuit and not bs_circuit:
            as_circuit.add(b)
        elif bs_circuit and not as_circuit:
            bs_circuit.add(a)
        elif not as_circuit and not bs_circuit:
            circuits.append({a,b})
        elif as_circuit and bs_circuit and as_circuit != bs_circuit:
            as_circuit.update(bs_circuit)
            circuits.remove(bs_circuit)

    boxes_in_circuits = 0
    for c in circuits:
        boxes_in_circuits += len(c)

    circuit_count = len(circuits) + (len(points) - boxes_in_circuits)
    print("created ", circuit_count, "circuits")

    circuits.sort(key=len, reverse=True)
    return reduce(lambda x,y: x*y, map(len,circuits[:3]))

def get_distance(a ,b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2 )
@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    points = process_input(input_data)

    distances = defaultdict(tuple)
    seen = set()
    for d in points:
        seen.add(d)
        for other in points - seen:
            distance = get_distance(d, other)
            distances[distance] = tuple([d, other])

    circuits = []
    sorted_keys = sorted(distances.keys())

    while True:
        minimal_key = sorted_keys.pop(0)
        a, b = distances[minimal_key]

        as_circuit = None
        bs_circuit = None
        for c in circuits:
            if a in c:
                as_circuit = c
            if b in c:
                bs_circuit = c
        if as_circuit and not bs_circuit:
            as_circuit.add(b)
        elif bs_circuit and not as_circuit:
            bs_circuit.add(a)
        elif not as_circuit and not bs_circuit:
            circuits.append({a, b})
        elif as_circuit and bs_circuit and as_circuit != bs_circuit:
            as_circuit.update(bs_circuit)
            circuits.remove(bs_circuit)

        if len(circuits) == 1 and len(circuits[0]) == len(points):
            return a[0] * b[0]

TEST = False
if __name__ == "__main__":
    file_content = read_input_file(test=TEST)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

