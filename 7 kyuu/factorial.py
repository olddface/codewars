def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    elif n == 0:
        return 1
    else:
        return factorial(n-1) * n
print(factorial(-5))