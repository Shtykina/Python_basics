t = input("Введите строку из нескольких слов: ")
for ind, el in enumerate(t.split(" ")):
    print(ind, el[:10:])
