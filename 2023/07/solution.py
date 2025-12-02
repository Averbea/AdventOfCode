""" Advent of code Year 2023 Day 7 solution
Author = Averbea
Date = December 2023
"""

import os
from collections import Counter
from functools import cmp_to_key
from time import time


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end - time_start, result


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read().splitlines()
    return [line.split(' ') for line in inputs]


def get_hand_value(hand):
    """returns the value of a hand"""
    char_count = Counter(hand[0])

    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    if sorted_char_count[0][1] == 5:  # five of a kind
        return 7
    elif sorted_char_count[0][1] == 4:  # four of a kind
        return 6
    elif sorted_char_count[0][1] == 3 and sorted_char_count[1][1] == 2:  # full house
        return 5
    elif sorted_char_count[0][1] == 3:  # three of a kind
        return 4
    elif sorted_char_count[0][1] == 2 and sorted_char_count[1][1] == 2:  # two pairs
        return 3
    elif sorted_char_count[0][1] == 2:
        return 2
    else:
        return 1


def first_different_char(hand1, hand2):
    """finds the first different character in two hands"""
    idx = 0
    while idx < len(hand1[0]) and hand1[0][idx] == hand2[0][idx]:
        idx += 1
    if idx == len(hand1[0]):
        return -1
    return idx


def get_joker_hand_value(hand):
    hand, bet = hand
    # replace joker with all possible values
    joker_hands = []
    for i in range(12):
        joker_hands.append(hand.replace('J', '23456789TQKA'[i]))
    max_val = 0
    for j_hand in joker_hands:
        max_val = max(get_hand_value([j_hand, bet]), max_val)

    return max_val


def compare_hands(hand1, hand2, jasjoker=False):
    """compares two hands"""
    hand1_value = get_joker_hand_value(hand1) if jasjoker else get_hand_value(hand1)
    hand2_value = get_joker_hand_value(hand2) if jasjoker else get_hand_value(hand2)
    if hand1_value < hand2_value:
        return -1
    elif hand1_value > hand2_value:
        return 1
    else:
        idx = first_different_char(hand1, hand2)
        if idx == -1:
            return 0
        if jasjoker:
            handvals = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
        else:
            handvals = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        if handvals.index(hand1[0][idx]) < handvals.index(hand2[0][idx]):
            return 1
        return -1

def calculate_winnings(hands):
    """calculates the winnings for a list of hands"""
    winnings = 0
    for rank, hand in enumerate(hands):
        winnings += (rank + 1) * int(hand[1])
    return winnings

def part_one():
    """Solution for Part 1"""
    hands = parse_input()
    hands.sort(key=cmp_to_key(compare_hands))
    winnings = calculate_winnings(hands)
    return winnings


def part_two():
    """Solution for Part 2"""
    hands = parse_input()
    hands.sort(key=cmp_to_key(lambda h1, h2: compare_hands(h1, h2, True)))
    winnings = calculate_winnings(hands)
    return winnings


def main():
    """main method"""
    time_needed, result = measure_timing(part_one)

    print("Part One : " + str(result))
    print("time elapsed: " + str(time_needed))

    time_needed, result = measure_timing(part_two)
    print("\nPart Two : " + str(result))
    print("time elapsed: " + str(time_needed))


if __name__ == "__main__":
    main()
