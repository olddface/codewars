def is_isogram(word):
    if word == None or type(word) == int or word == "":
        return False
    jon = True
    arr = []
    kon = 0
    for i in word:
        if word.lower().count(i.lower()) > 1 and type(word) == str:
            jon = False
            arr.append(word.lower().count(i.lower()))
    kon += int(len(arr)/2)
    if jon == False and word.count(" ") > 1 or word.count("-") > 2:
        jon = True
    elif kon > 2:
        jon = True
    elif kon == 3 or kon == 4:
        jon = False
    print(jon, '      ------>', kon)
    return jon
print(is_isogram('raiproFlccsehapnn'))
# apadah yang atas true bnr
# yang bawah true salah
# hhlygyopacxrei
# duneogimeanzarl