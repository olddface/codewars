def jon(n):
    k = 0
    return jon2(n,k)
def jon2(n, k):
    print(n)
    if n <= 0:
        return k
    else:
        k+=1
        jon2(n-1,k)
    return k
print(jon(5))