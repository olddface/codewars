def int_to_negabinary(a):
    base, absolute_base = -2, 2 #base -2 karna itu negative binary
    holder = ""
    if a == 0: #a is also quotient
        return "0"
    while a != 0:
        if a % base < 0:
            remainder = a % absolute_base
            a = a // base+1
        else:
            remainder = a % base
            a = a // base
        holder += str(remainder)

    return holder[::-1]
def negabinary_to_int(a):
    base = -2
    index,total = 0, 0
    value_holder = []
    for i in reversed(a):
        if int(i) == 1:
            total += 1 * ((-2) ** index)
            value_holder.append(total)
        index += 1
    print(total)
    return total

negabinary_to_int("11010")
