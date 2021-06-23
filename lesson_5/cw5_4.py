with open("file_for_5_4.txt", "r", encoding="UTF-8") as my_file:
    numeral_dict = {}
    my_list = ["Один", "Два", "Три", "Четыре"]

    for i in my_list:
        line = my_file.readline()
        data = line.split(" — ")
        for el in data[1::]:
            numeral_dict[i] = el

with open("file_for_5_4(2).txt", "w", encoding="UTF-8") as new_file:
    for key, value in numeral_dict.items():
        print(key, " - ", value, end="", file=new_file)
