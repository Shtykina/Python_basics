my_list = [19, 17, 13, 11, 11, 11, 7, 5, 3, 3]
el = int(input("Введите натуральное число: "))
for x in my_list:
    i = my_list.count(el)
    if i > 0:
        j = my_list.index(el)
        my_list.insert(j + i, el)
        break
    else:
        if el > x:
            j = my_list.index(x)
            my_list.insert(j, el)
            break
        elif el < my_list[len(my_list) - 1]:
            my_list.append(el)
            break
print(my_list)