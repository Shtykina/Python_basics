def my_func(a, b, c):
    my_list = [a, b, c]
    s = min(a, b, c)
    my_list.remove(s)
    return sum(my_list)


print(my_func(5, 7, 3))
