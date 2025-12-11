""" Advent of code Year 2025 Day 10 solution
Link to task: https://adventofcode.com/2025/day/10
Author = Averbea
Date = 10/12/2025
"""
import re
import z3

from utils.templateutils import timeit, read_input_file
from collections import  deque

def process_input(input_data: str):
    """parses the input file and returns the result"""
    lines = []

    for line in input_data.splitlines():
        line = line.split(" ")
        # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        light_diagram, wirings, joltages = line[0], line[1:-1], line[-1]
        light_diagram = [False if x == "." else True for x in light_diagram[1:-1]]
        wirings = [tuple(map(int, re.findall(r"\d+", x))) for x in wirings]
        joltages = tuple(map(int, re.findall(r"\d+", joltages)))
        lines.append((light_diagram, wirings, joltages))
    return lines


def toggle_lamp(current_state, w):
    new_state = current_state[:]
    for lamp_index in w:
        new_state[lamp_index] = not new_state[lamp_index]
    return new_state

def get_min_presses_to_switch_lights(desired_lamp_state, wirings):
    initial_state = [False]*len(desired_lamp_state)
    to_explore = deque()
    to_explore.append((initial_state, 0))

    visited = set()
    while to_explore:
        current_state, presses = to_explore.popleft()
        state_tuple = tuple(current_state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if current_state == desired_lamp_state:
            return presses

        for w in wirings:
            new_state = toggle_lamp(current_state, w)
            to_explore.append((new_state, presses + 1))



@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    data = process_input(input_data)
    total_presses = 0
    for lamps, wirings, joltages in data:
        presses = get_min_presses_to_switch_lights(lamps, wirings)
        total_presses += presses
    return total_presses


def adjust_counters(current_state, w):
    new_state = current_state[:]
    for lamp_index in w:
        new_state[lamp_index] = new_state[lamp_index] + 1
    return new_state

def get_min_presses_to_match_counters(desired_counters, wirings):
    # Works with test data but way too slow
    initial_state = [0]*len(desired_counters)
    to_explore = deque()
    to_explore.append((initial_state, 0))

    i = 0
    visited = set()
    while to_explore:
        i+= 1
        if i % 100000 == 0:
            print("Explored states:", i, " Queue size:", len(to_explore))
            print("desired:", desired_counters)
            i = 0
        current_state, presses = to_explore.popleft()
        state_tuple = tuple(current_state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if state_tuple == desired_counters:
            print("Found solution:", presses)
            return presses

        for w in wirings:
            new_state = adjust_counters(current_state, w)
            if all(new_state[i] <= desired_counters[i] for i in range(len(desired_counters))):
                to_explore.append((new_state, presses + 1))


def get_min_presses_to_match_counters_linalg(joltages, wirings):
    vecs = []
    for w in wirings:
        vector = [0]*len(joltages)
        for lamp_index in w:
            vector[lamp_index] += 1
        vecs.append(vector)

    # solve Ax = B

    x = [z3.Int(f'B{i}') for i in range(len(wirings))]

    equations = []
    for i in range(len(joltages)):
        terms = [x[j] for j in range(len(wirings)) if i in wirings[j]]
        eq = (sum(terms) == joltages[i])
        equations.append(eq)


    optimizer = z3.Optimize()

    optimizer.minimize(sum(x)) # we are searching for the minimum number of presses


    for eq in equations:
        optimizer.add(eq)
    # each button press count must be non-negative
    for button_presses in x:
        optimizer.add(button_presses >= 0)

    optimizer.check()

    model = optimizer.model()
    return sum(model[d].as_long() for d in model.decls())


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    data = process_input(input_data)
    total_presses = 0
    for lamps, wirings, joltages in data:
        #presses = get_min_presses_to_match_counters(joltages, wirings)
        presses = get_min_presses_to_match_counters_linalg(joltages, wirings)

        total_presses += presses
    return total_presses


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

