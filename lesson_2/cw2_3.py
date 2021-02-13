# list
a = input("Введите порядковый номер месяца (от 1 до 12): ")
if a == "1" or a == "2" or a == "12":
    print("winter")
elif a == "3" or a == "4" or a == "5":
    print("spring")
elif a == "6" or a == "7" or a == "8":
    print("summer")
elif a == "9" or a == "10" or a == "11":
    print("autumn")
else:
    print("Error")

# dict
seasons_dict = {
    "1": "winter",
    "2": "winter",
    "3": "spring",
    "4": "spring",
    "5": "spring",
    "6": "summer",
    "7": "summer",
    "8": "summer",
    "9": "autumn",
    "10": "autumn",
    "11": "autumn",
    "12": "winter"
}
a = input("Введите порядковый номер месяца (от 1 до 12): ")
print(seasons_dict[a])