""" Advent of code Year 2022 Day 1 solution
Author = Averbea
Date = December 2022
"""


from time import time
import os
start = time()

with open(os.path.dirname(__file__) +"/input.txt", 'r', encoding="UTF-8") as inputFile:
    inputs = inputFile.read()

inputs = inputs.split("\n\n")


inputGroups =  list(map(lambda el: list(map(lambda innerEl: int(innerEl), el.split("\n"))), inputs))

calories = []
for inputGroup in inputGroups:
    calories.append(sum(inputGroup))


calories.sort(reverse=True)

print("Part One : "+ str(calories[0]))
print("Part Two : "+ str(calories[0] + calories[1] +  calories[2]))

print("time elapsed: " + str(time() - start))
