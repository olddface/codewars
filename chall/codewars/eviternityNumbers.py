'''pokokny di setiap digit harus ada 8/5/3
8 > 5 > 3
cth:
83 False:
soalny gak ada 5 kan 5 > 3
53 False:
soalny gak ada 8 kan 8 > 5 > 3
'''
def solve(a, b):
    txt = ""
    conditionMain = False
    condition1 = False
    for a in range(b):
        txt = str(a)
        for i in range(len(txt)):
            if(int(txt[i]) == 8):
                if len(txt) == 1:
                    condition1, conditionMain = True, True
                else:
                    conditionMain = True
                    for j in range(len(txt)):
                        if(int(txt[j]) == 5):
                            condition1 = True
        if conditionMain and condition1:
            print(a)
            conditionMain = False
            condition1 = False
solve(0, 100)