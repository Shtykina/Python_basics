def user(name, surname, y_of_bth, c_of_res, email, tel):
    print(f"фамилия - {surname}; имя - {name}; год рождения - {y_of_bth}; "
          f"город проживания - {c_of_res}; email - {email}; номер телефона - {tel}")


user(name=input("Введите имя: "),
     surname=input("Введите фамилию: "),
     y_of_bth=input("Введите год рождения: "),
     c_of_res=input("Введите город проживания: "),
     email=input("Введите E-mail: "),
     tel=input("Введите номер телефона: "))
