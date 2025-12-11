""" Advent of code Year 2025 Day 11 solution
Link to task: https://adventofcode.com/2025/day/11
Author = Averbea
Date = 11/12/2025
"""
from collections import defaultdict
from functools import lru_cache


from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    graph = defaultdict()

    for line in input_data.splitlines():
        fr, *to = line.split(" ")
        fr = fr[:-1]
        graph[fr] = to
    return graph


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    graph = process_input(input_data)

    def dfs(current_node):
        if current_node == "out":
            return 1
        total = 0

        for neighbor in graph.get(current_node, []):
            total += dfs(neighbor)
        return  total
    return dfs("you")



@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    graph = process_input(input_data)

    memo = defaultdict(int)

    @lru_cache
    def dfs(current_node, found_dac=False, found_fft=False):

        memokey = (current_node, found_dac, found_fft)

        if memo.get(memokey) is not None:
            return memo[memokey]

        if current_node == "dac":
            found_dac = True
        if current_node == "fft":
            found_fft = True
        memokey = (current_node, found_dac, found_fft)


        if current_node == "out":
            if found_dac and found_fft:
                memo[memokey] = 1
                return 1
            else:
                memo[memokey] = 0
                return 0
        total = 0

        for neighbor in graph.get(current_node, []):
            total += dfs(neighbor, found_dac, found_fft)

        memo[memokey] = total

        return total

    return dfs("svr")


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

