def read(f):
    fileContent = open(f, 'r')
    array = []
    for line in fileContent.readlines():
        array.append(line.strip())
    fileContent.close()
    return array


def replaceChar(string, char, position):
    s = list(string)
    s[position] = char
    return "".join(s)


def generateMap(inputMap):
    newMap = []
    for m in inputMap:
        newMap.append(m * len(inputMap))
    return newMap


def findTrees(newMap, pattern):
    position = {
        "x": 0,
        "y": 0
    }
    trees = 0
    mapHeight = len(newMap)

    for line in newMap:
        if position["y"] < mapHeight - pattern[1] and position["x"] < len(line) - 1 - pattern[0]:
            position["x"] += pattern[0]
            position["y"] += pattern[1]

            if newMap[position["y"]][position["x"]] == "#":
                newMap[position["y"]] = replaceChar(newMap[position["y"]], "X", position["x"])
                trees += 1
    return trees


inputMap = read("input.txt")
newMap = generateMap(inputMap)
print(findTrees(newMap, [3, 1]))

