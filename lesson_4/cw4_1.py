from sys import argv


def calc(ph, rate, prize):
    sal = int(ph) * int(rate) + int(prize)
    print(f'Заработная плата сотрудника составляет {sal}')


calc(*argv[1:])
