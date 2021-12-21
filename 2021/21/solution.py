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

rollCombinations = []
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            rollCombinations.append([i, j, k])



p1Wins = 0
p2Wins = 0
Roll_Sums = {3:1,4:3,5:6,6:7,7:6,8:3,9:1}

def game(rollSum,multiplier,  turn,pos1, pos2, score1, score2):
    global p1Wins, p2Wins, Roll_Sums
    if (score1 >= 21) or (score2 >= 21):
        return
    if turn == "p1":
        pos1 = (pos1 + rollSum) % 10

        score1 += pos1 +1
        if score1 >= 21:
            p1Wins +=  multiplier
        else:
            for total, freq in Roll_Sums.items():
                game(total,freq* multiplier, "p2", pos1, pos2, score1, score2 )
    elif turn == "p2":
        pos2 = (pos2 + rollSum) %10
        score2 += pos2 +1
        if score2 >= 21:
            p2Wins += 1 * multiplier
        else:
            for total, freq in Roll_Sums.items():
                game(total, freq * multiplier, "p1", pos1, pos2, score1, score2)

for total, freq in Roll_Sums.items():
    print(total)
    game(total, freq, "p1", int(input[0][-1]) -1 ,int(input[1][-1]) -1,0,0)
print("Part Two : ")
print("P1: " + str(p1Wins))
print("P2: " + str(p2Wins))



print("time elapsed: " + str(time() - start))
