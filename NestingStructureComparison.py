def same_structure_as(original, other):
    jon = Recur(original, other)
    if isinstance(jon, bool):
        return jon
    else:
        if len(jon) == 0:
            return True
        else:
            return False
jon = []
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
            jon.append(False)
            break
        elif type(val1[i]) == type(val2[i]) == list:
            return same_structure_as(val1[i], val2[i])
    return True
    return jon


print(same_structure_as([[14, 17, 9, -20], [-10, -13, [-4, [-17, 20, -5, [-3, 11, [-3, [-3, 16]], -12]], [-1, [-2, -3], 10, -2], -13], -2], 20, -14, 18, 8, [[[[6, -19], -17, -15, -2], [[[-15, 14, [-19, -8], -13], [[], -1]], 12]], 6], 7]
, [[17, 1, -17, -20], [17, 16, [-11, [18, -2, -13, [-8, -13, [-16, [-20, 6]], 12]], [15, [-8, -2], 10, 0], -3], -10], -11, -20, -4, -1, [[[[3, -2], -8, 1, 9], [[[20, -1, [14, 13], -4], [[], 2]], -13]], 7], 18] ))