""" Advent of code Year 2023 Day 12 solution
Author = Averbea
Date = December 2023
"""
from functools import cache
from typing import Tuple

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False).splitlines()
    output = []
    for line in file:
        springs, groups = line.split(" ")
        groups = tuple([int(num) for num in groups.split(",")])
        output.append([springs, groups])

    return output


def get_groups_for_springs(springs):
    groups = []
    for i in range(len(springs)):
        if i > 0 and springs[i] == springs[i - 1] == '#':
            groups[-1] += 1
        elif springs[i] == '#':
            groups.append(1)
    return groups


def calc_variations_old(springs: str, groups: Tuple[int]):
    """first solution.... very slow"""
    if springs.count('?') == 0:
        cur_groups = get_groups_for_springs(springs)
        if groups == cur_groups:
            return 1
        else:
            return 0
    # replace first occurence of ? in springs with #
    idx = springs.index('?')
    new_true = springs[:idx] + '#' + springs[idx + 1:]
    new_false = springs[:idx] + '.' + springs[idx + 1:]
    return calc_variations_old(new_true, groups) + calc_variations_old(new_false, groups)


@cache
def calc_variations(springs: str, groups: Tuple[int]):
    if len(springs) == 0:
        if len(groups) == 0:
            return 1
        else:
            return 0

    cur = springs[0]

    if cur == '?':
        return calc_variations('#' + springs[1:], groups) + calc_variations('.' + springs[1:], groups)
    if cur == '.':
        return calc_variations(springs.lstrip('.'), groups)

    if cur == '#':
        if len(groups) == 0 or len(springs) < groups[0]:
            return 0
        next_group_length = groups[0]

        if '.' in springs[0:next_group_length]:     # group is shorter than expected
            return 0
        if len(springs) > next_group_length and springs[next_group_length] == '#':       # group is longer than expected
            return 0
        if len(springs) > groups[0]:
            if springs[groups[0]] == "?":
                return calc_variations(springs[groups[0] + 1:].lstrip("."), groups[1:])
        return calc_variations(springs[next_group_length:], groups[1:])

@timeit
def part_one():
    """Solution for Part 1"""
    data = process_input()
    sum_of_variations = 0
    for idx, line in enumerate(data):
        #variations = calc_variations_old(line[0], line[1])
        print(line)
        variations = calc_variations(line[0], line[1])
        sum_of_variations += variations
    return sum_of_variations


@timeit
def part_two():
    """Solution for Part 2"""
    data = process_input()
    sum_of_variations = 0
    for line in data:
        springs, groups = line
        springs = springs + '?' + springs + '?' + springs + '?' + springs + '?' + springs
        groups = groups * 5
        sum_of_variations += calc_variations(springs, groups)
    return sum_of_variations



if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
