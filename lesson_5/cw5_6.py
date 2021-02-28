with open("file_for_5_6.txt", "r", encoding="UTF-8") as sch_pr:
    my_dict = {}
    for line in sch_pr:
        sub_list = line.split(":")
        my_list = []
        for el in sub_list[1::]:
            hours = ""
            for x in el:
                if str(0) <= x <= str(9):
                    hours += x
                elif x == "(":
                    my_list.append(hours)
                    hours = ""
                    continue
            total = 0
            for x in my_list:
                time = int(x)
                total += time
                for name in sub_list[0:1:]:
                    my_dict[name] = total
print(my_dict)
