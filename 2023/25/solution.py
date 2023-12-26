""" Advent of code Year 2023 Day 25 solution
Author = Averbea
Date = December 2023
"""
from collections import deque

from pyvis.network import Network
import networkx as nx

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file()
    map = {}
    for line in file.splitlines():
        left, right = line.split(':')
        map[left] = right.strip().split(' ')
    return map


def create_graph(data):
    graph = nx.Graph()
    for key, value in data.items():
        graph.add_node(key)
        graph.add_nodes_from(value)
    for key, value in data.items():
        for v in value:
            graph.add_edge(key, v, capacity=1)

    return graph


def visualize_graph(graph):
    net = Network()
    net.from_nx(graph)
    net.show("graph.html", notebook=False)


@timeit
def part_one():
    """Solution for Part 1"""
    data = process_input()
    graph = create_graph(data)
    visualize_graph(graph)

    # get these from looking at the graph visualization
    definetly_in_left = 'tfq'
    definetly_in_right = 'pkz'
    cut, (left, right) = nx.minimum_cut(graph, definetly_in_left, definetly_in_right)

    print(len(left) * len(right))
    return 0


@timeit
def part_two():
    """Solution for Part 2"""
    data = process_input()
    return 0


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
