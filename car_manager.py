from car import Car
from lane import Lane
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink", "gray"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self, window_width, window_height):
        self.level = 0
        self.cars = []
        self.window_width = window_width
        self.window_height = window_height
        self.lanes = []
        self.cars = []
        self.next_level()

    def next_level(self):
        self.level += 1
        for car in self.cars:
            car.reset()
            car.hideturtle()
        self.cars = []
        for lane_index in range(1, 25):
            car = Car(random.choice(COLORS), lane_index, self.level, self.window_width, self.window_height)
            #Each level we increase chances more cars exist per lane
            random_cars = random.randint(1, 10)
            self.cars.append(car)
            if random_cars < self.level:
                new_car = Car(random.choice(COLORS), lane_index, self.level, self.window_width, self.window_height)
                if new_car.distance(car) < 50:
                    new_car.setx(new_car.xcor() + 50)
                self.cars.append(new_car)





    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.has_left_screen():
                car.reposition()


