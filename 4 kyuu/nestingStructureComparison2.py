def same_structure_as(original, other):
    return func(original, other, 0)
def func(Or, Ot, In):
    try:
        if len(Or[In]) != len(Ot[In]):
            return False
    except:
        return False

    if In == len(Or)-1:
        return True
    else:
        func(Or[In], Ot[In], In+1)
    return True

print(same_structure_as([[],[[]]], [[],[2,9]]))