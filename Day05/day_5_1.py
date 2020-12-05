import math


def read(f):
    fileContent = open(f, 'r')
    array = []
    for line in fileContent.readlines():
        array.append(line.strip())
    fileContent.close()
    return array

def splitRowsAndCols(string):
    return string[:7], string[7:]


def decodeRows(string):
    rows = list(string)
    min, max = 0, 127

    for row in rows:
        if row == "F":
            max = max - math.floor((max + 1 - min) / 2)
        if row == "B":
            min = min + math.ceil((max + 1 - min) / 2)
    return max


def decodeCols(string):
    cols = list(string)
    min, max = 0, 7

    for col in cols:
        if col == "L":
            max = max - math.floor((max + 1 - min) / 2)
        if col == "R":
            min = min + math.ceil((max + 1 - min) / 2)
    return max


def getSeatId(row, col, number=8):
    return int(row * number + col)


seats = read("input.txt")
seatsIds = []

for seat in seats:
    r, c = splitRowsAndCols(seat)
    seatId = getSeatId(decodeRows(r), decodeCols(c))
    seatsIds.append(seatId)

print(max(seatsIds))
