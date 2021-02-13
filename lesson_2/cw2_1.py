s = (1234)
l1 = list((str(s)))
l1.append("пять")
l1.pop(0)
l1.insert(0, "Раз")
l1.remove("3")
l1.insert(2, "три")
print(l1)

t = "Вышел зайчик погулять"
l2 = t.split()
print(l2)

l3 = (["Вдруг", "дворник"], "выбегает")
l3[0][1] = "охотник"
print(l3)

l4 = {"Прямо", "в зайчика"}
l4.add("стреляет")
print(l4)

l5 = {"one": "Пиф-паф!",
      "two": "Ой-ой-ой!"}
print(l5.values())

l6 = {'Умирает': 'wtf?!!', 'зайчик': None, 'мой': 'whose'}
for el in l6:
    if l6[el] == None:
        print(f"Умирает {el} мой")

l = (l1, l2, l3, l4, l5, l6)
for x in l:
    print(type(x), end=" ")





