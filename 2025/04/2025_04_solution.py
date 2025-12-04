from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    # TODO parse input into correct data structure
    positions = set()
    for line_idx, line in enumerate(input_data.splitlines()):
        for char_idx, char in enumerate(line):
            if char == "@":
                positions.add((line_idx, char_idx))
    return positions

DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    positions = process_input(input_data)
    total = 0

    for (y, x) in positions:
        count = 0
        for direction in DIRS:
            if (y + direction[0], x + direction[1]) in positions:
                count += 1
        if count < 4:
            total += 1


    return total


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    positions = process_input(input_data)
    total = 0
    current_removed = 1
    while current_removed >0 :
        current_removed = 0
        removed = set()
        for (y, x) in positions:
            count = 0
            for direction in DIRS:
                pos_to_check = (y + direction[0], x + direction[1])
                if pos_to_check in positions:
                    count += 1
            if count < 4:
                current_removed += 1
                removed.add((y,x))
        total += current_removed
        positions = positions - removed

    return total


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

