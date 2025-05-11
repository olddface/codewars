def even_or_odd(number):
    if isinstance(number, (list, tuple)):
        return "Even" if number[0] % 2 ==0 else "Odd"
    return "Even" if number % 2 == 0 else "Odd"

print(even_or_odd([3]))  # prints "Odd"
