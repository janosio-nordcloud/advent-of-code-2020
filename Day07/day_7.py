from collections import defaultdict, deque


def read(f):
    fileContent = open(f, 'r')
    array = []
    for line in fileContent.readlines():
        array.append(line.strip())
    fileContent.close()
    return array


bags = read("input.txt")
formatted = defaultdict(list)
groups = defaultdict(list)

for bag in bags:
    color, children = bag.split(" contain ")
    color = tuple(color.split()[:-1])
    if children.startswith("no"):
        continue
    formatted[color] = [(int(v.split()[0]), tuple(v.split()[1:-1])) for v in children.split(", ")]
    for _, v in formatted[color]:
        groups[v].append(color)

target = deque([("shiny", "gold")])
sum = {tuple(target[0])}

while target:
    u = target.popleft()
    for x in groups[u]:
        if x not in sum:
            target.append(x)
            sum.add(x)


def part_2(col):
    answer = 1
    for count, subcol in formatted[col]:
        answer += count * part_2(subcol)
    return answer


print("part 1", len(sum) - 1)
print("part 2", part_2(("shiny", "gold")) - 1)
