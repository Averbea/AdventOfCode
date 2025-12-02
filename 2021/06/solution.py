# Advent of code Year 2021 Day 6 solution
# Author = Averbea
# Date = December 2021
import collections


def simple_solution(input, days):
    fishlist = [int(x) for x in input.split(",")]
    #print("Initial-State: " + str(fishlist))

    for day in range(days):
        countNewFish = 0
        for i, fish in enumerate(fishlist):
            if fishlist[i] == 0:
                fishlist[i] = 6
                countNewFish += 1
            else:
                fishlist[i] -= 1

        fishlist += countNewFish * [8]
    return len(fishlist)


with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

days = 80
dayOne = simple_solution(input, days)
print("Part One : \nTotal fish after " + str(days)+ " days:"+ str(dayOne))




days = 256

fishlist = input.split(",")

fishcounter = [0] * 9

for fish in fishlist:
    fishcounter[int(fish)] += 1

for day in range(days):
    fishBorn = fishcounter[0]

    fishcounter = collections.deque(fishcounter)
    fishcounter.rotate(-1)
    fishcounter = list(fishcounter)

    fishcounter[6] += fishBorn
    fishcounter[8] = fishBorn


print("Part Two : \nTotal fish after " + str(days)+ " days:"+ str(sum(fishcounter)))