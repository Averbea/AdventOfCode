""" Advent of code Year 2023 Day 22 solution
Author = Averbea
Date = December 2023
"""
import re
from typing import Tuple

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm

from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    return [list(map(int, re.findall(r"\d+", line))) for line in file.splitlines()]


def plot_as_voxel(cubes_data):
    dim_x = max([int(x[3]) for x in cubes_data]) + 1
    dim_y = max([int(x[4]) for x in cubes_data]) + 1
    dim_z = max([int(x[5]) for x in cubes_data]) + 1
    # Prepare some coordinates
    x, y, z = np.indices((dim_x, dim_y, dim_z))

    fig = plt.figure(figsize=(12, 4))  # Adjust the figsize as needed
    ax1 = fig.add_subplot(131, projection="3d")  # Front view
    ax2 = fig.add_subplot(132, projection="3d", proj_type='ortho')  # Left view
    ax3 = fig.add_subplot(133, projection="3d", proj_type='ortho')  # Right view

    for ax, elev, azim in zip([ax1, ax2, ax3], [None, 0, 0], [None, 0, -90]):
        cubes = False
        # Draw cuboids
        for min_x, min_y, min_z, max_x, max_y, max_z in cubes_data:
            cubes |= (x >= min_x) & (x <= max_x) & \
                     (y >= min_y) & (y <= max_y) & \
                     (z >= min_z) & (z <= max_z)

        ax.voxels(cubes, edgecolor='k', facecolors='blue')
        ax.view_init(elev=elev, azim=azim)  # Set view angle

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

    plt.show()


def let_bricks_fall(bricks):
    amount_fallen = 0
    bricks.sort(key=lambda x: min(x[2], x[5]))
    x_length = max([x[3] for x in bricks])
    y_length = max([x[4] for x in bricks])
    # plot_as_voxel(bricks)
    heightmap = np.zeros((x_length + 1, y_length + 1))
    for brick in bricks:
        min_x, min_y, min_z, max_x, max_y, max_z = brick
        assert (min_y <= max_y)
        assert (min_x <= max_x)
        assert (min_z <= max_z)
        max_below = np.max(heightmap[min_y:max_y + 1, min_x:max_x + 1])
        diff = brick[2] - max_below - 1
        if diff >= 1:
            amount_fallen += 1

        brick[2] -= diff
        brick[5] -= diff
        heightmap[min_y:max_y + 1, min_x:max_x + 1] = brick[5]
    return amount_fallen


def get_supports_and_supported_by(bricks):
    supports = [set() for _ in range(len(bricks))]
    supported_by = [set() for _ in range(len(bricks))]
    for idx1, b1 in enumerate(bricks):
        outer_min_x, outer_min_y, outer_min_z, outer_max_x, outer_max_y, outer_max_z = b1

        # check which bricks are supported by b1
        for idx2, b2 in enumerate(bricks):
            if idx1 == idx2:
                continue
            inner_min_x, inner_min_y, inner_min_z, inner_max_x, inner_max_y, inner_max_z = b2
            if inner_min_z - 1 != outer_max_z:
                continue

            for y in range(inner_min_y, inner_max_y + 1):
                for x in range(inner_min_x, inner_max_x + 1):
                    if outer_min_y <= y <= outer_max_y and outer_min_x <= x <= outer_max_x:
                        supports[idx1].add(idx2)
                        supported_by[idx2].add(idx1)
    return supports, supported_by


@timeit
def part_one():
    """Solution for Part 1"""
    bricks = process_input()
    # let bricks fall
    let_bricks_fall(bricks)
    supports, supported_by = get_supports_and_supported_by(bricks)
    # plot_as_voxel(bricks)
    amount_to_safely_remove = 0
    for idx, brick in enumerate(bricks):
        bricks_supported_by_this = supports[idx]
        if len(bricks_supported_by_this) == 0:
            amount_to_safely_remove += 1
            continue
        for brick_supported in bricks_supported_by_this:
            if len(supported_by[brick_supported]) == 1:
                break
        else:
            amount_to_safely_remove += 1

    return amount_to_safely_remove


def amount_fallen_for(bricks: Tuple[Tuple[int, ...], ...], idx):
    new_bricks = [list(brick) for brick in bricks]
    new_bricks.pop(idx)
    return let_bricks_fall(new_bricks)


@timeit
def part_two():
    """Solution for Part 2"""
    bricks = process_input()
    let_bricks_fall(bricks)
    bricks = tuple([tuple(brick) for brick in bricks])
    sum_fallen = 0
    for idx, brick in enumerate(tqdm(bricks)):
        sum_fallen += amount_fallen_for(bricks, idx)
    return sum_fallen


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
