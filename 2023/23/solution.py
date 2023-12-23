""" Advent of code Year 2023 Day 23 solution
Author = Averbea
Date = December 2023
"""
from collections import deque

from matplotlib import pyplot as plt

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    return [list(row) for row in file.splitlines()]


def visualize(data):
    """Visualizes the data"""
    color_mapping = {
        '#': 'black',
        '.': 'white',
        '<': 'lightblue',
        '>': 'lightblue',
        'v': 'lightblue',
        '^': 'lightblue'
    }

    # Erstelle das Bild
    fig, ax = plt.subplots()
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            color = color_mapping.get(char, 'white')
            ax.add_patch(plt.Rectangle((j, -i), 1, 1, color=color))

            # Wenn das Zeichen ein Pfeil ist, füge den Pfeil hinzu
            if char in ('>', '<', 'v', '^'):
                arrow_color = 'black'
                dx, dy = 0, 0
                if char == '>':
                    dx = -0.2
                elif char == '<':
                    dx = 0.2
                elif char == 'v':
                    dy = 0.2
                elif char == '^':
                    dy = -0.2

                arrow = plt.Arrow(j + 0.5, -i + 0.5, dx, dy, color=arrow_color)
                ax.add_patch(arrow)

    # Setze Achsen
    ax.set_xlim(0, len(data[0]) + 1)
    ax.set_ylim(-len(data) - 1, 1)
    ax.axis('off')

    # Zeige das Bild an
    plt.show()


def get_possible_steps(pos, data, ignore_slopes = False):
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

def solve(data, ignore_slopes = False):
    starting_pos = (0, data[0].index('.'))
    target_pos = (len(data) - 1, data[-1].index('.'))
    #visualize(data)
    pathlengths = []
    paths = []
    starting_path = set(starting_pos)
    paths.append((starting_path, starting_pos))
    while paths:
        path, last = paths.pop()
        possible = get_possible_steps(last, data, ignore_slopes=ignore_slopes)
        for step in possible:
            if step == target_pos:
                pathlengths.append(len(path)-1)
            if step not in path:
                if len(possible) == 1:
                    new_path = path
                else :
                    new_path = path.copy()
                new_path.add(step)
                paths.append((new_path, step))
    return max(pathlengths)

@timeit
def part_one():
    """Solution for Part 1"""
    data = process_input()
    return solve(data, False)



@timeit
def part_two():
    """Solution for Part 2"""
    data = process_input()
    return solve(data, True)


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
