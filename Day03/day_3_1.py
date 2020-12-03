def read(f):
    fileContent = open(f, 'r')
    array = []
    for line in fileContent.readlines():
        array.append(line.strip())
    fileContent.close()
    return array


def findTrees(world, pattern):
    x, y, trees = 0, 0, 0
    dx, dy = pattern[0], pattern[1]
    mapHeight, lineLength = len(world), len(world[0])
    for _ in world:
        x += dx
        y += dy
        if y < mapHeight:
            x = x % lineLength
            if world[y][x] == "#":
                trees += 1
    return trees


inputMap = read("input.txt")
print(findTrees(inputMap, [3, 1]))

