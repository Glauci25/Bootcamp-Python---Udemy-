import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detectando colisão da tartaruga com algum dos carros
    for car in car_manager.cars:
        if player.distance(car) < 25:
            score.game_over()
            game_is_on = False

    if player.ycor() > 280:
        score.win()
        player.go_back()
        car_manager.level_up()

screen.exitonclick()