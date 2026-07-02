from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle(280,0)
l_paddle = Paddle(-285,0)
ball = Ball()

score_r = Score(-30,270)
score_l = Score(30,270)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.0097)
    screen.update()
    ball.move()

    #detectando a colisão com as paredes
    if ball.ycor() > 285 or ball.ycor() < -285:
        #precisa 'quicar'
        ball.bounce()
    
    #detectando colisão com a defesa

    if ball.distance(r_paddle) < 18 or ball.distance( l_paddle) < 18:
        ball.bounce_paddle()

    if ball.xcor() > 290:
        score_r.update()
        ball.reset_position()

    if ball.xcor() < -290:
        score_l.update()
        ball.reset_position()

screen.exitonclick()