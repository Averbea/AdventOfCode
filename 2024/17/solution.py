""" Advent of code Year 2024 Day 17 solution
Link to task: https://adventofcode.com/2024/day/17
Author = Averbea
Date = 17/12/2024
"""

from utils.templateutils import timeit, read_input_file


def process_input(input_data: str):
    """parses the input file and returns the result"""
    data = input_data.split("\n\n")

    registers = [int(line.split(" ")[2]) for line in data[0].splitlines()]
    register_dict = {}
    for i, register in enumerate(registers):
        register_dict["ABC"[i]] = register

    instructions = [int(num) for num in data[1].split(" ")[1].split(",")]
    return register_dict, instructions


class Program:
    registers: dict
    instructions: list
    instruction_pointer: int

    output: list

    def __init__(self, registers, instructions):
        self.registers = registers
        self.instructions = instructions
        self.instruction_pointer = 0
        self.output = []

    def combo_operand(self, operand):
        match operand:
            case 4:
                operand = self.registers["A"]
            case 5:
                operand = self.registers["B"]
            case 6:
                operand = self.registers["C"]
            case 7:
                raise Exception("Invalid operand")
        return operand

    def adv(self, op):
        self.registers["A"] = self.registers["A"] // (2 ** self.combo_operand(op))

    def bxl(self, op):
        self.registers["B"] = self.registers["B"] ^ op

    def bst(self, op):
        self.registers["B"] = self.combo_operand(op) % 8

    def jnz(self, op):
        if self.registers["A"] != 0:
            self.instruction_pointer = op - 2  # will be increased afterward again

    def bxc(self, op):
        self.registers["B"] = self.registers["B"] ^ self.registers["C"]

    def out(self, op):
        self.output.append(self.combo_operand(op) % 8)

    def bdv(self, op):
        self.registers["B"] = self.registers["A"] // (2 ** self.combo_operand(op))

    def cdv(self, op):
        self.registers["C"] = self.registers["A"] // (2 ** self.combo_operand(op))

    def run_program(self):

        while self.instruction_pointer < len(self.instructions):
            opcode = self.instructions[self.instruction_pointer]
            operand = self.instructions[self.instruction_pointer + 1]
            match opcode:
                case 0:
                    self.adv(operand)
                case 1:
                    self.bxl(operand)
                case 2:
                    self.bst(operand)
                case 3:
                    self.jnz(operand)
                case 4:
                    self.bxc(operand)
                case 5:
                    self.out(operand)
                case 6:
                    self.bdv(operand)
                case 7:
                    self.cdv(operand)

            self.instruction_pointer += 2

        return self.output


@timeit
def part_one(input_data: str):
    """Solution for Part 1"""
    registers, instructions = process_input(input_data)

    program = Program(registers, instructions)
    ret = program.run_program()
    return str(ret).replace(" ", "")[1:-1]


@timeit
def part_two(input_data: str):
    """Solution for Part 2"""
    registers, instructions = process_input(input_data)
    #  2, 4,  b = combo(4) % 8              b = a % 8           b is the last 3 bits of a (0 after first iteration)
    #  1, 2,  b =  b ^ 2                    b = b ^ 2           b will be 0x010 (2) after first iteration
    #  7, 5,  c = a // (2 ** combo(5))      c = a // (2 ** b)   c is a // 4 after first iteration aka removes the last 2 bits of a
    #  1, 3,  b = b ^ 3                     b = b ^ 3
    #  4, 3,  b = b ^ c                     b = b ^ c
    #  5, 5,  print(combo(5) % 8)           print(b % 8)
    #  0, 3,  a = a // (2 ** combo(3))      a = (a // 8)         this removes the last 3 bits of a
    #  3, 0   if a != 0: goto 0             if a != 0: goto 0

    # only the last 3 bits of a are used (this will always be 0 after first iteration)
    # the first output depends only on the last 3 bits of a, the second on the second last 3 bits of a, etc.


    registers["A"] = 0 # reset to 0 so we can try out all vals
    return find_a_dfs(registers, instructions)



def find_a_dfs(registers, prog, ip=-1):
    """This was hard to figure out. Solved with tips from the subreddit."""
    if abs(ip) > len(prog):
        return registers["A"]
    for i in range(8):
        new_regs = registers.copy()
        new_a =  (registers["A"] << 3) + i
        new_regs["A"] = new_a
        program = Program(new_regs, prog)
        output = program.run_program()
        if output[0] == prog[ip]:
            program.registers["A"] = new_a # register A is reset to 0 after each iteration, so we set it again. B and C will be 0 already
            aa = find_a_dfs(program.registers, prog, ip - 1)
            if aa is not None:
                return aa
    return None


if __name__ == "__main__":
    file_content = read_input_file(test=False)
    print("Part One : " + str(part_one(file_content)) + "\n")
    print("Part Two : " + str(part_two(file_content)))
