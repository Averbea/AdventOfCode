# Advent of code Year 2021 Day 8 solution
# Author = Averbea
# Date = December 2021

with open((__file__.rstrip("solution.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()

lines = input.split("\n")

lines = [s.split(" | ") for s in lines]
signalsAndSegments = []
for line in lines:
    signalsAndSegments.append({
        "signals": line[0].split(" "),
        "segments": line[1].split(" ")
    })

count = 0
for x in signalsAndSegments:
    for s in x["segments"]:
        if len(s) in [2, 4, 3, 7]:
            count += 1

print("Part One : \ncount of unique digits: " + str(count))

outputSum = 0
for i in signalsAndSegments:
    signals = i["signals"]
    segments = i["segments"]
    all = signals + list(set(segments) - set(signals))
    lookup = [
        {
            "chars": "",
            "sure": False
        }
        for i in range(10)
    ]

    for s in all:
        match len(s):
            case 2:
                lookup[1]["chars"] = s
            case 3:
                lookup[7]["chars"] = s
            case 4:
                lookup[4]["chars"] = s
            case 7:
                lookup[8]["chars"] = s
    # all found digits are 1 4 7 8

    # now search for the 9
    charsInSeven = [char for char in lookup[7]["chars"]]
    charsInFour = [char for char in lookup[4]["chars"]]

    combined = charsInSeven + list(set(charsInFour) - set(charsInSeven))

    foundSets = []

    # it has all segments that 7 and 4 have combined + 1
    for s in all:
        match len(s):
            case 6:
                curChars = [char for char in s]
                if set(combined) <= set(curChars):
                    lookup[9]["chars"] = s
                    foundSets.append(set(curChars))
                    break

    # we now know digits 14789
    charsInOne = [char for char in lookup[1]["chars"]]

    for s in all:
        match len(s):
            case 6:
                curChars = [char for char in s]
                if set(charsInOne) <= set(curChars) and set(curChars) not in foundSets:
                    lookup[0]["chars"] = s
                    foundSets.append(set(curChars))
                    break

    # now we know 0 1 4 7 8 9

    # last digit with 6 segments is the 6
    for s in all:
        match len(s):
            case 6:
                curChars = [char for char in s]
                if set(curChars) not in foundSets:
                    lookup[6]["chars"] = s
                    foundSets.append(set(curChars))
                    break

    # if one is subset of digit with len 5 it must be a 3
    for s in all:
        match len(s):
            case 5:
                curChars = [char for char in s]
                if set(charsInOne) <= set(curChars) and set(curChars) not in foundSets:
                    lookup[3]["chars"] = s
                    foundSets.append(set(curChars))
                    break

    # if a digit of len 5 contains lower left segment it must be a 2 else it is a 5
    charsInEight = [char for char in lookup[8]["chars"]]
    charsinNine = [char for char in lookup[9]["chars"]]
    lowerLeftSegment = list(set(charsInEight) - set(charsinNine))
    for s in all:
        match len(s):
            case 5:
                curChars = [char for char in s]
                if set(lowerLeftSegment) <= set(curChars) and set(curChars) not in foundSets:
                    lookup[2]["chars"] = s
                    foundSets.append(set(curChars))
                    break
    for s in all:
        match len(s):
            case 5:
                curChars = [char for char in s]
                if (not set(lowerLeftSegment) <= set(curChars)) and set(curChars) not in foundSets:
                    lookup[5]["chars"] = s
                    foundSets.append(set(curChars))
                    break
    # all digit chars are found
    output = []
    for segment in segments:
        segmentSet = set([char for char in segment])
        for digit in range(10):
            digitSet = set([char for char in lookup[digit]["chars"]])
            if digitSet == segmentSet:
                output.append(digit)
                break
    outputDec = int(output[0]) * 1000 + int(output[1]) * 100 + int(output[2]) * 10 + int(output[3]) * 1
    outputSum += outputDec

print("Part Two : \nSum is: " + str(outputSum))