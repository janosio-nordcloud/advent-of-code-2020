def read(f):
    fileContent = open(f, 'r')
    array = []
    for line in fileContent.readlines():
        array.append(line.strip())
    fileContent.close()
    return array


def runProgram(program):
    acc = 0
    currentIndex = 0
    executedInstructions = []

    while not executedInstructions.count(currentIndex):
        instruction = program[currentIndex].split()
        if instruction[0] == 'acc':
            acc += int(instruction[1])
            executedInstructions.append(currentIndex)
            currentIndex += 1
        if instruction[0] == 'jmp':
            executedInstructions.append(currentIndex)
            currentIndex += int(instruction[1])
        if instruction[0] == 'nop':
            executedInstructions.append(currentIndex)
            currentIndex += 1
    print(acc)


prog = read("input.txt")
runProgram(prog)
