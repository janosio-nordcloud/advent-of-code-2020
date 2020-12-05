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
    string = string.replace("B", "1").replace("F", "0")
    return int(string, 2)


def decodeCols(string):
    string = string.replace("R", "1").replace("L", "0")
    return int(string, 2)


def getSeatId(row, col, number=8):
    return int(row * number + col)


seats = read("input.txt")
seatsIds = []

for seat in seats:
    r, c = splitRowsAndCols(seat)
    seatId = getSeatId(decodeRows(r), decodeCols(c))
    seatsIds.append(seatId)

print("max ID:", max(seatsIds))

for id in seatsIds:
    if not seatsIds.count(id + 1) and seatsIds.count(id + 2):
        print("your ID:", id+1)
