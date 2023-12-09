from utils.tenplateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file()
    # TODO parse input into correct data structure
    return file


@timeit
def part_one():
    """Solution for Part 1"""
    data = process_input()
    return 0


@timeit
def part_two():
    """Solution for Part 2"""
    data = process_input()
    return 0


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
