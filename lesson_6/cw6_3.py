class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


pos_worker = Position("Maruan", "Diallo", "specialist", 2500000, 100000)
print(f" Worker's full name - {pos_worker.get_full_name()}, his(her) total income = {pos_worker.get_total_income()}")
