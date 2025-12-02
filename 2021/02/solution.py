# Advent of code Year 2021 Day 2 solution
# Author = Averbea
# Date = December 2021

with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
lines = input.split("\n")

pos = {
    "horizontal": 0,
    "depth": 0
} #this is horizontal and DEPTH!!

for line in lines:
    [cmd, val] = line.split(" ")
    val = int(val)
    match cmd:
        case "forward":
            pos["horizontal"] += val
        case "up":
            pos["depth"] -= val
        case "down":
            pos["depth"] += val

print("Pos: " +str(pos))

print("Part One : "+ str(pos["horizontal"] * pos["depth"]))




pos = {
    "horizontal": 0,
    "depth": 0,
    "aim": 0
} #this is horizontal and DEPTH!!

for line in lines:
    [cmd, val] = line.split(" ")
    val = int(val)
    match cmd:
        case "forward":
            pos["horizontal"] += val
            pos["depth"] += pos["aim"] * val
        case "up":
            pos["aim"] -= val
        case "down":
            pos["aim"] += val

print("Pos: " +str(pos))

print("Part One : "+ str(pos["horizontal"] * pos["depth"]))


print("Part Two : "+ str(None))