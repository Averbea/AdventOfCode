""" Advent of code Year 2022 Day 3 solution
Author = Averbea
Date = December 2022
"""


import os
import re
from time import time

start = time()

with open(os.path.dirname(__file__) +"/input.txt", 'r', encoding="UTF-8") as inputFile:
    inputs = inputFile.read()

RUCKSACKS = inputs.split("\n")

def get_priority(char: str):
    """calculates the priority value for a given char

    Args:
        char (str): char to calculate value for
    """
    # ord("a") - 96 = 1
    # ord("A") - 38 = 27
    if re.match("[A-Z]", char): 
        return ord(char) - 38
    else: 
        return ord(char) - 96


def part_one():
    sum = 0
    for rucksack in RUCKSACKS:
        size = len(rucksack)
        
        first_compartment = rucksack[0:int(size/2)]
        second_compartment = rucksack[int(size/2): size]
        for char in first_compartment: 
            if char in second_compartment:
                sum += get_priority(char)
                break
    return sum

def part_two():
    sum = 0
    elve_groups = []
    for i in range(1,int(len(RUCKSACKS )/ 3) +1):
        elve_groups.append(RUCKSACKS[(i-1)*3:i*3])
    for group in elve_groups:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                sum += get_priority(char)
                break
    return sum


print("Part One : "+ str(part_one()))

print("Part Two : "+ str(part_two()))

print("time elapsed: " + str(time() - start))
