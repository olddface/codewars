holder = "
def int_to_negabinary(a):
    base, absolute_base = -2, 2
    if a == 0:
        return holder[::-1]
    while a != 0:
        if a % base < 0:
            remainder = a % absolute_base
    # if a % base < 0:
    #     remainder = a % absolute_base
    #     quotient = a // base+1
    #     print('quotient= ', quotient, 'reminder = ', remainder)
    # else:
    #     remainder = a % base
    #     quotient = a // base
    #     print('quotient= ', quotient, 'reminder = ', remainder)
    holder = holder + str(remainder)
    return int_to_negabinary(quotient)
print(int_to_negabinary(-6))


def negabinary_to_int(s):
    pass