""" Advent of code Year 2021 Day 22 solution 
Author = Averbea
Date = December 2022
"""


import os
import re
from time import time

start = time()

with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
    # inputs = input_file.read()
    REGEX_PATTERN = r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'
    steps = re.findall(REGEX_PATTERN, input_file.read())

#steps is now a list of tuples
# ("on", xmin, xmax, ymin, ymax, zmin, zmax)

on = set()

for index, step in enumerate(steps):
    print(index)
    action, x_min, x_max, y_min, y_max, z_min, z_max = step
    if (int(x_min) < -50 or int(y_min) < -50 or int(z_min) < -50 or
        int(x_max) > 50 or int(y_max) > 50 or int(z_max) > 50):
        continue

    for x in range(int(x_min), int(x_max) +1):
        for y in range(int(y_min), int(y_max)+1):
            for z in range(int(z_min), int(z_max) +1):
                if action=="on":
                    on.add((x,y,z))
                else:
                    on.discard((x,y,z))

print(len(on))
print("Part One : "+ str(None))



print("Part Two : "+ str(None))

print("time elapsed: " + str(time() - start))
