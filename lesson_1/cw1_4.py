a = int(input("Введите целое положительное число: "))
b = a % 10
while a > 10:
    a = a // 10
    if b < a % 10:
        b = a % 10
print(b)