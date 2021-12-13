# Advent of code Year 2021 Day 12 solution
# Author = Averbea
# Date = December 2021


def expl(node, visited):
    if node == "end":
        return 1, visited
    if node in visited and node.islower():
        return 0, visited

    sum = 0
    visited.append(node)
    for n in map[node]:
        i, visited = expl(n, visited)
        sum += i
    visited.remove(node)
    return sum, visited

all_paths = []
def newexpl(node, visited, alreadyTwice = False, curPath = "" ):
    if node == "end":
        all_paths.append(curPath + "end")
        return 1, visited
    if node in visited:
        return 0, visited

    curPath += node + ", "
    sum = 0
    if node.islower():
        visited.append(node)
    for n in map[node]:
        i, visited = newexpl(n, visited, alreadyTwice, curPath)
        sum += i
    if node in visited:
        visited.remove(node)
    if alreadyTwice == False and node != "start":
        for n in map[node]:
            i, visited = newexpl(n, visited, True, curPath)
            sum += i

    return sum, visited



with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = input.split("\n")

map = {}
for line in input:
    f, t = line.split("-")
    if not map.keys().__contains__(f):
        map[f] = []
    if not map.keys().__contains__(t):
        map[t] = []


    map[f].append(t)
    map[t].append(f)

for node in map:
    map[node] = list(dict.fromkeys(map[node])) # remove duplicates



paths = expl("start", [])



print("Part One : \n number of paths: "+ str(paths))

paths = newexpl("start", [])
all_paths = list(dict.fromkeys((all_paths))) ##cheating i guess but i dont know better....
print("Part Two : \n number of paths: "+ str(len(all_paths)))