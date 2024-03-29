import copy
import matplotlib.pyplot as plt
from time import time
# Advent of code Year 2021 Day 20 solution
# Author = Averbea
# Date = December 2021
import numpy as np

start = time()


def draw(pixels):
    minX = min([p[0] for p in pixels]) - 10
    maxX = max([p[0] for p in pixels]) + 11
    minY = min([p[1] for p in pixels]) - 10
    maxY = max([p[1] for p in pixels]) + 11
    data = np.zeros([maxX - minX, maxY - minY, 3], dtype=np.uint8)

    for p in pixels:
        x = p[0] + abs(minX)
        y = p[1] + abs(minY)
        data[y][x] = [255, 255, 255]

    plt.imshow(data, interpolation='nearest')
    plt.xticks(np.arange(0, maxX - minX, 1), np.arange(minX, maxX, 1))
    plt.yticks(np.arange(0, maxY - minY, 1), np.arange(minY, maxY, 1))
    plt.show()


def step(pixel_data, infinite_bit):

    minY = min(p[1] for p in pixels)
    maxY = max(p[1] for p in pixels)
    minX = min(p[0] for p in pixels)
    maxX = max(p[0] for p in pixels)

    enhanced = set()

    for y in range(minY - 1, maxY + 2):
        for x in range(minX - 1, maxX + 2):
            index = 0
            binString = ""
            for curY in range(y - 1, y + 2):
                for curX in range(x - 1, x + 2):
                    if (minY <= curY <= maxY and minX <= curX <= maxX):  ## why is this exactly needed?
                        binString += str(int((curX, curY) in pixels))
                    else:
                        binString += str(infinite_bit)

            if alg[int(binString,2)] == 1:
                enhanced.add((x, y))

    return enhanced


with open((__file__.rstrip("solution.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()

alg, _, *image = input.split("\n")
alg = [int(ch == '#') for ch in alg]

pixels = set(
    (x, y)
    for y, row in enumerate(image)
    for x, ch in enumerate(row)
    if ch == '#'
)

draw(pixels)


for i in range(50):
    infbit =  i & 1 & alg[0]
    pixels = step(pixels, infbit )

draw(pixels)
print(len(pixels))
print("Part Two : " + str(None))

print("time elapsed: " + str(time() - start))
