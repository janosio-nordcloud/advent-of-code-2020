import re


def read(f):
    fileContent = open(f, 'r')
    array = []
    for line in fileContent.readlines():
        array.append(line.rstrip('\n'))
    array.append('')
    fileContent.close()
    return array


def formatData(passports_raw_data):
    passports = []
    passport = ""

    for line in passports_raw_data:
        if line == '':
            passports.append(passport)
            passport = ""
        passport += line + " "

    formated_passports = []
    for line in passports:
        passport = line.split(" ")
        formated_passport = {}
        for p in passport:
            data = p.split(":")
            if data[0] != "":
                formated_passport[data[0]] = data[1]
        formated_passports.append(formated_passport)

    return formated_passports

def getValidPasswords(passports, required_fields):
    req_len = len(required_fields)
    valid_passports = 0

    for passport in passports:
        valid = 0
        for field in required_fields:
            if field in passport.keys():
                if field == 'byr':
                    if 1920 <= int(passport[field]) <= 2002:
                        valid += 1

                if field == 'iyr':
                    if 2010 <= int(passport[field]) <= 2020:
                        valid += 1

                if field == 'eyr':
                    if 2020 <= int(passport[field]) <= 2030:
                        valid += 1

                if field == 'hgt':
                    if passport[field].find("cm") != -1:
                        if 150 <= int(passport[field].split("cm")[0]) <= 193:
                            valid += 1
                    if passport[field].find("in") != -1:
                        if 59 <= int(passport[field].split("in")[0]) <= 76:
                            valid += 1

                if field == 'hcl':
                    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport[field])
                    if match is not None:
                        valid += 1

                if field == 'ecl':
                    valid_eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    if passport[field] in valid_eyes:
                        valid += 1

                if field == 'pid':
                    match = re.search(r'^(\d{9})$', passport[field])
                    if match is not None:
                        valid += 1

        if valid == req_len:
            valid_passports += 1

    return valid_passports


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports_raw_data = read("input.txt")
passports = formatData(passports_raw_data)
print(getValidPasswords(passports, required_fields))
