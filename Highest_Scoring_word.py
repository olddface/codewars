def high(x):
    char = ['a''b''c''d''e''f''g''h''i''j''k''l''m''n''o''p''q''r''t''u''v''w''x''y''z']
    Arr = x.split(" ")
    sumArr = []
    for i in range(len(Arr)):
        sumArr.append( sum([ord(char) - 96 for char in Arr[i]]))
    return Arr[sumArr.index(max(sumArr))]
print(high("man i need a taxi up to ubud"))