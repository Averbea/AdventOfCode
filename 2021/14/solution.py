# Advent of code Year 2021 Day 14 solution
# Author = Averbea
# Date = December 2021

def stupid_solution(data):
    data = data.split("\n")

    polymer = data[0]

    data = data[2:]

    insertion_rules = {}
    for line in data:
        line = line.split(" -> ")
        insertion_rules[line[0]] = line[1]

    for step in range(10):
        print(step)
        i = 1
        while (i < len(polymer)):
            a = polymer[:i]
            b = polymer[i:]
            combination = a[-1] + b[0]
            polymer = a + insertion_rules[combination] + b
            i += 2

    count = {}
    for char in polymer:
        if char not in count.keys():
            count[char] = 0
        count[char] += 1

    return max(count.values()) - min(count.values())

with open((__file__.rstrip("solution.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()


print("Part One :\nquantity of the most common element minus quantity of the least common element is " + str(stupid_solution(input)))

print("Part Two : " + str(None))
