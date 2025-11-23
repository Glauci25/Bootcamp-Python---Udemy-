from turtle import Turtle, Screen
from random import choice
colors = ['red','blue','green','yellow','orange','purple','pink','cyan','magenta','gold','coral','salmon','tomato','brown','chocolate','darkgreen','deepskyblue','dodgerblue','mediumpurple','slategray','olivedrab','navy','teal','paleturquoise']
tim = Turtle()
tim.shape('turtle')

for x in range(3,11):
    angle = 360/x
    tim.color(choice(colors))
    for i in range(x):
        tim.forward(60)
        tim.right(360-angle)

screen = Screen()
screen.exitonclick()