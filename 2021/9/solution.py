# Advent of code Year 2021 Day 9 solution
# Author = Averbea
# Date = December 2021
from functools import reduce

with open((__file__.rstrip("solution.py") + "input.txt"), 'r') as input_file:
    input = input_file.read().split("\n")

grid = []
for line in input:
    grid.append([int(digit) for digit in line])

maxX = len(grid) - 1
maxY = len(grid[0]) - 1

riskLevelSums = 0
# search for low points
for x, line in enumerate(grid):
    for y, val in enumerate(line):
        if x > 0 and grid[x - 1][y] <= val:
            continue
        if x < maxX and grid[x + 1][y] <= val:
            continue
        if y > 0 and grid[x][y - 1] <= val:
            continue
        if y < maxY and grid[x][y + 1] <= val:
            continue
        riskLevel = val + 1
        print(str(riskLevel) + " at " + str((x, y)))
        riskLevelSums += riskLevel

print("Part One : \n Sum of RiskLevels: " + str(riskLevelSums))


def explore(cur_grid, x_pos, y_pos):
    if x_pos < 0 or y_pos < 0 or x_pos >= len(cur_grid) or y_pos >= len(cur_grid[0]):
        return cur_grid, 0
    if cur_grid[x_pos][y_pos] == 9:
        return cur_grid, 0

    cur_grid[x_pos][y_pos] = 9  # not count this as basin anymore
    count = 1
    cur_grid, to_add = explore(cur_grid, x_pos - 1, y_pos)
    count += to_add
    cur_grid, to_add = explore(cur_grid, x_pos + 1, y_pos)
    count += to_add
    cur_grid, to_add = explore(cur_grid, x_pos, y_pos - 1)
    count += to_add
    cur_grid, to_add = explore(cur_grid, x_pos, y_pos + 1)
    count += to_add

    return cur_grid, count


basin_sizes = []
for x, val_x in enumerate(grid):
    for y, val_y in enumerate(val_x):
        grid, cur_basin = explore(grid, x, y)
        if cur_basin != 0:
            basin_sizes.append(cur_basin)

basin_sizes.sort(reverse=True)

print(basin_sizes)
sum_of_largest_basins = reduce((lambda a, b: a * b), basin_sizes[:3])
print("Part Two : \nSum of three largest " + str(sum_of_largest_basins))
