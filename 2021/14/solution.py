# Advent of code Year 2021 Day 14 solution
# Author = Averbea
# Date = December 2021
import copy
from collections import Counter
from time import time
start = time()

def stupid_solution( polymer, insertion_rules):
    for step in range(10):
        i = 1
        while (i < len(polymer)):
            a = polymer[:i]
            b = polymer[i:]
            combination = a[-1] + b[0]
            polymer = a + insertion_rules[combination] + b
            i += 2
    count = {}
    for char in polymer:
        if char not in count.keys():
            count[char] = 0
        count[char] += 1
    return max(count.values()) - min(count.values())


def step(counter, insertion_rules):
    for molecule,value in list(counter.items()):
        new = insertion_rules[molecule]
        counter[molecule] -= value
        counter[molecule[0] + new] += value
        counter[new + molecule[1]] += value
    return counter

def get_result(counter, firstChar):
    elementCounter = Counter() ##this counts how many times the element is in the polymer
    for mol, amount in counter.items():
        elementCounter[mol[1]] += amount
    elementCounter[firstChar] += 1 ## compensate the first element

    return max(elementCounter.values())- min(elementCounter.values())


with open((__file__.rstrip("solution.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()
polymer, _ , *input = input.split("\n")

counter = Counter()
for i in range(len(polymer) -1):
    counter[polymer[i:i+2]] += 1
insertion_rules = {}
for line in input:
    line = line.split(" -> ")
    insertion_rules[line[0]] = line[1]

counter2 = copy.deepcopy(counter) ##copy counter for part 2



for i in range(10):
    counter = step(counter, insertion_rules)
result = get_result(counter, polymer[0])

print("Part One :\nquantity of the most common element minus quantity of the least common element is " + str(result))



for i in range(40):
    counter2 = step(counter2, insertion_rules)
result = get_result(counter2, polymer[0])
print("Part Two :\nquantity of the most common element minus quantity of the least common element is " + str(result))

print("elapsed time: " + str(time() - start) + "s")