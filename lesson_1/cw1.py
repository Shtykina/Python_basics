#Решим квадратичное уравнение: y=a*x^2+b*x+c
a = 1
b = 2
c = int(input("Введите значение c: "))
x = int(input("Введите значение переменной x:"))
y = a * x ** 2 + b * x + c
print("y = ", y)

s = "Карл у Клары украл "
answer = input("Что Карл украл у Клары? ")
if answer == "кораллы":
    print("Верно! " + s + answer)
else:
    print("Да нет же, кораллы!")
