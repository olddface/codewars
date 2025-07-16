x = ''
def rgb(r):
    Hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    remainder =0
    if r > 0:
        remainder = r % 16
        global x
        print(rgb(int(r/16)))
        x += Hex[remainder]
    else:
        return 0
    return x
print(rgb(99))
