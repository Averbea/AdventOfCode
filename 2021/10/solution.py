# Advent of code Year 2021 Day 10 solution
# Author = Averbea
# Date = December 2021
from functools import reduce

with open((__file__.rstrip("solution.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()
    input = input.split("\n")

lookup = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}
syntax_checker_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
opening = lookup.keys()
closing = lookup.values()

syntax_score = 0
autocomplete_score_list = []
for line in input:
    stack = []
    incompleteLine = True
    for sign in line:
        if sign in opening:
            stack.append(sign)
        elif sign in closing:
            last = stack.pop()
            if lookup[last] != sign:
                print("expected %s but was %s" % (lookup[last], sign))
                syntax_score += syntax_checker_scores[sign]
                incompleteLine = False
                break
    if incompleteLine:
        stack.reverse()
        stack = [lookup[c] for c in stack]
        closing_sequence = reduce(lambda a, b: a + b, stack)
        print(closing_sequence)
        print("incomplete line : closing sequence is " + closing_sequence)
        curScore = 0
        for c in stack:
            curScore *= 5
            curScore += autocomplete_scores[c]
        autocomplete_score_list.append(curScore)

print("Part One : \nfinal syntax checker score is: " + str(syntax_score))

autocomplete_score_list.sort()
i = len(autocomplete_score_list)

# this is correct because indices start at 0 and there will always be an odd number of scores
middle_score = autocomplete_score_list[int(i / 2)]
print("Part Two : \nfinal autocomplete score is: " + str(middle_score))
