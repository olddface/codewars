def sum_strings(x, y):
    sumX, sumY = 0, 0
    j = len(x) - 1
    for i in range(len(x)):
        sumX += int(x[i]) * 10**j
        j-= 1
    j = len(y) - 1
    for i in range(len(y)):
        sumY += int(y[i]) * 10**j
        j-= 1
    return str(sumX + sumY)
print(sum_strings('60142343249', '60193424324324'))