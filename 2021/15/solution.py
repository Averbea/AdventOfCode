import copy
from time import time
# Advent of code Year 2021 Day 15 solution
# Author = Averbea
# Date = December 2021

start = time()


class AStar:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.openList = []
        self.closedList = []

        ##open list contains tuples of (x, y, cost)
        self.openList.append((start[0], start[1], 0))

    def h(self, x, y):
        return self.end[1] - y + self.end[0] - x

    def sortByCost(self):

        self.openList.sort(key=lambda x: x[2] + self.h(x[0], x[1]))


    def expand(self, toExpand):
        x = toExpand[0]
        y = toExpand[1]
        cost = toExpand[2]
        if x > 0:
            self.addToOpen(x - 1, y, cost)
        if y > 0:
            self.addToOpen(x, y - 1, cost)
        if x < len(self.grid[0]) - 1:
            self.addToOpen(x + 1, y, cost)
        if y < len(self.grid) - 1:
            self.addToOpen(x, y + 1, cost)

    def openlistcontains(self, x, y):
        for tuple in self.openList:
            if tuple[0] == x and tuple[1] == y:
                return tuple[2]


    def addToOpen(self, x, y, beforeCost):
        if self.closedList.__contains__((x,y)):
            return

        newcost = beforeCost + self.grid[y][x]
        oldTupleCost = self.openlistcontains(x,y)
        if oldTupleCost == None:
            self.openList.append((x, y, newcost))
            return
        if oldTupleCost > newcost:
            self.openList.remove((x,y,oldTupleCost))
            self.openList.append((x, y, newcost))




    def step(self):
        self.sortByCost()
        cur = self.openList.pop(0)
        if( (cur[0], cur[1]) == self.end):
            return "SUCCESS", cur[2]
        self.closedList.append((cur[0], cur[1]))
        self.expand(cur)

        return "NO Success", -1

    def find(self):
        while len(self.openList) != 0:
            ret, risk = self.step()
            if ret == "SUCCESS":
                return risk



with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

grid = [[int(char) for char in line] for line in input.split("\n") ]


alg = AStar(grid, (0,0), (len(grid)-1, len(grid[0])-1))
risk = alg.find()

print("Part One: \ntotal risk is "+ str(risk))

print("time elapsed: " + str(time() - start))
sizex = len(grid[0])
sizey = len(grid)
grid2 = [[0 for j in range(sizex * 5)] for i in range(sizey * 5)]

for y, line in enumerate(grid2):
    for x, cell in enumerate(line):
        grid2[y][x] = grid[y % sizey][x % sizex]
        grid2[y][x] += int(y / sizey) + int(x / sizex)
        while grid2[y][x] > 9:
            grid2[y][x] -= 9





alg2 = AStar(grid2, (0,0), (len(grid2)-1, len(grid2[0])-1))
risk2 = alg2.find()


print("Part Two: \ntotal risk is "+ str(risk2))

print("time elapsed: " + str(time() - start))