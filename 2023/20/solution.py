""" Advent of code Year 2023 Day 20 solution
Author = Averbea
Date = December 2023
"""
import math
import re

from utils.templateutils import timeit, read_input_file
from pyvis.network import Network
import matplotlib.pyplot as plt
import networkx as nx


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False).splitlines()
    modules = {}
    for line in file:
        module_type = line[0] if line[0] in '%&' else None

        w = re.findall(r"\w+", line)
        name = w[0]
        targets = w[1:]
        modules[name] = {"type": module_type, "targets": targets}
        if module_type == "%":
            modules[name]["on"] = False
        if module_type == "&":
            modules[name]["last_pulse"] = {}

    for name, module in modules.items():
        for target in module["targets"]:
            if target not in modules.keys():
                continue
            target_module = modules[target]
            if target_module["type"] == "&":
                target_module["last_pulse"][name] = 0

    return modules


def process_signal(modules, signal):
    new_signals = []
    src, val, mod = signal

    if mod not in modules.keys():
        return new_signals
    module = modules[mod]
    targets = module["targets"]
    match module["type"]:
        case "%":
            if val == 0:
                module["on"] = not module["on"]
                if module["on"]:
                    for target in targets:
                        new_signals.append((mod, 1, target))
                else:
                    for target in targets:
                        new_signals.append((mod, 0, target))
        case "&":
            module["last_pulse"][src] = val
            if all(module["last_pulse"].values()):
                for target in targets:
                    new_signals.append((mod, 0, target))
            else:
                for target in targets:
                    new_signals.append((mod, 1, target))
        case None:
            if mod == "broadcaster":
                for target in targets:
                    new_signals.append((mod, val, target))
    return new_signals


@timeit
def part_one():
    """Solution for Part 1"""
    modules = process_input()
    amount_low = amount_high = 0

    for i in range(1000):
        signals = [('btn', 0, 'broadcaster')]
        while signals:
            signal = signals.pop()
            if signal[1] == 0:
                amount_low += 1
            else:
                amount_high += 1
            new_signals = process_signal(modules, signal)
            signals.extend(new_signals)
    return amount_low * amount_high


@timeit
def part_two():
    """Solution for Part 2"""
    modules = process_input()
    return 0


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
