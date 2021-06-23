from math import factorial


def fact(n):
    cnt = 1
    while cnt <= n:
        yield factorial(cnt)
        cnt +=1


n = int(input("Введите число для вычисления факториала: "))
for el in fact(n):
    print(el)
