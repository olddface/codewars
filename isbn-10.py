def valid_ISBN10(isbn):
    index = 0
    remainder = 0
    for i in isbn:
        index += 1
        i = int(i)
        remainder += index * i
    remainder = remainder % 11
    return remainder

jon = valid_ISBN10('048665088X')
print(jon)