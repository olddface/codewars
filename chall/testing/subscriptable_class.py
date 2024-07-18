class jon:
    def __init__(self, number):
        self.number = number
    def evenOrOdd(self):
        return "odd" if self.number % 2 == 0 else "even"
kon = jon(3)
print(kon.evenOrOdd())