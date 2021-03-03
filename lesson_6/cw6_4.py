class Car:
    def __init__(self, name, speed, color, is_police=True):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Your {self.name} has started.'

    def stop(self):
        return f'Your {self.name} has stopped.'

    def turn(self, direction):
        return f'Your {self.name} turned {direction}.'

    def show_speed(self):
        return f'Your speed is {self.speed}.'


class TownCar(Car):
    speed = 60
    def show_speed(self):
        if self.speed > TownCar.speed:
            return f'Your speed is {self.speed}. Over speed. Permitted speed in the town is 60 km/h!'


class SportCar(Car):
    pass


class WorkCar(Car):
    speed = 40
    def show_speed(self):
        if self.speed > WorkCar.speed:
            return f'Your speed is {self.speed}. Over speed. Permitted speed is 40 km/h!'


class PoliceCar(Car):
    pass


town_car = TownCar('Toyota', 70, 'black', True)
print(f"{town_car.go()} {town_car.show_speed()} {town_car.turn('left')} {town_car.stop()}")

sport_car = SportCar('BMW', 240, 'blue', True)
print(f"{sport_car.go()} {sport_car.show_speed()} {sport_car.turn('left')} {sport_car.stop()}")

work_car = WorkCar('Ford', 50, 'red', True)
print(f"{work_car.go()} {work_car.show_speed()} {work_car.turn('right')} {work_car.stop()}")

police_car = PoliceCar('Lada', 90, 'white', False)
print(f"{police_car.go()} {police_car.show_speed()} {police_car.turn('right')} {police_car.stop()}")
