""" Advent of code Year 2024 Day 5 solution
Link to task: https://adventofcode.com/2024/day/5
Author = Averbea
Date = 05/12/2024
"""
import re
from collections import defaultdict

import networkx as nx

from utils.templateutils import timeit, read_input_file


def process_input(input_data) :
    """parses the input file and returns the result"""
    rules, updates = input_data.split("\n\n")
    rules = re.findall(r"\d+", rules)
    # ever two numbers are in sublist
    rules = [[int(rules[i]), int(rules[i + 1]) ]for i in range(0, len(rules), 2)]
    updates = updates.split("\n")
    updates = [[int(x) for x in re.findall(r"\d+", update)] for update in updates]


    return rules, updates

def filter_correct(rules, updates):
    dict_rules = defaultdict(set)
    for (left, right) in rules:
        dict_rules[left].add(right)

    correct, not_correct = [], []
    for update in updates:
        is_correct = True
        seen = set()
        for num in update:
            must_be_before_all = dict_rules.get(num, {})
            if any([b in seen for b in must_be_before_all]):
                is_correct = False
                break
            seen.add(num)

        if is_correct:
            correct.append(update)
        else:
            not_correct.append(update)

    return correct, not_correct

def sum_of_middles(updates):
    sum_of_middles = 0
    for update in updates:
        middle_index = int((len(update) - 1) / 2)
        sum_of_middles += update[middle_index]
    return sum_of_middles


@timeit
def part_one(input_data):
    """Solution for Part 1"""
    rules, updates = process_input(input_data)
    correct, not_correct = filter_correct(rules, updates)

    return sum_of_middles(correct)


@timeit
def part_two(input_data):
    """Solution for Part 2"""
    rules, updates = process_input(input_data)
    _, not_correct = filter_correct(rules, updates)
    reordered  =[]
    for update in not_correct:
            reordered.append(list(
            nx.topological_sort(
                nx.DiGraph((a, b) for (a, b) in rules if a in update and b in update)
            )
        ))
    return sum_of_middles(reordered)


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

