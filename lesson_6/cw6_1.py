from time import sleep
from itertools import cycle


class TrafficLight:
    __color = {1: "Red", 2: "Yellow", 3: "Green"}

    def running(self):
        cnt = 12
        for key in cycle(TrafficLight.__color.keys()):
            print(f"{TrafficLight.__color.get(key)} traffic light is on")
            if key == 1:
                sleep(7)
            elif key == 2:
                sleep(2)
            elif key == 3:
                sleep(15)
            cnt -= 1
            if cnt == 0:
                break

my_traffic_light = TrafficLight()
my_traffic_light.running()
