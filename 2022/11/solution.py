""" Advent of code Year 2022 Day 11 solution
Author = Averbea
Date = December 2022
"""


import os
import re
from time import time
from typing import Callable



def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read().split("\n\n")
    monkeys: list[Monkey] = []
    for i in inputs:
        start_items = re.findall(r"Starting items: (.*)\n", i)[0]
        start_items = start_items.split(", ")
        start_items = list(map(int, start_items))

        operation = eval("lambda old:" + re.findall(r"Operation: new =(.*)\n", i)[0])

        test = int(re.findall(r"Test: divisible by (\d*)", i)[0])
        test_true_target = int(re.findall(
            r"If true: throw to monkey (\d*)", i)[0])
        test_false_target = int(re.findall(
            r"If false: throw to monkey (\d*)", i)[0])

        monkeys.append(Monkey(start_items, operation, test,
                       test_true_target, test_false_target))

    return monkeys


class Monkey:
    """class representing a monkey"""

    def __init__(self, starting_items: list[int], operation: Callable[[int], int], test: int, test_true_target: int, test_false_target: int):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.test_true_target = test_true_target
        self.test_false_target = test_false_target
        self.inspect_count = 0

    def take_turn(self, decrease_worry_level: bool = False, least_common_multiple=1):
        """take a turn

        Args:
            decrease_worry_level (bool, optional): decrease the worry level for each item. Defaults to False.
            least_common_multiple (int, optional): least common multiple of all divisors. Defaults to 1.

        Returns:
            list: [item, target]
        """
        to_throw = []
        for item in self.items:
            self.inspect_count += 1
            new = self.operation(item)
            new = new % least_common_multiple
            if decrease_worry_level:
                new = new // 3
            if new % self.test == 0:
                to_throw.append([new, self.test_true_target])
            else:
                to_throw.append([new, self.test_false_target])
        self.items = []
        return to_throw


def solve(monkeys: list[Monkey], rounds: int, reduce_worry: bool):
    """solve the task for given monkeys, number of rounds"""
    lcm = 1

    for monkey in monkeys:
        lcm *= monkey.test

    for _ in range(rounds):
        for monkey in monkeys:
            items_to_throw = monkey.take_turn(reduce_worry, lcm)
            for item, target in items_to_throw:
                monkeys[target].items.append(item)

    visited = list(map(lambda m: m.inspect_count, monkeys))
    visited.sort()
    return visited[-1] * visited[-2]


def part_one():
    """Solution for Part 1"""
    rounds = 20
    monkeys = parse_input()
    return solve(monkeys, rounds, True)


def part_two():
    """Solution for Part 2"""
    rounds = 10000
    monkeys = parse_input()
    return solve(monkeys, rounds, False)


def main():
    """main method"""
    time_needed, result = measure_timing(part_one)

    print("Part One : " + str(result))
    print("time elapsed: " + str(time_needed))

    time_needed, result = measure_timing(part_two)
    print("\nPart Two : " + str(result))
    print("time elapsed: " + str(time_needed))


def print_monkey_lists(monkeys: list[Monkey]):
    """prints the monkeys lists"""
    for i, monkey in enumerate(monkeys):
        print("monkey ", i, " : ", monkey.items)
    print("\n")
    for i, monkey in enumerate(monkeys):
        print("monkey ", i, " inspected ", monkey.inspect_count, " items")


if __name__ == "__main__":
    main()


# durch 23
# (x * 23 + r)
