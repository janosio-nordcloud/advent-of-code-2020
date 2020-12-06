import fileinput
import string

lines = list(fileinput.input('input.txt'))
lines.append('')

answer_1, answer_2, asciChars = 0, 0, string.ascii_lowercase
anyYes, allYes = set(), set(asciChars)

for line in lines:
    line = line.strip()
    if not line:
        answer_1 += len(anyYes)
        answer_2 += len(allYes)
        anyYes, allYes = set(), set(asciChars)
    else:
        for char in line:
            anyYes.add(char)
        for char in asciChars:
            if char not in line and char in allYes:
                allYes.remove(char)

print("any: ", answer_1)
print("all: ", answer_2)
