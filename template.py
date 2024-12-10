from utils.templateutils import timeit, read_input_file


def process_input(input_data):
    """parses the input file and returns the result"""
    # TODO parse input into correct data structure
    return input_data


@timeit
def part_one(input_data):
    """Solution for Part 1"""
    data = process_input(input_data)
    return 0


@timeit
def part_two(input_data):
    """Solution for Part 2"""
    data = process_input(input_data)
    return 0


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

