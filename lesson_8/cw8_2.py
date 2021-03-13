class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


a = float(input("Enter dividend: "))
b = float(input("Enter divisor: "))

try:
    res = a/b
except ZeroDivisionError:
    print("Zero Division Error")
else:
    print(f"The quotient is {res}")
