def read(f):
    fileContent = open(f, 'r').readlines()
    array = []
    for line in fileContent:
        array.append(int(line.strip()))
    return array


def findThree(array, number):
    length = len(array)
    for i in range(0, length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if array[i] + array[j] + array[k] == number:
                    print(array[i] * array[j] * array[k])
                    return True
    return False


findThree(read("input.txt"), 2020)
