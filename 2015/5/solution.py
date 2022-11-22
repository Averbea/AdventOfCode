""" Advent of code Year 2015 Day 3 solution 
Author = Averbea
Date = November 2022
"""

import re
import os
from time import time

start = time()

with open( os.path.dirname(__file__)+"./input.txt", 'r', encoding="UTF-8") as input_file:
    inputs = input_file.readlines()


pattern_vowels = r"([aeiou].*){3,}"
pattern_double = r"(.)\1"
pattern_not = r"ab|cd|pq|xy"

nice_count, naughty_count = 0 ,0 
for s in inputs: 
    if (re.findall(pattern_vowels, s) and
        re.findall(pattern_double, s)
        and not re.findall(pattern_not, s)):
        nice_count+=1
    else: 
        naughty_count += 1

print("Part One : Nice ",  str(nice_count), "Naughty ", str(naughty_count))

nice_count, naughty_count = 0, 0
pattern_a = r"(..).*\1"
pattern_b = r"(.).\1"
for s in inputs:
    if re.findall(pattern_a,s) and re.findall(pattern_b, s):
        nice_count+=1
    else: 
        naughty_count +=1


print("Part Two : Nice"+  str(nice_count), "Naughty ", str(naughty_count))

print("time elapsed: " + str(time() - start))

