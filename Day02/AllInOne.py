def read(f):
    fileContent = open(f, 'r')
    array = []
    for line in fileContent.readlines():
        array.append(line.strip())
    fileContent.close()
    return array


passwords = read("input.txt")


def matchPasswords(array, method=1):
    match = 0
    for i in array:
        policy = i.split(" ")
        [num1, num2] = list(map(int, policy[0].split("-")))
        letter = policy[1][0]
        number = policy[2].count(letter)

        if method == 1 and num2 >= number >= num1:
            match += 1

        if method == 2:
            first = policy[2][num1 - 1] == letter
            second = policy[2][num2 - 1] == letter
            if first ^ second:
                match += 1

    return match


print(matchPasswords(passwords, 1))
print(matchPasswords(passwords, 2))
