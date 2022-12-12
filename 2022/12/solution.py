""" Advent of code Year 2022 Day 12 solution
Author = Averbea
Date = December 2022
"""


import math
import os
from time import time


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result


class Node:
    """class representing a Node"""

    def __init__(self, pos: tuple[int, int], predecessor=None) -> None:
        self.pos = pos
        self.predecessor = predecessor

        self.dist_to_start = 0

    def __eq__(self, other) -> bool:
        return self.pos == other.pos

    def __repr__(self) -> str:
        return str(self.pos)


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read().splitlines()
    grid = list(map(lambda el: [*el], inputs))
    return grid


def get_starting_s_and_end(grid):
    """get S as starting positions and end position"""
    start = end = None
    for y_pos, line in enumerate(grid):
        for x_pos, col in enumerate(line):
            if col == "S":
                start = (y_pos, x_pos)
            if col == "E":
                end = (y_pos, x_pos)
    assert start is not None
    assert end is not None
    return start, end


def get_starting_positions_and_end(grid):
    """get S and all occurences of a as starting position and end position"""
    starts = []
    end = None
    for y_pos, line in enumerate(grid):
        for x_pos, col in enumerate(line):
            if col == "S" or col == "a":
                starts.append((y_pos, x_pos))
            if col == "E":
                end = (y_pos, x_pos)
    assert starts is not None
    assert end is not None
    return starts, end


def lookup(char):
    """get comparable values for chars"""

    if char == "E":
        char = "z"
    if char == "S":
        char = "a"

    return ord(char)


def get_neighbors(data: list[list[str]], cur_pos: tuple[int, int]):
    """get neighbor positions for cur_pos in data"""

    neighbors = []

    y_pos, x_pos = cur_pos
    cur_data = data[y_pos][x_pos]
    cur_val = lookup(cur_data)
    height = len(data)
    width = len(data[0])

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    for dir_y, dir_x in directions:
        if 0 <= y_pos + dir_y < height and 0 <= x_pos + dir_x < width:
            neighbor_data = data[y_pos + dir_y][x_pos + dir_x]
            neighbor_val = lookup(neighbor_data)
            if neighbor_val <= cur_val + 1:
                neighbors.append((y_pos + dir_y, x_pos+dir_x))

    return neighbors


def heuristic(position: tuple[int, int], target: tuple[int, int]):
    """heuristic function"""
    return abs(target[0] - position[0]) + abs(target[1] - position[1])


def total_cost(node: Node, target: tuple[int, int]):
    """calculate the total cost to end node"""
    return node.dist_to_start + heuristic(node.pos, target)


def a_star(data: list[list[str]], start_pos: tuple[int, int], end_pos: tuple[int, int]):
    """A star algorithm"""
    start_node = Node(start_pos)
    end_node = Node(end_pos)
    # open list contains start node
    open_list: list[Node] = [start_node]
    # closed list is initially empty
    closed_list: list[Node] = []

    # until there are no nodes to explore
    while len(open_list) > 0:
        # get node with minimum total cost from open_list
        cur_node = open_list[0]
        cur_index = 0
        for index, node in enumerate(open_list):
            if total_cost(node, end_pos) < total_cost(cur_node, end_pos):
                cur_node = node
                cur_index = index
        open_list.pop(cur_index)

        if cur_node.pos == end_node.pos:
            # Backtrack to get path
            path = [cur_node.pos]
            while cur_node is not None:
                path.append(cur_node.pos)
                cur_node = cur_node.predecessor

            return path[1:-1][::-1]

        # add this node to closed list
        closed_list.append(cur_node)

        # Expand node
        neighbor_positions = get_neighbors(data, cur_node.pos)
        for neighbor_pos in neighbor_positions:
            neighbor_node = Node(neighbor_pos, cur_node)

            # if this neighbor is closed it there is nothing to do
            if neighbor_node in closed_list:
                continue

            # calculate new distance
            new_distance = cur_node.dist_to_start + 1

            # if new node is in open list and has a smaller distance there is nothing to do

            if neighbor_node in open_list:
                index = open_list.index(neighbor_node)
                if new_distance >= open_list[index].dist_to_start:
                    continue

            # set predecessor and current node
            neighbor_node.predecessor = cur_node
            neighbor_node.dist_to_start = new_distance

            # add node to open list
            open_list.append(neighbor_node)
    return []


def part_one():
    """Solution for Part 1"""
    data = parse_input()

    start_pos, end_pos = get_starting_s_and_end(data)
    path = a_star(data, start_pos, end_pos)
    return len(path)


def part_two():
    """Solution for Part 2"""
    data = parse_input()

    starting_positions, end_pos = get_starting_positions_and_end(data)
    paths = []

    for i, start_pos in enumerate(starting_positions):
        print(i, "/", len(starting_positions))
        path = a_star(data, start_pos, end_pos)
        paths.append(path)

    minimum = math.inf
    print("done")
    for path in paths:
        if len(path) != 0:
            minimum = min(len(path), minimum)

    return minimum


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
