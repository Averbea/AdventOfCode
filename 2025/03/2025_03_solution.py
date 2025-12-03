from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    # TODO parse input into correct data structure
    return [[int(d) for d in line] for line in input_data.splitlines()]


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    data = process_input(input_data)
    total = 0
    for line in data:
        max_in_line  = max(line[:-1])
        first_index = line.index(max_in_line)
        max_after_max = max(line[first_index + 1 :])
        highest = max_in_line * 10 + max_after_max
        total += highest

    return total


def find(data: list[int], i:int):
    if i == 0:
        return 0
    max_in_line = max(data[:- i+1]) if i > 1 else max(data)
    first_index = data.index(max_in_line)
    return max_in_line * 10**(i-1) + find(data[first_index + 1 :], i - 1)

@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    data = process_input(input_data)
    total = 0
    for line in data:
        result = find(line, 12)
        print(result)
        total += result
    return total

if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

