""" Advent of code Year 2022 Day 2 solution
Author = Averbea
Date = December 2022
"""


from time import time
import os

start = time()

with open(os.path.dirname(__file__) +"/input.txt", 'r', encoding="UTF-8") as inputFile:
    inputs = inputFile.read().split("\n")

GUIDE = []
for i in inputs:
    GUIDE.append(i.split(" "))

ENEMY_MOVES  = {
    'A': "Rock",
    'B': "Paper",
    'C': "Scissors"
}

RESPONSE_MOVES = {
    'X': "Rock",
    'Y': "Paper",
    'Z': "Scissors"
}

SCORES = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "win": 6,
    "lose": 0,
    "draw": 3
}

HANDS = ["Rock", "Paper", "Scissors"]


def result(enemy_move, your_move):
    """calculates the result of a round

    Args:
        enemy_move (string): the enemy Move
        your_move (string): your Move

    Returns:
        number: total score of round
    """

    e_index = HANDS.index(enemy_move)
    r_index = HANDS.index(your_move)

    if r_index == e_index:
        return "draw"

    if r_index == (e_index + 1 )% len(HANDS):
        return "win"

    return "lose"

def part_one():
    """solves part one

    Returns:
        number: the total score of part One
    """
    total_score = 0

    for guideround in GUIDE:
        e_move = ENEMY_MOVES[guideround[0]]
        r_move = RESPONSE_MOVES[guideround[1]]
        total_score += SCORES[r_move] +  SCORES[result(e_move, r_move )]
    return total_score


RESULTS = {
    'X': "lose",
    'Y': "draw",
    'Z': "win"
}

def response_for_result(enemy_move, expected_result):
    """calculates a response to get a result

    Args:
        enemy_move (string): the enemies move
        expected_result (string): the expected result

    Returns:
        str: move to counter enemy move for expected result
    """
    match expected_result:
        case "draw":
            return enemy_move
        case "win":
            return HANDS[(HANDS.index(enemy_move) + 1) % len(HANDS)]
        case "lose":
            return HANDS[(HANDS.index(enemy_move) -1 ) % len(HANDS)]

def part_two():
    """caluclates the solution for part two

    Returns:
        string: total score of part two
    """
    total_score = 0

    for guideround in GUIDE:
        enemy_move = ENEMY_MOVES[guideround[0]]
        expected_result = RESULTS[guideround[1]]
        res = response_for_result(enemy_move, expected_result)

        total_score += SCORES[res] + SCORES[expected_result]
    return total_score


if __name__ == "__main__":
    print("Part One : "+ str(part_one()))
    print("Part Two : "+ str(part_two()))

    print("time elapsed: " + str(time() - start))
