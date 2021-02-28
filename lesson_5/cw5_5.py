my_file = open("file_for_5_5.txt", "w", encoding="UTF-8")
my_file.write("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
my_file.close()

my_file = open("file_for_5_5.txt", "r", encoding="UTF-8")
data = my_file.read().split()
sum_el = 0
for i in data:
    el = int(i)
    sum_el += el
print(sum_el)
my_file.close()
