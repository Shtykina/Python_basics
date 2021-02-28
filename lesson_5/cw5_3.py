with open("file_for_5_3.txt", "r", encoding="UTF-8") as my_list:
    employees = []
    money = 0
    i = 0
    while True:
        line = my_list.readline()
        data = line.split(" - ")
        if not line:
            break
        for el in data[1::]:
            sal = int(el)
            i += 1
            money += sal
            if sal < 2000000:
                employees.append(data[0:1])
    print(f"Меньше 2 млн гвинейских франков получают - {employees}")
    print(f"Средняя величина дохода сотрудников департамента - {money / i:.2f} GNF")
