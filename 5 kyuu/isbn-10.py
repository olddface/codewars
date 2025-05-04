def valid_ISBN10(isbn):
    index = 0
    remainder = 0
    countChara = 0
    if len(isbn) != 10:
        return False
    for i in isbn:
        index += 1
        if i.isdigit():
            i = int(i)
            remainder += index * i
        else:
            countChara += 1
            if i.lower() == "x" and index == 10:
                remainder += index * 10
            elif i.lower() == "x" and index != 10:
                return False
            else:
                remainder += index * 0

        print(i," * ",index, " = ", index * i, "\n", "total = ", remainder, "\n\n")
    if countChara == 10:
        return False
    remainder = remainder % 11
    return remainder == 0

jon = valid_ISBN10('048665088X')
print(jon)