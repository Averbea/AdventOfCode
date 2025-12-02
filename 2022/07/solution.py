""" Advent of code Year 2022 Day 7 solution
Author = Averbea
Date = December 2022
"""


import os
import re
from time import time


def measure_timing(func):
    """measures the time needed for executing the given function"""
    time_start = time()
    result = func()
    time_end = time()
    return time_end-time_start, result


def parse_input():
    """parses the input file and returns the result"""
    with open(os.path.dirname(__file__) + "/input.txt", 'r', encoding="UTF-8") as input_file:
        inputs = input_file.read()
    # find all blocks of commands (start with $)
    entries = re.findall(r"(?<=\$\s)[^\$]*", inputs)
    commands = []
    for entry in entries:
        if re.match(r"^cd", entry):
            # remove cd and \n from line
            args = entry[3:-1]
            command = {
                "command": "cd",
                "args": args
            }
            commands.append(command)
        else:
            lines = entry.split("\n")
            # first line is "ls", other lines are output lines
            command = {
                "command": "ls",
                "output": lines[1:]
            }
            commands.append(command)
    return commands


def parse_filesystem():
    """parses the input and create a filesystem data structure"""
    commands = parse_input()

    filesystem = Folder("root")

    # cur_item tracks the currently seleted folder
    cur_folder = filesystem
    for command in commands:
        if command["command"] == "cd":
            # Change directory
            target_directory = command["args"]
            if target_directory == "..":
                cur_folder = cur_folder.parent
            elif target_directory == "/":
                cur_folder = filesystem
            else:
                # target_directory is a folder
                new_folder = Folder(target_directory)
                cur_folder.append_child(new_folder)
                cur_folder = new_folder
        elif command["command"] == "ls":
            # List files
            for output in command["output"]:
                words = output.split(" ")
                if words[0] == "dir":
                    # this is a directory
                    diretory_name = words[1]
                    new_folder = Folder(diretory_name)
                    cur_folder.append_child(new_folder)
                else:
                    if words[0] == "":
                        continue
                    # this is a file
                    file_name = words[1]
                    file_size = int(words[0])
                    cur_folder.append_child(File(file_name, file_size))
    return filesystem


class FileSystem:
    """Base class for File System Items"""

    def __init__(self, name) -> None:
        self.parent = None
        self.name = name
        self.children = {}

    def get_size(self):
        """get the size of this File System Item and it's contents"""
        total_size = 0
        for _, child in self.children.items():
            total_size += child.get_size()
        return total_size

    def print(self, prefix=""):
        """print this File System and its contents to the console"""
        print(prefix + "--" + str(self))
        for _, child in self.children.items():
            child.print(prefix + "  |")


class Folder(FileSystem):
    """Class representing a folder"""

    def __str__(self) -> str:
        return self.name + "   (dir)"

    def append_child(self, child):
        """Append a child to this folder"""
        child.parent = self
        self.children[child.name] = child


class File(FileSystem):
    """Class representing a File"""

    def __init__(self, name, size: int) -> None:
        super().__init__(name)
        self.size = size

    def get_size(self):
        return self.size

    def __str__(self) -> str:
        return self.name + "   (file, size:" + str(self.size) + ")"


def parse_filesystem_for_dirs(filesystem: FileSystem) -> list:
    """Parse the filesystem for directorys

    Args:
        filesystem (FileSystem): the filesystem to parse

    Returns:
        list: the diretories as list
    """
    dirs = []
    if isinstance(filesystem, File):
        return dirs

    for child in filesystem.children:
        subdirs = parse_filesystem_for_dirs(filesystem.children[child])
        dirs += subdirs
    dirs.append(filesystem)
    return dirs


def part_one():
    """Solution for Part 1"""
    # filesystem = parse_filesystem()
    filesystem = parse_filesystem()

    filesystem.print()

    dirs = parse_filesystem_for_dirs(filesystem)
    total_size = 0
    for directory in dirs:
        size = directory.get_size()
        if size <= 100000:
            total_size += size
    return total_size


def part_two():
    """Solution for Part 2"""
    total_space = 70000000
    space_needed = 30000000

    filesystem = parse_filesystem()
    dirs = parse_filesystem_for_dirs(filesystem)
    dir_sizes = []
    for directory in dirs:
        dir_sizes.append(directory.get_size())

    dir_sizes.sort()
    # the total space used is the size of the root directory and should be the biggest number
    space_used = dir_sizes[-1]

    # find the smallest file bigger than needed
    space_to_be_freed = space_used - (total_space - space_needed)
    for size in dir_sizes:
        if size > space_to_be_freed:
            return size

    return 0


def main():
    """main method"""
    time_needed, result = measure_timing(part_one)

    print("Part One : " + str(result))
    print("time elapsed: " + str(time_needed))

    time_needed, result = measure_timing(part_two)
    print("\nPart Two : " + str(part_two()))
    print("time elapsed: " + str(time_needed))


if __name__ == "__main__":
    main()
