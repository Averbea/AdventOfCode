""" Advent of code Year 2023 Day 2 solution
Author = Averbea
Date = December 2023
"""
import os
from time import time


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read().splitlines()
    out = []
    for line in inputs:
        out.append([])
        game, line = line.split(':')
        game_no = game.split(' ')[1]

        draws = line.split(';')

        for draw in draws:
            counter = {
                'blue': None,
                'red': None,
                'green': None,
            }
            color = draw.split(',')
            for c in color:
                c = c.strip()
                for key in counter.keys():
                    if c.find(key) != -1:
                        counter[key] = int(c.split(' ')[0])
            out[-1].append(counter)
    return out


def part_one():
    """Solution for Part 1"""
    games = parse_input()

    bag = {
        'blue': 14,
        'red': 12,
        'green': 13,
    }
    possible_games = []
    for idx, game in enumerate(games):
        possible = True
        for draw in game:
            for key in draw.keys():
                if draw[key] and draw[key] > bag[key]:
                    possible = False
        if possible:
            possible_games.append(idx+1)

    return sum(possible_games)


def part_two():
    """Solution for Part 2"""
    games = parse_input()
    sum_of_powers = 0
    for game in games:
        min_bag = {
            'red': 0,
            'blue': 0,
            'green': 0,
        }
        for draw in game:
            for key in draw.keys():
                if draw[key] and draw[key] > min_bag[key]:
                    min_bag[key] = draw[key]

        power = min_bag['red'] * min_bag['blue'] * min_bag['green']
        sum_of_powers += power
    return sum_of_powers


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
