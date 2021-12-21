from time import time

# Advent of code Year 2021 Day 21 solution
# Author = Averbea
# Date = December 2021

start = time()

numberOfTimesRolled = 0


def rollDice():
    global numberOfTimesRolled
    numberOfTimesRolled += 1
    val = numberOfTimesRolled
    while val > 100:
        val -= 100
    return val


class Player:
    def __init__(self, start, winningScore, name):
        self.name = name
        self.pos = start
        self.score = 0
        self.winningScore = winningScore

    def turn(self, vals):
        for number in vals:
            self.pos += number
            while self.pos > 10:
                self.pos -= 10
        self.score += self.pos

    def checkWin(self):
        if self.score >= self.winningScore:
            return True
        return False


with open((__file__.rstrip("solution.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()

input = input.split("\n")

player1 = Player(int(input[0][-1]), 1000, "p1")
player2 = Player(int(input[1][-1]), 1000, "p2")


def takeTurn(p, p2):
    p.turn([rollDice(), rollDice(), rollDice()])
    if p.checkWin():
        winner = p
        loser = p2
        return winner, loser
    return takeTurn(p2, p)


winner, loser = takeTurn(player1, player2)

print("Part One : " + str(loser.score * numberOfTimesRolled))


print("Part Two : " + str(None))

print("time elapsed: " + str(time() - start))
