# Advent of code Year 2021 Day 13 solution
# Author = Averbea
# Date = December 2021


def foldX(index, oldGrid):
    newGrid = [[False] * index for i in range(len(oldGrid))]


    for y , line in enumerate(newGrid):
        for x, dot in enumerate(line):
            newGrid[y][x] = oldGrid[y][x]
            if 2*(index -x) < len(oldGrid[0]):
                newGrid[y][x] |= oldGrid[y][x + 2*(index -x)]
    return newGrid


def foldY(index, oldGrid):
    newGrid = [[False] * len(oldGrid[0]) for i in range(index)]
    for y, line in enumerate(newGrid):
        for x, dot in enumerate(line):
            newGrid[y][x] = oldGrid[y][x]
            if y + 2 * (index - y) < len(oldGrid):
                newGrid[y][x] |= oldGrid[y + 2 * (index - y)][x]
    return newGrid



def printgrid(grid):
    print("grid:")
    for line in grid:
        str = ""
        for dot in line:
            if dot:
                str += "#"
            else:
                str += "."
        print(str)


def countDots(grid):
    count = 0
    for line in grid:
        for dot in line:
            if dot:
                count += 1
    return count


with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = input.split("\n")
for i, line in enumerate(input):
    if line == "":
        index = i

dots = input[:index]
instructions = input[index +1 :]
dots = [list(map(int,d.split(","))) for d in dots]
maxX, maxY = 0, 0
for dot in dots:
    if dot[0] > maxX:
        maxX = dot[0]
    if dot[1] > maxY:
        maxY = dot[1]

grid = [[False]*(maxX+1) for i in range(maxY + 1)]

for dot in dots:
    grid[dot[1]][dot[0]] = True

instructions = [i[11:].split("=") for i in instructions]

gridA = grid
for i in instructions[:1]:
    if i[0] == "x":
        gridA = foldX(int(i[1]), gridA)
    if i[0] == "y":
        gridA = foldY(int(i[1]), gridA)
print("Part One : \ncont after first fold "+ str(countDots(gridA)))


for i in instructions:
    if i[0] == "x":
        grid = foldX(int(i[1]), grid)
    if i[0] == "y":
        grid = foldY(int(i[1]), grid)

print("Part Two : "+ str(None))
printgrid(grid)