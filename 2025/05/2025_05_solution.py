from tqdm import tqdm, trange

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    # TODO parse input into correct data structure
    ranges, data = input_data.split("\n\n")
    ranges = [(int(start), int(end)) for start, end in (line.split("-") for line in ranges.splitlines())]
    fruits = [int(line) for line in data.splitlines()]
    return ranges, fruits


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    ranges, fruits = process_input(input_data)
    fresh = 0
    for fruit in fruits:
        for start, end in ranges:
            if start <= fruit <= end:
                fresh += 1
                break

    return fresh

@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    ranges, fruits = process_input(input_data)

    ranges = set(ranges)

    merged = []


    while ranges:
        cur_start, cur_end = ranges.pop()
        to_remove = set()
        for (start, end) in ranges.copy():
            if dotheyoverlap((cur_start, cur_end), (start, end)):
                cur_start = min(cur_start, start)
                cur_end = max(cur_end, end)
                to_remove.add((start, end))



        ranges -= to_remove
        if not hasoverlap((cur_start, cur_end), ranges):
            merged.append((cur_start, cur_end))
        else:
            ranges.add((cur_start, cur_end))

    total = 0
    for start, end in merged:
        total += end - start + 1
    return total


def hasoverlap(my_range, ranges):
    for r in ranges:
        if dotheyoverlap(my_range, r):
            return True
    return False

def dotheyoverlap(a,b) -> bool:
    start_a, end_a = a
    start_b, end_b = b

    if start_a > end_b or start_b > end_a:
        return False
    return True

if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

