with open("file_for_5_2.txt", "r", encoding="UTF-8") as my_file:
    el = 0
    for i, line in enumerate(my_file, 1):
        el += 1
        cnt = 1
        for x in line:
            if x == " ":
                cnt += 1
        print(f"{i, line} - {cnt} слов в строке")
    print(f"Всего строк в файле - {el}")
