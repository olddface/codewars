def same_structure_as(original, other):
    return Recur(original, other)


def Recur(val1, val2):
    global jon
    if type(val1) != type(val2):
        return False
    if len(val1) == len(val2) == 0:
        return True
    if len(val1) != len(val2):
        return False
    for i in range(len(val1)):
        if bool(type(val1[i]) == list) != bool(type(val2[i]) == list):

            return False
        elif type(val1[i]) == type(val2[i]) == list:
            return same_structure_as(val1[i], val2[i])
    return True
    return jon