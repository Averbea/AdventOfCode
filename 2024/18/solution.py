""" Advent of code Year 2024 Day 18 solution
Link to task: https://adventofcode.com/2024/day/18
Author = Averbea
Date = 18/12/2024
"""


from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    return [tuple(map(int, line.split(","))) for line in input_data.splitlines()]


def find_path(blocked, start, end):
    max_y = max_x = 70
    visited = set()
    # find the shortest path from start to end
    queue = [(*start, [])]
    while queue:
        y, x, path = queue.pop(0)
        if (y, x) == end:
            return path
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y <= max_y and 0 <= new_x <= max_x and (new_y, new_x) not in blocked | visited:
                visited.add((new_y, new_x))
                queue.append((new_y, new_x, path + [(new_y, new_x)]))
    return None

@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    data = process_input(input_data)
    blocked = set(data[:1024])
    end = (70, 70)
    start = (0,0)
    # find the shortest path from start to end
    shortest_path = find_path(blocked, start, end)
    return len(shortest_path)


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    data = process_input(input_data)

    i = 1024
    end = (70, 70)
    start = (0,0)
    blocked = set(data[:1024])
    path = find_path(blocked, start, end)
    while True:
        while data[i] not in path: # if the new point is not in path we do not need to recalculate the path
            blocked.add(data[i])
            i += 1

        blocked.add(data[i])
        path = find_path(blocked, start, end)

        if path is None:
            return str(data[i])[1:-1].replace(" ", "") # remove brackets and spaces




if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

