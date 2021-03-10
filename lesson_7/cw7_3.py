class Cell:
    def __init__(self, number_of_cells):
        self.number = number_of_cells

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if self.number - other.number > 0:
            return self.number - other.number
        else:
            return f"Subtraction is not possible!"

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return round(self.number / other.number)

    def make_order(self, rows):
        result = ""
        for i in range(self.number // rows):
            result += "*" * rows + "\n"
        result += "*" * (self.number % rows) + "\n"
        return result


c1 = Cell(25)
c2 = Cell(5)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(5))
