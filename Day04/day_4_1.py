def read(f):
    fileContent = open(f, 'r')
    array = []
    for line in fileContent.readlines():
        array.append(line.rstrip('\n'))
    array.append('')
    fileContent.close()
    return array


def getValidPassports(passports_raw_data, required_fields):
    passports = []
    passport = ""
    req_len = len(required_fields)

    for line in passports_raw_data:
        if line == '':
            passports.append(passport)
            passport = ""
        passport += line + " "

    valid_passports = 0
    for line in passports:
        pass_valid_number = 0
        for req in required_fields:
            if req in line:
                pass_valid_number += 1
        if pass_valid_number == req_len:
            valid_passports += 1
    return valid_passports

passports_raw_data = read("input.txt")
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

print(getValidPassports(passports_raw_data, required_fields))