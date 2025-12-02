# Advent of code Year 2021 Day 1 solution
# Author = Averbea
# Date = December 2021

with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()


timesIncreased = 0

count = 0
prev = int(input[0])

for i in range(len(input)):
    if i == 0:
        continue
    cur = int(input[i])

    if cur > prev:
        timesIncreased += 1
    prev = cur

print("Part One : "+ str(timesIncreased))


timesIncreased = 0

prev = int(input[0]) + int(input[1]) + int(input[2])

for i in range(len(input)):
    if i == 0:
        continue
    cur = int(input[i])+int(input[i-1])+int(input[i-2])

    if cur > prev:
        timesIncreased += 1
    prev = cur

print("Part Two : "+ str(timesIncreased))