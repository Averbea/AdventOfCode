import functools
from time import time
# Advent of code Year 2021 Day 16 solution
# Author = Averbea
# Date = December 2021
start = time()

class Message:
    def __init__(self, version, packetID):
        self.version = version
        self.packetID = packetID
        self.binaryMsg = ""

    def parse(self, input):
        return input

    def getVersionSum(self):
        return self.version

    def getValue(self):
        raise Exception("this method cant be called on parent class")

class LiteralMessage(Message):
    def __init__(self, version, packetID):
        if packetID != 4:
            raise Exception("expected packet ID 4, but got " + str(packetID))
        super().__init__(version, packetID)
        self.subPackets = []


    def parse(self, input):
        while True:
            cur  = input[:5]
            input = input[5:]

            leadingBit = cur[0]
            cur = cur[1:]

            self.binaryMsg += cur

            if leadingBit == '0':
                break

        self.message = int(self.binaryMsg, 2)

        return input

    def getValue(self):
        return self.message

class OperatorMessage(Message):
    def __init__(self, version, packetID):
        if packetID == 4:
            raise Exception("expected packet ID != 4, but got " + str(packetID))
        super().__init__(version, packetID)
        self.subPackets = []

    def parse(self, input):

        self.lengthTypeID = input[0]
        input = input[1:]

        if self.lengthTypeID == '0': #next 15 bits represent TOTAL LENGTH IN BITS of Subpackets
            subPacketTotalLength = int(input[:15], 2)
            input = input[15:]
            subPacketsBin = input[:subPacketTotalLength]
            input = input[subPacketTotalLength:]

            while len(subPacketsBin) > 0:
                subPacketsBin,msg = parseMsg(subPacketsBin)
                self.subPackets.append(msg)


        elif self.lengthTypeID == '1':  # next 11 bits represent NUMBER OF SUB-PACKETS
            subPacketCount = int(input[:11],2)
            input = input[11:]
            for i in range(subPacketCount):
                input, msg = parseMsg(input)
                self.subPackets.append(msg)
        else:
            raise Exception("invalid lengthTypeID: was " + self.lengthTypeID)
        return input

    def getVersionSum(self):
        versSum = self.version
        for c in self.subPackets:
            versSum += c.getVersionSum()
        return versSum

    def getValue(self):
        match self.packetID:
            case 0:     #sum of subpackets
                return functools.reduce(lambda a, b: a+b, [m.getValue() for m in self.subPackets])
            case 1:     #product of subpackets
                return functools.reduce(lambda a, b: a * b, [m.getValue() for m in self.subPackets])
            case 2:     #min of subpackets
                return functools.reduce(lambda a, b: min(a, b), [m.getValue() for m in self.subPackets])
            case 3:     #max of subpackets
                return functools.reduce(lambda a, b: max(a, b), [m.getValue() for m in self.subPackets])
            case 5:     #greater than... contains exactly 2 subpackets
                return 1 if self.subPackets[0].getValue() > self.subPackets[1].getValue() else 0
            case 6:     #less than... contains exactly 2 subpackets
                return 1 if self.subPackets[0].getValue() < self.subPackets[1].getValue() else 0
            case 7:  # equal... contains exactly 2 subpackets
                return 1 if self.subPackets[0].getValue() == self.subPackets[1].getValue() else 0

def parseMsg(binary):
    version = int(binary[:3], 2)
    binary = binary[3:]

    packetId = int(binary[:3], 2)
    binary = binary[3:]

    if packetId == 4:
        msg = LiteralMessage(version, packetId)
    else:
        msg = OperatorMessage(version, packetId)

    binary = msg.parse(binary)

    return binary, msg


with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

binary = ""
for char in input:
    curBin = bin(int(char, 16))[2:]
    curBin = '0'* (4-len(curBin)) + curBin
    binary += curBin


binary, msg = parseMsg(binary)

print("Part One : "+ str(msg.getVersionSum()))

print("Part Two : "+ str( msg.getValue()))

print("time elapsed: " + str(time() - start))