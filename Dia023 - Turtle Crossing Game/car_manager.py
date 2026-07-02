import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
CREATING_CARS = [
    -250, -230, -210, -190, -170, -150, -130, -110, -90, -70,
    -50, -30, -10, 10, 30, 50, 70, 90, 110, 130,
    150, 170, 190, 210, 230, 250
]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(300, random.choice(CREATING_CARS))

    def move(self):
        self.backward(STARTING_MOVE_DISTANCE)

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1: 
            y = random.choice(CREATING_CARS)

            for car in self.cars:
                if car.ycor() == y and car.xcor() > 200:
                    return
            
            new_car = Car()
            new_car.goto(300,y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

        for car in self.cars[:]:
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)

    def level_up(self):
        self.car_speed += 2

        

