#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
a = float(input("Сколько километров пробежал спортсмен в первый день: "))
b = float(input("Сколько километров хочет пробегать спортсмен в день: "))
n = 1
while a < b:
    a = 1.1 * a
    n = n + 1
print(f"Спортсмен добьется своего результата на: {n}" + " день")