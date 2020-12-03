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

    [minimum, maximum] = list(map(int, policy[0].split("-")))
    letter = policy[1][0]
    number = policy[2].count(letter)

    if maximum >= number >= minimum:
        match += 1

print(match)
