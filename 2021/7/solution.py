# Advent of code Year 2021 Day 7 solution
# Author = Averbea
# Date = December 2021
def calcFuel(list, pos):
    fuel = 0
    for elem in list:
        fuel += abs(elem - pos)
    return fuel

#inefficient but works
def newCalcFuel(list, pos):
    print(pos)
    fuel = 0
    for elem in list:
        diff = abs(elem - pos)
        for i in range(diff+1):
            fuel += i
    return fuel

with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
crabPositions  = [int(x) for x in input.split(",")]

minFuel = min(calcFuel(crabPositions, i) for i in range(min(crabPositions), max(crabPositions)))


print(min(crabPositions))
print(max(crabPositions))
print("Part One : \nMin Fuel: "+ str(minFuel))

minFuel = min(newCalcFuel(crabPositions, i) for i in range(min(crabPositions), max(crabPositions)))
print("Part Two : \nMin Fuel: "+ str(minFuel))