""" Advent of code Year 2024 Day 22 solution
Link to task: https://adventofcode.com/2024/day/22
Author = Averbea
Date = 22/12/2024
"""
from collections import defaultdict

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    return [int(x) for x in input_data.splitlines()]


def mix(secret, to_mix):
    return secret ^ to_mix

def prune(secret):
    return secret % 16777216

def next_secret(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune( mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    initial_secrets = process_input(input_data)
    total_sum = 0
    for initial_secret in initial_secrets:
        secret = initial_secret
        for i in range(2000):
            secret = next_secret(secret)
        total_sum += secret
    return total_sum


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""

    data = process_input(input_data)
    all_secrets = []
    for initial_secret in data:
        cur_secrets = [initial_secret]
        for i in range(2000):
            secret = next_secret(cur_secrets[-1])
            cur_secrets.append(secret)
        all_secrets.append(cur_secrets)

    all_price_differences = []
    for secrets_for_buyer in all_secrets:
        tmp_diffs = [(secrets_for_buyer[0] % 10, None)] # price, diff to previous

        for _, secret in enumerate(secrets_for_buyer[1:]):
            prev_price, prev_diff = tmp_diffs[-1]
            next_price = secret % 10
            tmp_diffs.append((next_price, next_price - prev_price))
        all_price_differences.append(tmp_diffs)


    bananas = defaultdict(int)
    for diffs_per_buyer in all_price_differences:
        seen = set()
        for i in range(len(diffs_per_buyer) - 3):
            last_4 = tuple([d[1] for d in diffs_per_buyer[i:i + 4]])
            if last_4 not in seen:
                bananas[last_4] += diffs_per_buyer[i + 3][0]
                seen.add(last_4)

    return max(bananas.values())




if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

