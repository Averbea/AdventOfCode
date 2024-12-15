""" Advent of code Year 2024 Day 15 solution
Link to task: https://adventofcode.com/2024/day/15
Author = Averbea
Date = 15/12/2024
"""


from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    the_map, movements = input_data.split("\n\n")

    walls = set()
    boxes = set()
    fish = ()
    for y, line in enumerate(the_map.split("\n")):
        for x, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            elif char == "O":
                boxes.add((x, y))
            elif char == "@":
                fish = (x, y)

    movements = movements.replace("\n", "")
    return walls, boxes, fish, movements


def print_map(walls, boxes, fish, in_part_two=False):
    if in_part_two:
        boxes_left = {box[0] for box in boxes}
        boxes_right = {box[1] for box in boxes}
        max_y = max(y for x, y in walls | boxes_left | {fish})
        max_x = max(x for x, y in walls | boxes_right | {fish})
    else:
        max_y = max(y for x, y in walls | boxes | {fish})
        max_x = max(x for x, y in walls | boxes | {fish})

    for y in range(max_y + 1 ):
        for x in range(max_x + 1):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) == fish:
                print("@", end="")
            elif (x, y) in boxes and not in_part_two:
                print("O", end="")
            elif in_part_two and (x, y) in boxes_left:
                print("[", end="")
            elif in_part_two and (x, y) in boxes_right:
                print("]", end="")
            else:
                print(".", end="")
        print("")
    print("")

DIRECTIONS = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
}

@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    walls, boxes, fish, movements = process_input(input_data)
    for movement in movements:
        dx, dy = DIRECTIONS[movement]
        new_fish = (fish[0] + dx, fish[1] + dy)
        if new_fish in walls:
            continue
        if new_fish in boxes:
            boxes_to_move = []
            cur_x, cur_y = new_fish
            while (cur_x, cur_y) in boxes:
                boxes_to_move.append((cur_x, cur_y))
                cur_x += dx
                cur_y += dy
            if(cur_x, cur_y) in walls:
                continue # Can't move the box

            for box in reversed(boxes_to_move):
                boxes.remove(box)
                boxes.add((box[0] + dx, box[1] + dy))
        fish = new_fish
        #print_map(walls, boxes, fish)

    total_sum = sum([100 * y + x for x, y in boxes])
    return total_sum



@timeit
def part_two(input_data: str):
    """Solution for Part 2"""

    walls, boxes, fish, movements = process_input(input_data)
    new_walls = set()
    for wall in walls:
        new_walls.add((wall[0] * 2, wall[1]))
        new_walls.add((wall[0] * 2 + 1, wall[1]))
    new_boxes = set()
    for box in boxes:
        new_boxes.add(((box[0] * 2, box[1]), (box[0] * 2 + 1, box[1])))

    fish = (fish[0] * 2, fish[1])
    walls = new_walls
    boxes = new_boxes


    for movement in movements:
        #print_map(walls, boxes, fish, True)
        #print("Moving", movement)
        dx, dy = DIRECTIONS[movement]
        new_fish = (fish[0] + dx, fish[1] + dy)
        collision_detected = False
        if new_fish in walls:
            continue

        if new_fish in [box[0] for box in boxes] + [box[1] for box in boxes]:
            boxes_to_move = []
            positions_to_check = [new_fish]

            while positions_to_check:
                pos_to_check = positions_to_check.pop()
                if pos_to_check in walls:
                    collision_detected = True
                    break

                # check each box left and right side for collision
                for box in boxes:
                    if pos_to_check in box:
                        boxes_to_move.append(box)
                        # if pushing right we don't want to check the pushed left side of box aka the current right side of box again
                        if dx != 1:
                            box_left_x, box_left_y = box[0]
                            to_add = (box_left_x + dx, box_left_y + dy)
                            if to_add not in positions_to_check:
                                positions_to_check.append(to_add)
                        # if pushing left we don't want to check the pushed right side of box aka the current left side of box again
                        if dx != -1:
                            box_right_x, box_right_y = box[1]
                            to_add = (box_right_x + dx, box_right_y + dy)
                            if to_add not in positions_to_check:
                                positions_to_check.append(to_add)

            if not collision_detected:
                # move the boxes
                new_boxes = {box for box in boxes if box not in boxes_to_move}
                for box in boxes_to_move:
                    new_boxes.add(((box[0][0] + dx, box[0][1] + dy), (box[1][0] + dx, box[1][1] + dy)))
                boxes = new_boxes


        if not collision_detected:
            fish = new_fish # move the fish

    #print_map(walls, boxes, fish, True)
    boxes_left = {box[0] for box in boxes}
    total_sum = sum([100 * y + x for x, y in boxes_left])
    return total_sum


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))

