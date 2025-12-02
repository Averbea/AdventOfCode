# Advent of code Year 2021 Day 4 solution
# Author = Averbea
# Date = December 2021
def checkWin(board):
    for line in board:
        if all(e["marked"] is True for e in line):
            return True

    for x in range(board_size):
        if all(board[y][x]["marked"] is True for y in range(board_size)):
            return True

    return False


def initializeBoards(lines):
    boards = []
    while len(lines) >= 5:
        board = []
        for line in lines[0:5]:
            line = [line[i:i + 3] for i in range(0, len(line), 3)]
            line = [el.strip() for el in line ]
            dictline = []
            for i in line:
                dictline.append(
                    {
                        "val": i,
                        "marked": False
                    }
                )
            board.append(dictline)
        boards.append(board)
        lines = lines[6:] #skip empty row between boards
    return boards


def markNumber(number, boards):
    for board in boards:
        for line in board:
            for d in line:
                if d["val"] == number:
                    d["marked"] = True
    return boards

def evaluateScore(board, lastNumber):
    sum = 0
    for line in winningBoard:
        for d in line:
            if d["marked"]  == False:
                sum += int(d["val"])


    return sum * lastNumber


with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
lines = input.split("\n")
board_size = 5

numbers = lines[0].split(',')
lines = lines[2:]

boards = initializeBoards(lines)

winningBoard = None
lastNumber = None

for number in numbers:
    boards = markNumber(number, boards)

    for board in boards:
        if checkWin(board):
            winningBoard = board
            lastNumber = number
            break
    if winningBoard:
        break


score = evaluateScore(winningBoard, int(lastNumber))
print("Part One : "+ str(score))


boards = initializeBoards(lines)
winningBoard = None
lastNumber = None

for number in numbers:
    boards = markNumber(number, boards)

    for board in boards:
        if checkWin(board):
            winningBoard = board
            lastNumber = number
            boards.remove(board)

score = evaluateScore(winningBoard, int(lastNumber))
print("Part Two : "+ str(score))