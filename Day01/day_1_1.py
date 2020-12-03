def read(f):
    fileContent = open(f, 'r').readlines()
    array = []
    for line in fileContent:
        array.append(int(line.strip()))
    return array


def findTwo(array, number):
    length = len(array)
    for i in range(0, length - 2):
        for j in range(i + 1, length - 1):
            if array[i] + array[j] == number:
                print(array[i] * array[j])
                return True
    return False


findTwo(read('input.txt'), 2020)