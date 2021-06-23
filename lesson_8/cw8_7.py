class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def __add__(self, other):
        return f"{self.real + other.real} + {self.img + other.img}i"

    def __mul__(self, other):
        return f"{self.real * other.real - (self.img * other.img)} + {self.real * other.img + self.img * other.real}i"

    def __str__(self):
        return f"({self.real}{'+' if self.img > 0 else ''}{self.img}i)"


a = ComplexNumber(2, 3)
b = ComplexNumber(1, 2)
print(f"Sum of complex numbers: {a + b}")
print(f"Multiplication of complex numbers: {a * b}")
