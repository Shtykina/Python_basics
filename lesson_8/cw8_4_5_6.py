from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self, dimensions, capacity):
        self.dimensions = dimensions
        self.capacity = capacity
        self.temperature = 23
        self.moisture = 0.6
        self.storage = {"printer": [], "scanner": [], "copier": []}

    @abstractmethod
    def reception_equipment(self):
        pass


class OfficeEquipment(ABC):
    def __init__(self, model, serial_number, producing_country, dimensions):
        self.model = model
        self.serial_number = serial_number
        self.producing_country = producing_country
        self.dimensions = dimensions


class Printer(OfficeEquipment):
    def __init__(self, model, serial_number, producing_country, dimensions, monochrome_printing):
        super().__init__(model, serial_number, producing_country, dimensions)
        self.monochrome_printing = monochrome_printing

    def reception_equipment(self):
        print(f"")


class Scanner(OfficeEquipment):
    def __init__(self, model, serial_number, producing_country, dimensions, monochrome_scanning):
        super().__init__(model, serial_number, producing_country, dimensions)
        self.monochrome_scanning = monochrome_scanning


class Copier(OfficeEquipment):
    def __init__(self, model, serial_number, producing_country, dimensions, wifi_direct_technology):
        super().__init__(model, serial_number, producing_country, dimensions)
        self.wifi_direct_technology = wifi_direct_technology

