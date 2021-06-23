my_file = open("its_my_file.txt", "w")
while True:
    content = input("Желает ли мой господин ввести какие-то данные? Если нет, поставьте ! ")
    if content != "!":
        my_file = open("its_my_file.txt", "a", encoding="UTF-8")
        my_file.write(content)
        my_file.write("\n")
    else:
        break
my_file.close()
