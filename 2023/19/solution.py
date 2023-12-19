""" Advent of code Year 2023 Day 19 solution
Author = Averbea
Date = December 2023
"""
import math

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


def workflow_result(workflow, item):
    x, m, a, s = item
    for condition, next in workflow:
        if eval(condition):
            return next


def get_rating_for_part(workflows, part):
    next_workflow = 'in'
    while next_workflow not in ['A', 'R']:
        next_workflow = workflow_result(workflows[next_workflow], part)
    if next_workflow == 'A':
        return sum(part)
    return 0


@timeit
def part_one():
    """Solution for Part 1"""
    workflows, parts = process_input()
    return sum(get_rating_for_part(workflows, part) for part in parts)


def get_workflow_ranges(workflows):
    """convert workflow conditions to ranges"""
    ranges = []
    for condition, next in workflows[:-1]:
        if '>' in condition:
            symbol, number = condition.split('>')
            cur_range = (int(number) + 1, math.inf)
        elif '<' in condition:
            symbol, number = condition.split('<')
            cur_range = (0, int(number) - 1)
        else:
            raise ValueError("Condition ", condition, " not valid")
        ranges.append((symbol, cur_range, next))
    ranges.append(workflows[-1])
    return ranges


def index(c):
    return "xmas".index(c)


def get_overlaps(category_range, range_in_step):
    left = (category_range[0], range_in_step[0] - 1)
    left = left if left[0] <= left[1] else None

    inside = (max(category_range[0], range_in_step[0]), min(category_range[1], range_in_step[1]))
    # inside = inside if inside[0] <= inside[1] else None

    right = (range_in_step[1] + 1, category_range[1])
    right = right if right[0] <= right[1] else None

    return left, inside, right


def replace_idx_in_tuple(tup, idx, value):
    return tup[:idx] + (value,) + tup[idx + 1:]


def amount_in_tuple(t):
    a = t[1]
    amount = t[0][1] - t[0][0] + 1
    for i in range(1, len(t)):
        amount *= t[i][1] - t[i][0] + 1
    return amount


@timeit
def part_two():
    """Solution for Part 2"""
    workflows, parts = process_input()
    range_workflows = {key: get_workflow_ranges(workflow) for key, workflow in workflows.items()}

    # start at in and explore all possible ranges
    parts_to_explore = [('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000))]

    accepted_count = 0
    while parts_to_explore:
        wf_and_part = parts_to_explore.pop()
        cur_wf_name, cur_part = wf_and_part[0], wf_and_part[1:]
        cur_wf = range_workflows[cur_wf_name]
        ranges_to_check = [cur_part]

        for step in cur_wf[:-1]:
            new_ranges = []
            for part_ranges in ranges_to_check:
                category, range_in_step, next_wf_name = step
                category_idx = index(category)
                category_range = part_ranges[category_idx]

                left_outside, inside, right_outside = get_overlaps(category_range, range_in_step)
                if inside:
                    if next_wf_name == 'A':
                        accepted_count += amount_in_tuple(replace_idx_in_tuple(part_ranges, category_idx, inside))
                    elif next_wf_name != 'R':
                        parts_to_explore.append(
                            (next_wf_name, *replace_idx_in_tuple(part_ranges, category_idx, inside)))

                if left_outside:
                    new_ranges.append(replace_idx_in_tuple(part_ranges, category_idx, left_outside))
                if right_outside:
                    new_ranges.append(replace_idx_in_tuple(part_ranges, category_idx, right_outside))
            ranges_to_check = new_ranges

        next_wf = cur_wf[-1][1]
        for part_ranges in ranges_to_check:
            if next_wf == 'A':
                accepted_count += amount_in_tuple(part_ranges)
            elif next_wf != 'R':
                parts_to_explore.append((cur_wf[-1][1], *part_ranges))

    return accepted_count


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
