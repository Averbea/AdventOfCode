# Advent of code Year 2021 Day 3 solution
# Author = Averbea
# Date = December 2021

def fun(lines, lambdaforVal):
    curLines = lines
    newLines = []
    for i in range(numberOfBits):
        countOne = 0
        countZero = 0

        for line in curLines:
            if line[i] == '1':
                countOne += 1
            else:
                countZero += 1

        for line in curLines:
            val =lambdaforVal(countOne, countZero)
            if line[i] == val:
                newLines.append(line)

        curLines = newLines
        if len(curLines) == 1:
            break
        newLines = []
    return int(curLines[0],2)



with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
lines = input.split("\n")

numberOfBits = len(lines[0])
numberOfInputs = len(lines)

countOne = [0] * numberOfBits
countZero = [0] * numberOfBits
for line in lines:
    for i in range(len(line)):
       if line[i] == '1':
            countOne[i] += 1
       else:
           countZero[i] += 1


gammaBin = '0b'
epsilonBin = '0b'
for b in countOne:
    if b > numberOfInputs / 2:
        gammaBin += '1'
        epsilonBin += '0'
    else:
        gammaBin += '0'
        epsilonBin += '1'

gamma = int(gammaBin, 2)
epsilon = int(epsilonBin, 2)
print("Gamma: " + str(gamma))
print("Epsilon: " + str(epsilon))

powerConsumption = gamma * epsilon
print("Part One : power Consumption = "+ str(powerConsumption))

#Oxygen generator.... keep lines with most common bit

oxygen= fun(lines,lambda a, b: '1' if a >= b else '0')
co2 = fun(lines, lambda  a, b: '0' if a >= b else '1')
print("oxygen Generator:" +str(oxygen))
print("co2Scrubber Generator:" +str(co2))

lifeSupportRating = oxygen * co2
print("Part Two : lifeSupportRating = "+ str(lifeSupportRating))

