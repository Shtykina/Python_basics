time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 3600 % 60
#print(hours, minutes, seconds)
print(f"{'%02d'%hours}:{'%02d'%minutes}:{'%02d'%seconds}")