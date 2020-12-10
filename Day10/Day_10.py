def read(fi):
    f = open(fi, "r")
    return [int(line.strip()) for line in f.readlines() if line.strip()]


def prepareAdapters(adapters):
    adapters.sort()
    return [0] + adapters + [adapters[-1] + 3]


def findAdapters(adapters, minimum, maximum):
    previous = 0
    min_len, max_len = 0, 0
    for adapter in adapters:
        if adapter - previous == minimum:
            min_len += 1
        elif adapter - previous == maximum:
            max_len += 1
        previous = adapter
    return min_len * max_len


def totalNumberOfDistinct(adapters):
    dist = [1]
    for i in range(1, len(adapters)):
        answer = 0
        for j in range(i):
            if adapters[j] + 3 >= adapters[i]:
                answer += dist[j]
        dist.append(answer)
    return dist[-1]


adapters = prepareAdapters(read("input.txt"))
print("Part 1: ", findAdapters(adapters, 1, 3))
print("Part 2: ", totalNumberOfDistinct(adapters))
