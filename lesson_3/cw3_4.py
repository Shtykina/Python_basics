a = float(input("Введите действительное положительное число: "))
b = int(input("Введите целое отрицательное число: "))

"""Способ №2 по условию задачи"""
def my_func(x, y):
    if b > 0:
        print("Читай условие задачи!")
    else:
        i = y
        s = 1
        while i < 0:
            s = s / x
            i = i + 1
        return s


print(my_func(a, b))

"""Способ №1 по условию задачи"""
def my_func(x, y):
    p = x ** y
    return p


print(my_func(a, b))
