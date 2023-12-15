""" Advent of code Year 2023 Day 15 solution
Author = Averbea
Date = December 2023
"""


from utils.templateutils import timeit, read_input_file


def process_input():
    """parses the input file and returns the result"""
    file = read_input_file(test=False)
    # TODO parse input into correct data structure
    return file.split(',')



def hash_phrase(phrase):
    """Hashes a phrase to a number"""
    hash_val = 0
    for char in phrase:
        hash_val += ord(char)
        hash_val *= 17
        hash_val %= 256
    return hash_val


@timeit
def part_one():
    """Solution for Part 1"""
    data = process_input()
    sum = 0
    for phrase in data:
        sum += hash_phrase(phrase)

    return sum


@timeit
def part_two():
    """Solution for Part 2"""
    data = process_input()
    hashmap = {i:{} for i in range(256)}
    for phrase in data:
        if phrase[-1] == '-':
            phrase = phrase[:-1]
            hash_val = hash_phrase(phrase)
            cur_dict = hashmap[hash_val]
            cur_dict.pop(phrase, None)

        else:
            phrase, focal_length = phrase.split('=')
            hash_val = hash_phrase(phrase)
            cur_dict = hashmap[hash_val]
            cur_dict[phrase] = focal_length

    focusing_power = 0
    for box_id, box in hashmap.items():
        for lens_id, focal_length in enumerate(box.values()):
            focusing_power += (box_id + 1) * (lens_id + 1) * int(focal_length)

    return focusing_power


if __name__ == "__main__":
    print("Part One : " + str(part_one()) + "\n")
    print("Part Two : " + str(part_two()))
