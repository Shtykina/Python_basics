dividend = float(input("Введите значение делимого: "))
divider = float(input("Введите значение делителя: "))


def div(a, b):
    if b == 0:
        print("Деление на ноль")
    else:
        return a / b


print(div(dividend, divider))
