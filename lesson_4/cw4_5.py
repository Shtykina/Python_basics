from functools import reduce


def multiplication(a, b):
    return a * b


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(multiplication, my_list))
