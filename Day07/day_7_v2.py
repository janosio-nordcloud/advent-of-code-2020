def read(f):
    fileContent = open(f, 'r')
    array = []
    for line in fileContent.readlines():
        array.append(line.strip())
    fileContent.close()
    return array


def prepareData(f):
    bags = []
    for i in f:
        bag = {}
        tmp1 = i.split(" bags contain ")
        bag["name"] = tmp1[0]
        bag["children"] = []
        tmp2 = tmp1[1].split(", ")
        for child in tmp2:
            children = {}
            ch = child.split(" ")
            quantity = ch[0]
            name = ch[1] + " " + ch[2]
            if quantity != "no":
                children["quantity"] = int(quantity)
                children["name"] = name
                bag["children"].append(children)
        bags.append(bag)
    return bags


f = read("input.txt")
bags = prepareData(f)
print(bags)

target = "shiny gold"
count = 0

# TBD....


print count
