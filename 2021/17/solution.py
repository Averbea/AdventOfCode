from time import time
# Advent of code Year 2021 Day 17 solution
# Author = Averbea
# Date = December 2021

start = time()

class Probe:
    def __init__(self, velocity_x, velocity_y,  target):
        self.velocity = [velocity_x, velocity_y]
        self.position = [0, 0]
        self.target = target

    def step(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        if self.velocity[0] > 0:
            self.velocity[0] -= 1
        elif self.velocity[0] < 0:
            self.velocity[0] += 1

        self.velocity[1] -= 1

    def isInTarget(self):
        if target["minX"] <= self.position[0] <= target["maxX"] and  target["minY"] <=  self.position[1] <= target["maxY"]:
            return True
        return False

    def simulate(self):
        maxY = 0
        for step in range(200):
            self.step()
            maxY = max(maxY, self.position[1])
            if self.isInTarget():
                return True, maxY

        return False, maxY


with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = input[len("target area: x="):]
input = input.split(", y=")


xRange = input[0].split("..")
yRange = input[1].split("..")

target = {
    "minX": int(xRange[0]),
    "maxX": int(xRange[1]),
    "minY": int(yRange[0]),
    "maxY": int(yRange[1])
}

print("Part One : "+ str(target["minY"] * (target["minY"] +1) / 2)) ##why is this correct???

vels = []

for x in range(1, target["maxX"] + 1):
    for y in range(-100,400):
        probe = Probe(x,y, target)
        success, val = probe.simulate()
        if success:
            vels.append((x,y))

print("Part Two : "+ str(len(vels)))

print("time elapsed: " + str(time() - start))
