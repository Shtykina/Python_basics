class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass = 25
        self.thickness = 5

    def calculation(self):
        calc = self._length * self._width * self.mass * self.thickness / 1000
        return calc


my_road = Road(500000, 10)
my_road.calculation()
print(f"The required mass of asphalt for a two-lane highway {my_road._length / 1000} km length "
      f"and {my_road._width} m width will be {my_road.calculation()} tons")
