def read(f):
    fileContent = open(f, 'r')
    array = []
    for line in fileContent.readlines():
        array.append(line.strip())
    fileContent.close()
    return array


input = read("input.txt")

match = 0
for i in input:
    policy = i.split(" ")

    [pos1, pos2] = list(map(int, policy[0].split("-")))
    letter = policy[1][0]

    first = policy[2][pos1 - 1] == letter
    second = policy[2][pos2 - 1] == letter

    if first ^ second:
        match += 1
print(match)
