from turtle import Turtle
import random
CAR_COLORS = ["red", "blue", "pink", "green", "orange", "purple"]


class CarManager:
    def __init__(self):
        self.all_cars= []
        self.car_speed = 5

    def create_car(self):
        random_chance = random.randint(1, 6)  # so that cars are created little slowly
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.goto(x= 300, y = random.randint(-250, 250))

            new_car.shapesize(stretch_wid=1 , stretch_len=2)
            new_car.color(random.choice(CAR_COLORS))
            new_car.setheading(180)

            self.all_cars.append(new_car)

    def move_car(self):
        for car_obj in self.all_cars:
            car_obj.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 10
