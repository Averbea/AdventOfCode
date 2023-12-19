""" Advent of code Year 2023 Day 19 solution
Author = Averbea
Date = December 2023
"""

from utils.templateutils import timeit, read_input_file
import re


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)

    workflows_strings, parts = file.split("\n\n")
    workflows_strings = workflows_strings.splitlines()
    workflows = {}
    for workflow in workflows_strings:
        splits = workflow[:-1].split("{")
        name = splits[0]
        operations_strings = splits[1:]
        operations = []
        for op_string in operations_strings:
            all_strs = op_string.split(',')
            for i in range(len(all_strs) - 1):
                operations.append(all_strs[i].split(':'))
            operations.append(['True', all_strs[-1]])

        workflows[name] = operations
    parts = [list(map(int, re.findall(r'\d+', part))) for part in parts.splitlines()]

    return workflows, parts


def item_workflow(workflow, item):
    x, m, a, s = item
    for condition, next in workflow:
        if eval(condition):
            return next


@timeit
def part_one():
    """Solution for Part 1"""
    workflows, parts = process_input()
    starting_workflow = 'in'
    sum_of_ratings = 0
    for part in parts:
        print("checking part", part)
        next_workflow = starting_workflow
        while next_workflow not in ['A', 'R']:
            next_workflow = item_workflow(workflows[next_workflow], part)
        if next_workflow == 'A':
            sum_of_ratings += sum(part)
    return sum_of_ratings


@timeit
def part_two():
    """Solution for Part 2"""
    workflows, parts = process_input()
    return 0


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
