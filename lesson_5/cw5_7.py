import json

with open("file_for_5_7.txt", "r", encoding="UTF-8") as firms:
    firm_dict = {}
    ap_dict = {}
    data = []
    i = 0
    all_profit = 0
    for line in firms:
        f_list = line.split()
        name = f_list[0:1:]
        for el in f_list[2:3:]:
            proceeds = int(el)
        for el in f_list[3::]:
            costs = int(el)
        profit = proceeds - costs
        data.append(profit)
        for x in data:
            for y in f_list[0:1:]:
                firm_dict[y] = x
        i += 1
        if profit > 0:
            all_profit += profit
    average_profit = all_profit / i
    ap_dict["average_profit"] = average_profit
    my_list = [firm_dict, ap_dict]

with open("file_5_7.json", "w", encoding="UTF-8") as js_file:
    json.dump(my_list, js_file)
