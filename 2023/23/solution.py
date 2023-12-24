""" Advent of code Year 2023 Day 23 solution
Author = Averbea
Date = December 2023
"""
from collections import deque
from functools import cache

from matplotlib import pyplot as plt
from tqdm import tqdm

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    return tuple([tuple(row) for row in file.splitlines()])


def visualize(data):
    """Visualizes the data in a matplotlib plot"""
    figsize = len(data) // 3
    color_mapping = {
        '#': 'black',
        '.': 'white',
        '<': 'lightblue',
        '>': 'lightblue',
        'v': 'lightblue',
        '^': 'lightblue'
    }
    crossings = find_crosssings(data)

    # Erstelle das Bild
    fig, ax = plt.subplots()
    fig.set_size_inches((figsize, figsize))

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            color = color_mapping.get(char, 'white')
            if (i, j) in crossings:
                color = 'red'
            ax.add_patch(plt.Rectangle((j, -i), 1, 1, facecolor=color, edgecolor="gray", linewidth=5))
            # add arrows
            if char in ('>', '<', 'v', '^'):
                arrow_color = 'black'
                dx, dy = 0, 0
                x, y = j + .5, -i + .5
                if char == '>':
                    dx = 0.6
                    x -= .3
                elif char == '<':
                    dx = -0.6
                    x += .3
                elif char == 'v':
                    dy = -0.6
                    y += .3
                elif char == '^':
                    dy = 0.6
                    y -= .3

                arrow = plt.Arrow(x, y, dx, dy, color=arrow_color)
                ax.add_patch(arrow)
    # add numbers
    for j in range(len(data[0])):
        ax.text(j + 0.5, 1.5, str(j), ha='center', va='center', color='black')
    for i in range(len(data)):
        ax.text(-.5, -i + 0.5, str(i), ha='center', va='center', color='black')

    ax.set_xlim(0, len(data[0]) + 1)
    ax.set_ylim(-len(data) - 1, 1)
    ax.axis('off')

    # Zeige das Bild an
    plt.show()


@cache
def get_possible_steps(pos, data, ignore_slopes=False):
    """Returns all possible steps from the given position"""
    row, col = pos
    cur_symbol = data[row][col]

    if not ignore_slopes:
        match cur_symbol:
            case '>':
                return [(row, col + 1)]
            case '<':
                return [(row, col - 1)]
            case '^':
                return [(row - 1, col)]
            case 'v':
                return [(row + 1, col)]

    steps = []
    if row > 0 and data[row - 1][col] != '#':
        steps.append((row - 1, col))
    if row < len(data) - 1 and data[row + 1][col] != '#':
        steps.append((row + 1, col))
    if col > 0 and data[row][col - 1] != '#':
        steps.append((row, col - 1))
    if col < len(data[0]) - 1 and data[row][col + 1] != '#':
        steps.append((row, col + 1))

    return steps


def get_net_graph(data, ignore_slopes=False):
    starting_pos = (0, data[0].index('.'))
    target_pos = (len(data) - 1, data[-1].index('.'))
    crossings = find_crosssings(data) + [starting_pos, target_pos]
    net_graph = {}
    for crossing in crossings:
        net_graph[crossing] = []
        possible_from_crossing = get_possible_steps(crossing, data, ignore_slopes=ignore_slopes)
        for step in possible_from_crossing:
            path = set()
            path.add(crossing)
            path.add(step)
            last = step
            possible = get_possible_steps(last, data, ignore_slopes=ignore_slopes)
            while True:
                if len(possible) == 1 and possible[0] in path:
                    break
                next_pos = possible[0] if possible[0] not in path else possible[1]
                path.add(next_pos)
                last = next_pos
                possible = get_possible_steps(last, data, ignore_slopes=ignore_slopes)

                found = False
                for cr in crossings:
                    if cr in possible:
                        net_graph[crossing].append((cr, len(path)))
                        found = True
                if found:
                    break
    return net_graph


def find_crosssings(data):
    """Finds all crossings"""
    crossings = []
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == '#':
                continue
            possible = get_possible_steps((i, j), data)
            if len(possible) > 2:
                crossings.append((i, j))
    return crossings


@timeit
def part_one():
    """Solution for Part 1"""
    data = process_input()
    starting_pos = (0, data[0].index('.'))
    target_pos = (len(data) - 1, data[-1].index('.'))
    # visualize(data)
    pathlengths = []
    paths = []
    starting_path = set([starting_pos])

    paths.append((starting_path, starting_pos))
    while paths:
        path, last = paths.pop()
        possible = get_possible_steps(last, data)
        while len(possible) == 2:
            next = possible[0] if possible[0] not in path else possible[1]
            path.add(next)
            last = next
            possible = get_possible_steps(last, data)
            if last == target_pos:
                pathlengths.append(len(path) - 1)
                break

        for step in possible:
            if step == target_pos:
                pathlengths.append(len(path) - 1)
            if step not in path:
                if len(possible) == 1:
                    new_path = path
                else:
                    new_path = path.copy()
                new_path.add(step)
                paths.append((new_path, step))
    return max(pathlengths)


@timeit
def part_two():
    """Solution for Part 2"""
    data = process_input()
    # visualize(data)
    net = get_net_graph(data, ignore_slopes=True)
    starting_pos = (0, data[0].index('.'))
    target_pos = (len(data) - 1, data[-1].index('.'))

    path_lengths = []
    paths = []
    paths.append((starting_pos, [], 0))
    while paths:
        last, path, length = paths.pop()
        for next, next_length in net[last]:
            if next == target_pos:
                path_lengths.append(length + next_length)
            if next not in path:
                new_path = path.copy()
                new_path.append(next)
                paths.append((next, new_path, length + next_length))

    return max(path_lengths)  # solve(data, True)


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
