from collections import *


def read(fi):
    f = open(fi, "r")
    return [int(line.strip()) for line in f.readlines() if line.strip()]


numbers = read("input.txt")
sums = set()
length = len(numbers)
ans = 0
for i, n in enumerate(numbers):
    valid = n in sums or i < 25
    if not valid:
        print("part 1", n)
        ans = n
        break
    for j in range(length):
        sums.add(n + numbers[j])

for i in range(length):
    s = 0
    for j in range(i, length):
        s += numbers[j]
        if s == ans:
            rng = numbers[i:j+1]
            print("part 2", min(rng) + max(rng))