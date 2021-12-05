# Advent of code Year 2021 Day 5 solution
# Author = Averbea
# Date = December 2021
def print_ocean(oceanlist):
    for l in oceanlist:
        print(l)


def set_lines(ocean, geysirlines, consider_diagonal=False):
    for line in geysirlines:
        (fromx, fromy) = line["from"]
        (tox, toy) = line["to"]

        if fromx == tox:
            a = fromy if fromy < toy else toy
            b = toy + 1 if fromy < toy else fromy + 1
            for i in range(a, b):
                ocean[i][fromx] += 1
        elif fromy == toy:
            a = fromx if fromx < tox else tox
            b = tox + 1 if fromx < tox else fromx + 1
            for i in range(a, b):
                ocean[fromy][i] += 1
        else:
            if consider_diagonal:
                stepx, stepy = 1, 1
                if fromx > tox:
                    stepx = -1
                if fromy > toy:
                    stepy = -1

                while (1):
                    ocean[fromy][fromx] += 1
                    if fromx == tox:
                        break
                    fromx += stepx
                    fromy += stepy

    return ocean


def countPoints(ocean):
    count = 0
    for i in range(len(ocean)):
        for j in range(len(ocean)):
            if ocean[i][j] >= 2:
                count += 1
    return count


with open((__file__.rstrip("solution.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()
oceansize = 1000
inputlines = input.split("\n")

geysirlines = []
for l in inputlines:
    fromandto = l.split(" -> ")
    line = {
        "from": [int(x) for x in fromandto[0].split(",")],
        "to": [int(x) for x in fromandto[1].split(",")]
    }
    geysirlines.append(line)

ocean = [[0] * oceansize for i in range(oceansize)]

ocean = set_lines(ocean, geysirlines)

count = countPoints(ocean)
# printOcean(ocean)

print("Part One : \nnumber of points where at least two lines overlap: " + str(count))

ocean = [[0] * oceansize for i in range(oceansize)]

ocean = set_lines(ocean, geysirlines, True)

# printOcean(ocean)
count = countPoints(ocean)

print("Part Two : \nnumber of points where at least two lines overlap: " + str(count))
