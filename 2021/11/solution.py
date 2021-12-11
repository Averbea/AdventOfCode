# Advent of code Year 2021 Day 11 solution
# Author = Averbea
# Date = December 2021


def increase_energy(grid, xPos, yPos, to_flash):
    if xPos < 0 or xPos >= size_x or yPos < 0 or yPos >= size_y:
        return grid, to_flash


    grid[yPos][xPos]["energy"] += 1
    if grid[yPos][xPos]["energy"] > 9:
        to_flash.append((xPos,yPos))

    return grid, to_flash


def flash(grid, xPos, yPos, to_flash):
    global flash_count
    if xPos < 0 or xPos >= size_x or yPos < 0 or yPos >= size_y:
        return grid, to_flash,0
    if grid[yPos][xPos]["flashed"]:
        return grid, to_flash,0
    grid[yPos][xPos]["flashed"] = True
    flash_count += 1
    for x, y in [(xPos -1, yPos -1), (xPos, yPos - 1), (xPos + 1, yPos -1), (xPos -1, yPos), (xPos +1, yPos), (xPos -1, yPos +1), (xPos, yPos + 1), (xPos + 1, yPos +1)]:
        grid, to_flash = increase_energy(grid, x, y, to_flash)

    return grid, to_flash, 1

def step(grid):
    to_flash = []
    flashes = 0
    for y , line in enumerate(grid):
        for x, pos in enumerate(line):
            grid, to_flash = increase_energy(grid, x,y,to_flash)

    while len(to_flash) != 0:
        x, y = to_flash.pop()
        grid, to_flash, new_flashes = flash(grid, x, y, to_flash)
        flashes += new_flashes

    for y, line in enumerate(grid):
        for x, pos in enumerate(line):
            if grid[y][x]["energy"] > 9:
                grid[y][x]["energy"] = 0
            grid[y][x]["flashed"] = False
    return grid, flashes



with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

size_x = 10
size_y = 10


flash_count = 0
simultaneous_flash_steps = []
input = input.split("\n")
number_of_steps = 100

grid = []
for line in input:
    grid.append([
        {
            "energy": int(c),
            "flashed": False
        }for c in line])

for s in range(number_of_steps):
    grid, flashes = step(grid)



print("Part One : \nTotal Flash Count: "+ str(flash_count))

simultaneous_flash_step = -1
grid = []
for line in input:
    grid.append([
        {
            "energy": int(c),
            "flashed": False
        }for c in line])
s = 0
while 1:
    s += 1
    grid , flashes= step(grid)
    if flashes == size_x * size_y:
        simultaneous_flash_step = s
        break


print("Part Two \n Steps where all ocopuses flash: "+ str(simultaneous_flash_step))