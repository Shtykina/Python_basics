from itertools import count, cycle
a = input("Введите стартовое число до 10: ")
for el in count(int(a)):
    if el > 10:
        break
    else:
        print(el)

i = 0
for el in cycle("WTF?"):
    if i > 11:
        break
    print(el)
    i += 1
