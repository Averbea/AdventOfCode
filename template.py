import os
from time import time

start = time()

with open(os.path.dirname(__file__) +"/input.txt", 'r', encoding="UTF-8") as inputFile:
    inputs = inputFile.read()



print("Part One : "+ str(None))

print("Part Two : "+ str(None))

print("time elapsed: " + str(time() - start))
