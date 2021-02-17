my_list = []
while True:
    st = input("введите несколько чисел через пробел или введите ! для завершения программы: ")
    st_list = st.split()
    for el in st.split():
        if el != "!":
            my_list.append(float(el))
        else:
            break
    print(sum(my_list))

