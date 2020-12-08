from collections import defaultdict


def read(f):
    file = open(f, "r")
    prog = [line.strip().split() for line in file.readlines() if line.strip()]
    return [(operation, int(value)) for operation, value in prog]


def runProgram(prog):
    acc = 0
    currentIndex = 0
    executed = set()
    while currentIndex < len(prog):
        if currentIndex in executed:
            return None

        executed.add(currentIndex)
        operation, value = prog[currentIndex]
        if operation == "acc":
            acc += value
            currentIndex += 1
        if operation == "jmp":
            currentIndex += value
        if operation == "nop":
            currentIndex += 1

    return acc


prog = read("input.txt")
for i in range(len(prog)):
    if prog[i][0] == "acc":
        continue
    newOperation = "jmp" if prog[i][0] == "nop" else "nop"
    newProgram = prog[:i] + [(newOperation, prog[i][1])] + prog[i+1:]
    accu = runProgram(newProgram)
    if accu is not None:
        print(accu)