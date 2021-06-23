class Date:
    def __init__(self, date_met):
        self.date_met = date_met

    @classmethod
    def number_type(cls, current_date):
        date_int_type = [int(el) for el in current_date.date_met.split("-")]
        return date_int_type

    @staticmethod
    def valid_date():
        date_int_type = [int(el) for el in current_date.date_met.split("-")]
        if date_int_type[2] < 0 or not 1 < date_int_type[1] < 12 or date_int_type[0] > 31:
            print("Invalid data")


current_date = Date("32-03-2021")
current_date.valid_date()
print(Date.number_type(current_date))
